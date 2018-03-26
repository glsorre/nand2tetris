import sys, getopt, copy

class Parser:
  def __init__(self, lines):
    self.lines = lines
    self.index = 0
    self.tot = len(lines)
  
  def has_more_commands(self):
    print(self.index)
    print(self.tot)
    if self.index < self.tot:
      return True
    else:
      return False

  def advance(self):
    self.index += 1

  def command_type(self):
    line = self.lines[self.index].split(' ')
    if line[0] == 'push':
      return 'C_PUSH'
    elif line[0] == 'pop':
      return 'C_POP'
    elif line[0] in ['add', 'sub', 'eq', 'lt' 'gt']:
      return 'C_ARITHMETIC'
    else:
      return None
  
  def arg1(self):
    line = self.lines[self.index].split(' ')

    command_type = self.command_type()

    if command_type in ['C_PUSH', 'C_POP']:
      return line[1]
    elif command_type == 'C_ARITHMETIC':
      return line[0]

  def arg2(self):
    line = self.lines[self.index].split(' ')

    command_type = self.command_type()

    if command_type in ['C_PUSH', 'C_POP']:
      return line[2]
    elif command_type == 'C_ARITHMETIC':
      return None

class CodeWiter:
  def __init__(self, filename):
    self.lines = []
    self.file = open(filename, 'w')
  
  def write_arithmetic(self, command):
    #do something
    self.file.write("arithmetic\n")

  def write_push_pop(self, segment, index):
    #do something
    self.file.write("pushpop\n")

  def close(self):
    self.file.close()    

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
  
    return result

def eliminate_newlines(lines):
    sep = '\n'
    result = copy.copy(lines)

    for i, line in enumerate(lines):
        if sep == line:
            result.remove(line)

    for i, line in enumerate(result):
        result[i] = line.strip()

    return result

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
    code_writer = CodeWiter(output_filename)

    while parser.has_more_commands():
      
      command_type = parser.command_type()
      print(command_type)
      print(parser.arg1())
      print(parser.arg2())
      
      if command_type in ["C_PUSH", "C_POP"]:
        code_writer.write_push_pop(parser.arg1(), parser.arg2())
      elif command_type == 'C_ARITHMETIC':
        code_writer.write_arithmetic(parser.arg1())
        
      parser.advance()

    code_writer.close()


if __name__ == "__main__":
  print(sys.argv)
  main(sys.argv[1:])