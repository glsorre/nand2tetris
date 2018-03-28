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

def and_to_d(file):
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('A=A-1' + '\n')
  file.write('A=A-1' + '\n')
  file.write('D=M' + '\n')
  file.write('A=A+1' + '\n')
  file.write('D=D&M' + '\n')

def or_to_d(file):
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('A=A-1' + '\n')
  file.write('A=A-1' + '\n')
  file.write('D=M' + '\n')
  file.write('A=A+1' + '\n')
  file.write('D=D|M' + '\n')

def neg_to_d(file):
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('A=A-1' + '\n')
  file.write('D=M' + '\n')
  file.write('D=-D' + '\n')

def not_to_d(file):
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('A=A-1' + '\n')
  file.write('D=M' + '\n')
  file.write('D=!D' + '\n')

def operator_to_d(file, index, operator):
  label_true = 'TRUE' + str(index)
  label_end = 'END' + str(index)
  file.write('@' + label_true + '\n')
  file.write('D;J' + operator + '\n')
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('M=0' + '\n')
  file.write('@' + label_end + '\n')
  file.write('0;JMP' + '\n')
  file.write('(' + label_true + ')\n')
  file.write('@SP' + '\n')
  file.write('A=M' + '\n')
  file.write('M=-1' + '\n')
  file.write('(' + label_end + ')\n')
  file.write('@SP' + '\n')
  file.write('M=M+1' + '\n')