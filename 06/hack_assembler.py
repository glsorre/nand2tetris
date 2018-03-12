#!/usr/bin/env python
import cli.app
import copy
import re

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
    sep = '0'
    result = copy.copy(lines)
    
    for i, line in enumerate(lines):
        if sep != line[0:1]:
            a = re.split('=|;',line)
            
            binary = "111"
            
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