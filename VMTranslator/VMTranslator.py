import sys, os
import getopt

from parser import Parser
from code_writer import CodeWiter
from clean_function import eliminate_comments, eliminate_newlines


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

        if os.path.isdir(filename):
            output_filename = str(filename.split('/')[-1])
            output_filename = filename + '/' + output_filename + '.asm'
            print(output_filename)
            
            partial_filename = filename[:-3]
            current_file = filename

            code_writer = CodeWiter(output_filename, partial_filename)

            code_writer.write_init()
            code_writer.write_call('C_CALL', 'Sys.init', '0', 'boot')

            for file in os.listdir(filename):
                if file.endswith(".vm") and file != "Sys.vm":
                    
                    print(file)
                    file_position = filename + '/' + file
                    code_writer.set_file_name(file_position)

                    content = open(file_position).readlines()
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
                                command_type, parser.arg1(), parser.arg2())
                        elif command_type == 'C_LABEL':
                            code_writer.write_label(command_type, parser.arg1())
                        elif command_type == 'C_GOTO':
                            code_writer.write_goto(command_type, parser.arg1())
                        elif command_type == 'C_IF':
                            code_writer.write_if(command_type, parser.arg1())
                        elif command_type == 'C_CALL':
                            code_writer.write_call(command_type, parser.arg1(), parser.arg2(), str(parser.index))
                        elif command_type == 'C_FUNCTION':
                            code_writer.write_function(command_type, parser.arg1(), parser.arg2())
                        elif command_type == 'C_RETURN':
                            code_writer.write_return(command_type)
                        elif command_type == 'C_ARITHMETIC':
                            code_writer.write_arithmetic(parser.arg1(), parser.index)

                        parser.advance()

            for file in os.listdir(filename):
                if file.endswith(".vm") and file == "Sys.vm":
                    print(file)
                    file_position = filename + '/' + file
                    code_writer.set_file_name(file_position)

                    content = open(file_position).readlines()
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
                                command_type, parser.arg1(), parser.arg2())
                        elif command_type == 'C_LABEL':
                            code_writer.write_label(command_type, parser.arg1())
                        elif command_type == 'C_GOTO':
                            code_writer.write_goto(command_type, parser.arg1())
                        elif command_type == 'C_IF':
                            code_writer.write_if(command_type, parser.arg1())
                        elif command_type == 'C_CALL':
                            code_writer.write_call(command_type, parser.arg1(), parser.arg2(), str(parser.index))
                        elif command_type == 'C_FUNCTION':
                            code_writer.write_function(command_type, parser.arg1(), parser.arg2())
                        elif command_type == 'C_RETURN':
                            code_writer.write_return(command_type)
                        elif command_type == 'C_ARITHMETIC':
                            code_writer.write_arithmetic(parser.arg1(), parser.index)

                        parser.advance()
            
            code_writer.close()

        else:
            with open(filename) as f:
                content = f.readlines()
                content = [x.strip() for x in content]

            print(content)
            content = eliminate_comments(content)
            print(content)
            content = eliminate_newlines(content)
            print(content)

            partial_filename = filename[:-3]
            print(partial_filename)
            output_filename = partial_filename + '.asm'
            print(output_filename)

            parser = Parser(content)
            code_writer = CodeWiter(output_filename, partial_filename)

            while parser.has_more_commands():

                command_type = parser.command_type()
                print(command_type)
                print(parser.arg1())
                print(parser.arg2())

                if command_type in ["C_PUSH", "C_POP"]:
                    code_writer.write_push_pop(
                        command_type, parser.arg1(), parser.arg2())
                elif command_type == 'C_LABEL':
                    code_writer.write_label(command_type, parser.arg1())
                elif command_type == 'C_GOTO':
                    code_writer.write_goto(command_type, parser.arg1())
                elif command_type == 'C_IF':
                    code_writer.write_if(command_type, parser.arg1())
                elif command_type == 'C_FUNCTION':
                    code_writer.write_function(command_type, parser.arg1(), parser.arg2())
                elif command_type == 'C_RETURN':
                    code_writer.write_return(command_type)
                elif command_type == 'C_ARITHMETIC':
                    code_writer.write_arithmetic(parser.arg1(), parser.index)

                parser.advance()

            code_writer.close()


if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])
