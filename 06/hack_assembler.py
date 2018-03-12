#!/usr/bin/env python
import cli.app
import copy
import re

computation = {
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
    '-M':   '1110011',
    'M+1':  '1110111',
    'M-1':  '1110010',
    'D+M':  '1000010',
    'D-M':  '1010011',
    'M-D':  '1000111',
    'D&M':  '1000000',
    'D|M':  '1010101'
}

destination = {
    'None': '000',
    'D':    '010',
    'MD':   '011',
    'A':    '100',
    'AM':   '101',
    'AD':   '110',
    'AM':   '111'
}

def eliminate_comments(lines):
    sep = '//'
    result = copy.copy(lines)
    
    for i, line in enumerate(lines):
        if sep == line[0:2]:
            result.remove(line)
    
    return result
    
def eliminate_newlines(lines):
    sep = '\n'
    result = copy.copy(lines)
    
    for i, line in enumerate(lines):
        if sep == line:
            result.remove(line)
    
    return result
    
def parse_a(lines):
    sep = '@'
    result = copy.copy(lines)
    
    for i, line in enumerate(lines):
        if sep == line[0:1]:
            a = line.split('@')
            binary = bin(int(a[1]))[2:].zfill(15)
            
            result[i] = "0" + binary + '\n'

    return result
    
def parse_c(lines):
    result = copy.copy(lines)
    
    for i, line in enumerate(lines):
        if line[0:1] != '01' or line[0:1] != '00':
            print(line)
            a = re.split('[;|=]', line)
            print(a)
            print(len(a))
            
            comp = 0
            dest = 0
            jmp = 0 

            if len(a) == 2 and "=" in line:
                print('assegnazione')
                comp = computation[a[1]]
                dest = destination[a[0]]
                jump = '000'
            elif len(a) == 2 and ";" in line:
                print('jump')
            else:
                print('assegnazione e jump')
            
            binary = "111" + comp + dest + jmp
            
            
            result[i] = binary + '\n'
            
    return result

@cli.app.CommandLineApp
def hack_assembler(app):
    
    with open(app.params.file, encoding="utf-8") as f:
        content = f.readlines()
    
    result = eliminate_comments(content)
    result = eliminate_newlines(result)
    result = parse_a(result)
    result = parse_c(result)
    print(''.join(result))
    
hack_assembler.add_param('file', metavar='FILE', help='The asm file.')

if __name__ == "__main__":
    hack_assembler.run()