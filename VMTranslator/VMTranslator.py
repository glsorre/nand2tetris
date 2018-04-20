import sys
import os
import getopt
import functools
from collections import deque

from parser import Parser
from code_writer import CodeWriter
from clean_function import eliminate_comments, eliminate_newlines


def is_dest_dir(dest):
    return os.path.isdir(dest)


def build_code_writer(dest):
    if is_dest_dir(dest):
        print('we have a dir')
        output_filename = str(dest.split('/')[-1])
        output_filename = os.path.join(dest, output_filename + '.asm')
        print(output_filename)
        code_writer = CodeWriter(output_filename, dest)
    else:
        print('we have a file')
        output_filename = dest[:-3] + '.asm'
        print(output_filename)
        code_writer = CodeWriter(output_filename, dest[:-3])
    return code_writer


def init_output_file(dest, code_writer):
    if is_dest_dir(dest):
        code_writer.write_init()
        code_writer.write_call('C_CALL', 'Sys.init', '0', 'bootstrap')


def build_output_file(dest, code_writer):
    if is_dest_dir(dest):
        files = os.listdir(dest)
        print(files)
        files.remove('Sys.vm')
        print(files)
        files = list(filter(lambda x: x[-3:] == '.vm', files))
        print(files)
        files = list(map(functools.partial(os.path.join, dest), files))
        print(files)
        files.append(os.path.join(dest, 'Sys.vm'))
        print(files)
        
        deque(map(functools.partial(process_file, code_writer), files))

    else:
        process_file(code_writer, dest)


def process_file(code_writer, file):
    code_writer.set_file_name(file)
    
    content = open(file).readlines()

    content = [x.strip() for x in content]
    print(content)
    content = eliminate_comments(content)
    print(content)
    content = eliminate_newlines(content)
    print(content)

    parser = Parser(content)

    while parser.has_more_commands():

        command_type = parser.command_type()
        print(command_type)
        print(parser.arg1())
        print(parser.arg2())

        if command_type in ["C_PUSH", "C_POP"]:
            code_writer.write_push_pop(
                command_type,
                parser.arg1(),
                parser.arg2()
            )
        elif command_type == 'C_LABEL':
            code_writer.write_label(
                command_type,
                parser.arg1(),
                code_writer.static_name
            )
        elif command_type == 'C_GOTO':
            code_writer.write_goto(
                command_type,
                parser.arg1(),
                code_writer.static_name
            )
        elif command_type == 'C_IF':
            code_writer.write_if(
                command_type,
                parser.arg1(),
                code_writer.static_name
            )
        elif command_type == 'C_CALL':
            code_writer.write_call(
                command_type,
                parser.arg1(),
                parser.arg2(),
                str(Parser.count)
            )
        elif command_type == 'C_FUNCTION':
            code_writer.write_function(
                command_type,
                parser.arg1(),
                parser.arg2(),
                code_writer.static_name
            )
        elif command_type == 'C_RETURN':
            code_writer.write_return(command_type)
        elif command_type == 'C_ARITHMETIC':
            code_writer.write_arithmetic(
                parser.arg1(),
                str(Parser.count)
            )

        parser.advance()


def close_file(code_writer):
    code_writer.close()


def main(argv):
    print(argv)
    try:
        opts, args = getopt.getopt(argv, "")
    except getopt.GetoptError:
        print('vmTanslator.py <inputfile.vm> or <directory> containing Sys.vm')
        sys.exit(2)

    if len(args) > 1:
        print('vmTanslator.py <inputfile.vm> or <directory> containing Sys.vm')
        sys.exit(2)
    else:
        filename = args[0]
        print(filename)

        code_writer = build_code_writer(filename)

        init_output_file(filename, code_writer)
        build_output_file(filename, code_writer)

        close_file(code_writer)


if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])
