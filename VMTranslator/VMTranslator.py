import sys, getopt

from parser import Parser
from code_writer import CodeWiter
from clean_function import eliminate_comments, eliminate_newlines

def main(argv):
  print(argv)
  try:
    opts, args = getopt.getopt(argv,"")
  except getopt.GetoptError:
    print ('vmTanslator.py <inputfile.vm>')
    sys.exit(2)

  if len(args) > 1:
    print ('vmTanslator.py <inputfile.vm>')
    sys.exit(2)
  else:
    filename = args[0]
    print(filename)

    with open(filename) as f:
      content = f.readlines()
      # remove whitespace characters like `\n` at the end of each line
      # content = [x.strip() for x in content]

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
        code_writer.write_push_pop(command_type, parser.arg1(), parser.arg2())
      elif command_type == 'C_LABEL':
        code_writer.write_label(command_type, parser.arg1())
      elif command_type == 'C_GOTO':
        code_writer.write_goto(command_type, parser.arg1())
      elif command_type == 'C_IF':
        code_writer.write_if(command_type, parser.arg1())
      elif command_type == 'C_ARITHMETIC':
        code_writer.write_arithmetic(parser.arg1(), parser.index)
        
      parser.advance()

    code_writer.close()


if __name__ == "__main__":
  print(sys.argv)
  main(sys.argv[1:])