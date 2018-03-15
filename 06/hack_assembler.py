#!/usr/bin/env python

import copy
import re
import logging

import cli.app

COMPUTATION = {
    '0':    '0101010',
    '1':    '0111111',
    '-1':   '0111010',
    'D':    '0001100',
    'A':    '0110000',
    '!D':   '0001101',
    '!A':   '0110001',
    '-D':   '0001111',
    '-A':   '0110011',
    'D+1':  '0011111',
    'A+1':  '0110111',
    'D-1':  '0001110',
    'A-1':  '0110010',
    'D+A':  '0000010',
    'D-A':  '0010011',
    'A-D':  '0000111',
    'D&A':  '0000000',
    'D|A':  '0010101',
    'M':    '1110000',
    '!M':   '1110001',
    '-M':   '1110011',
    'M+1':  '1110111',
    'M-1':  '1110010',
    'D+M':  '1000010',
    'D-M':  '1010011',
    'M-D':  '1000111',
    'D&M':  '1000000',
    'D|M':  '1010101'
}

DESTINATION = {
    'none': '000',
    'M':    '001',
    'D':    '010',
    'MD':   '011',
    'A':    '100',
    'AM':   '101',
    'AD':   '110',
    'AMD':  '111'
}

JUMP = {
    'none': '000',
    'JGT':  '001',
    'JEQ':  '010',
    'JGE':  '011',
    'JLT':  '100',
    'JNE':  '101',
    'JLE':  '110',
    'JMP':  '111'
}

LABELS = {

}

VARIABLES = {
    'SP':       0,
    'LCL':      1,
    'ARG':      2,
    'THIS':     3,
    'THAT':     4,
    'R0':       0,
    'R1':       1,
    'R2':       2,
    'R3':       3,
    'R4':       4,
    'R5':       5,
    'R6':       6,
    'R7':       7,
    'R8':       8,
    'R9':       9,
    'R10':      10,
    'R11':      11,
    'R12':      12,
    'R13':      13,
    'R14':      14,
    'R15':      15,
    'SCREEN':   16384,
    'KBD':      24576
}

def eliminate_comments(lines):
    sep = '//'
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        if sep == line[0:2]:
            result.remove(line)

    for i, line in enumerate(result):
        if sep in line:
            temp = line.split(sep)
            temp = temp[0].strip()
            result[i] = temp

    logging.debug('File content - no comments: %s/n', result)
    return result

def eliminate_newlines(lines):
    sep = '\n'
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        if sep == line:
            result.remove(line)

    for i, line in enumerate(result):
        result[i] = line.strip()

    logging.debug('File content - no newlines: %s/n', result)
    return result

def collect_labels(lines):
    counter = 0
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        if '(' in line and ')' in line:
            label = line[1:-1]
            LABELS[label] = i - counter
            counter += 1

    for i, line in enumerate(lines):
        if '(' in line and ')' in line:
            result.remove(line)

    logging.debug('File content - labels: %s/n', LABELS)
    logging.debug('File content - collect labels: %s/n', result)
    return result

def collect_variables(lines):
    sep = '@'
    start = VARIABLES['R15'] + 1

    for i, line in enumerate(lines):
        if sep == line[0:1]:
            a = line.split('@')

            try:
                label = int(a[1])
            except:
                label = str(a[1])

            if isinstance(label, str) and label not in LABELS.keys() and label not in VARIABLES.keys():
                VARIABLES[label] = start
                start += 1

    logging.debug('File content - VARIABLES: %s/n', VARIABLES)
    logging.debug('File content - collect variables: %s/n', lines)
    return lines

def parse_variables(lines):
    sep = '@'

    for i, line in enumerate(lines):
        #logging.debug('Line content - parse variables: %s/n' % line)
        if sep == line[0:1]:
            a = line.split('@')
            if a[1] in LABELS.keys():
                a[1] = LABELS[a[1]]
            elif a[1] in VARIABLES.keys():
                a[1] = VARIABLES[a[1]]

            lines[i] = '@'.join(str(e) for e in a)

    logging.debug('File content - parse variables: %s/n', lines)
    return lines

def parse_a(lines):
    sep = '@'
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        #logging.debug('Line content - a instructions: %s/n' % line)
        if sep == line[0:1]:
            a = line.split('@')
            binary = bin(int(a[1]))[2:].zfill(15)

            result[i] = "0" + binary + '\n'

    logging.debug('File content - a instructions: %s/n', result)
    return result

def parse_c(lines):
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        logging.debug('Line content - c instructions: %s/n', line)
        if line[0:2] != '00' and line[0:2] != '01':
            a = re.split('[;=]', line)

            comp = 0
            dest = 0
            jmp = 0

            if len(a) == 2 and "=" in line:
                comp = COMPUTATION[a[1]]
                dest = DESTINATION[a[0]]
                jmp = JUMP['none']
            elif len(a) == 2 and ";" in line:
                comp = COMPUTATION[a[0]]
                dest = DESTINATION['none']
                jmp = JUMP[a[1]]
            else:
                comp = COMPUTATION[a[1]]
                dest = DESTINATION[a[0]]
                jmp = JUMP[a[2]]

            binary = "111" + comp + dest + jmp

            if i < len(lines)-1:
                result[i] = binary + '\n'
            else:
                result[i] = binary

    logging.debug('File content - c instrunctions: %s/n', result)
    return result



#@cli.app.CommandLineApp
def hack_assembler(app):
    if app.params.debug:
        logging.basicConfig(filename=app.params.file+'.compile_log', filemode='w', level=logging.DEBUG)
    else:
        logging.basicConfig(filename=app.params.file+'.compile_log', filemode='w', level=logging.INFO)

    logging.info('### COMPILATION STARTED')

    with open(app.params.file, encoding="utf-8") as f:
        content = f.readlines()

    logging.debug('File content: %s', content)

    logging.info('### ELIMINATING COMMENTS...')
    result = eliminate_comments(content)
    logging.info('### ELIMINATING COMMENTS...DONE')

    logging.info('### ELIMINATING NEWLINES...')
    result = eliminate_newlines(result)
    logging.info('### ELIMINATING NEWLINES...DONE')

    logging.info('### COLLECTING LABELS...')
    result = collect_labels(result)
    logging.info('### COLLECTING LABELS...DONE')

    logging.info('### COLLECTING VARIABLES...')
    result = collect_variables(result)
    logging.info('### COLLECTING VARIABLES...DONE')

    logging.info('### PARSE VARIABLES...')
    result = parse_variables(result)
    logging.info('### PARSE VARIABLES...DONE')

    logging.info('### PARSING A INSTRUNCTIONS...')
    result = parse_a(result)
    logging.info('### PARSING A INSTRUNCTIONS DONE...')

    logging.info('### PARSING C INSTRUNCTIONS...')
    result = parse_c(result)
    logging.info('### PARSING C INSTRUNCTIONS DONE...')

    print(''.join(str(e) for e in result))

hack_assembler = cli.app.CommandLineApp(hack_assembler)
hack_assembler.add_param('file', metavar='FILE', help='The asm file.')
hack_assembler.add_param("-d", "--debug", help="log level to debug", default=False, action="store_true")

if __name__ == "__main__":
    hack_assembler.run()
