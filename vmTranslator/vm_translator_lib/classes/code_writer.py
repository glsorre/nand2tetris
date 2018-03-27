def set_d_to_value(file, value):
  file.write('@' + str(value) + '\n')
  file.write('D=A' + '\n')

def set_d_to_m(file, address):
  file.write('@' + str(address) + '\n')
  file.write('D=M' + '\n')

def set_m_to_d(file, address):
  file.write('@' + str(address) + '\n')
  file.write('M=D' + '\n')

def set_d_to_m_pointer(file, address):
  file.write('@' + str(address) + '\n')
  file.write('A=M' + '\n')
  file.write('D=M' + '\n')

def set_m_to_d_pointer(file, address):
  file.write('@' + str(address) + '\n')
  file.write('A=M' + '\n')
  file.write('M=D' + '\n')

def set_d_to_m_pointer_plus_d(file, base, address):
  file.write('@' + address + '\n')
  file.write('D=A' + '\n')
  file.write('@' + base + '\n')
  file.write('A=M' + '\n')
  file.write('D=D+A' + '\n')
  file.write('A=D' + '\n')
  file.write('D=M' + '\n')

def set_m_to_d_pointer_plus_d(file, base, address):
  file.write('@' + address + '\n')
  file.write('D=A' + '\n')
  file.write('@' + base + '\n')
  file.write('A=M' + '\n')
  file.write('D=D+A' + '\n')
  file.write('@R13' + '\n')
  file.write('M=D' + '\n')
  
def sp_plus(file):
  file.write('@SP' + '\n')
  file.write('M=M+1' + '\n')
  
def sp_minus(file):
  file.write('@SP' + '\n')
  file.write('M=M-1' + '\n')

def sp_plus_two(file):
  file.write('@SP' + '\n')
  file.write('M=M+1' + '\n')
  file.write('M=M+1' + '\n')
  
def sp_minus_two(file):
  file.write('@SP' + '\n')
  file.write('M=M-1' + '\n')
  file.write('M=M-1' + '\n')

def add_to_d(file):
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('A=A-1' + '\n')
  file.write('A=A-1' + '\n')
  file.write('D=M' + '\n')
  file.write('A=A+1' + '\n')
  file.write('D=D+M' + '\n')

def sub_to_d(file):
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('A=A-1' + '\n')
  file.write('A=A-1' + '\n')
  file.write('D=M' + '\n')
  file.write('A=A+1' + '\n')
  file.write('D=D-M' + '\n')


class CodeWiter:
  def __init__(self, filename):
    self.lines = []
    self.file = open(filename, 'w')
  
  def write_arithmetic(self, command, action):
    self.file.write('// ' + action + '\n')
    if action == 'add':
      add_to_d(self.file)
      sp_minus_two(self.file)
      set_m_to_d_pointer(self.file, 'SP')
      sp_plus(self.file)
    elif action == 'sub':
      sub_to_d(self.file)
      sp_minus_two(self.file)
      set_m_to_d_pointer(self.file, 'SP')
      sp_plus(self.file)
    self.file.write("\n")

  def write_push_pop(self, command, segment, index):
    if command == 'C_PUSH':
      self.file.write('// push ' + segment + ' ' + index + '\n')
      if segment == 'constant':
        set_d_to_value(self.file, index)
        set_m_to_d_pointer(self.file, 'SP')
        sp_plus(self.file)
      elif segment == 'temp':
        address = 5 + int(index)
        set_d_to_m(self.file, address)
        set_m_to_d_pointer(self.file, 'SP')
        sp_plus(self.file)
      elif segment == 'local':
        set_d_to_m_pointer_plus_d(self.file, 'LCL', index)
        set_m_to_d_pointer(self.file, 'SP')
        sp_plus(self.file)
      elif segment == 'argument':
        set_d_to_m_pointer_plus_d(self.file, 'ARG', index)
        set_m_to_d_pointer(self.file, 'SP')
        sp_plus(self.file)
      elif segment == 'this':
        set_d_to_m_pointer_plus_d(self.file, 'THIS', index)
        set_m_to_d_pointer(self.file, 'SP')
        sp_plus(self.file)
      elif segment == 'that':
        set_d_to_m_pointer_plus_d(self.file, 'THAT', index)
        set_m_to_d_pointer(self.file, 'SP')
        sp_plus(self.file)
      self.file.write('\n')
    else:
      self.file.write('// pop ' + segment + ' ' + index + '\n')
      if segment == 'temp':
        sp_minus(self.file)
        set_d_to_m_pointer(self.file, 'SP')
        address = 5 + int(index)
        set_m_to_d(self.file, address)
      elif segment == 'local':
        sp_minus(self.file)
        set_m_to_d_pointer_plus_d(self.file, 'LCL', index)
        set_d_to_m_pointer(self.file, 'SP')
        set_m_to_d_pointer(self.file, 'R13')
      elif segment == 'argument':
        sp_minus(self.file)
        set_m_to_d_pointer_plus_d(self.file, 'ARG', index)
        set_d_to_m_pointer(self.file, 'SP')
        set_m_to_d_pointer(self.file, 'R13')
      elif segment == 'this':
        sp_minus(self.file)
        set_m_to_d_pointer_plus_d(self.file, 'THIS', index)
        set_d_to_m_pointer(self.file, 'SP')
        set_m_to_d_pointer(self.file, 'R13')
      elif segment == 'that':
        sp_minus(self.file)
        set_m_to_d_pointer_plus_d(self.file, 'THAT', index)
        set_d_to_m_pointer(self.file, 'SP')
        set_m_to_d_pointer(self.file, 'R13')
      self.file.write('\n')
  

  def close(self):
    self.file.close()    