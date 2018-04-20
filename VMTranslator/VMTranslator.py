import sys, os
import getopt

from parser import Parser
from code_writer import CodeWriter
from clean_function import eliminate_comments, eliminate_newlines

class Main:
    def __init__(self, dest):
        self.dest = dest
        self.code_writer = None

    def is_dest_dir(self):
        return os.path.isdir(self.dest)

    def init_code_writer(self):
        if self.is_dest_dir():
            print('we have a dir')
            output_filename = str(self.dest.split('/')[-1])
            output_filename = self.dest + '/' + output_filename + '.asm'
            print(output_filename)
            self.code_writer = CodeWriter(output_filename, self.dest)
        else:
            print('we have a file')
            output_filename = self.dest[:-3] + '.asm'
            print(output_filename)
            self.code_writer = CodeWriter(output_filename, self.dest[:-3])

    def init_output_file(self):
        if self.is_dest_dir():
            self.code_writer.write_init()
            self.code_writer.write_call('C_CALL', 'Sys.init', '0', 'bootstrap')

    def build_output_file(self):
        if self.is_dest_dir():
            for file in os.listdir(self.dest):
                self.code_writer.set_file_name(self.dest + '/' + file)
                if file.endswith(".vm") and file != "Sys.vm":
                    self.process_file(self.dest + '/' + file)
            
            for file in os.listdir(self.dest):
                self.code_writer.set_file_name(self.dest + '/' + file)
                if file.endswith(".vm") and file == "Sys.vm":
                    self.process_file(self.dest + '/' + file)
        
        else:
            self.process_file(self.dest)

    def process_file(self, file):
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
                self.code_writer.write_push_pop(
                    command_type,
                    parser.arg1(),
                    parser.arg2()
                    )
            elif command_type == 'C_LABEL':
                self.code_writer.write_label(
                    command_type,
                    parser.arg1(),
                    self.code_writer.static_name
                    )
            elif command_type == 'C_GOTO':
                self.code_writer.write_goto(
                    command_type,
                    parser.arg1(),
                    self.code_writer.static_name
                    )
            elif command_type == 'C_IF':
                self.code_writer.write_if(
                    command_type,
                    parser.arg1(),
                    self.code_writer.static_name
                    )
            elif command_type == 'C_CALL':
                self.code_writer.write_call(
                    command_type,
                    parser.arg1(),
                    parser.arg2(),
                    str(Parser.count)
                    )
            elif command_type == 'C_FUNCTION':
                self.code_writer.write_function(
                    command_type,
                    parser.arg1(),
                    parser.arg2(),
                    self.code_writer.static_name
                    )
            elif command_type == 'C_RETURN':
                self.code_writer.write_return(command_type)
            elif command_type == 'C_ARITHMETIC':
                self.code_writer.write_arithmetic(
                    parser.arg1(),
                    str(Parser.count)
                    )

            parser.advance()

    def close_file(self):
        self.code_writer.close()

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

        ork = Main(filename)

        ork.init_code_writer()
        ork.init_output_file()
        ork.build_output_file()
        ork.close_file()

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])
