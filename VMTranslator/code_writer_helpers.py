def set_a_to_m(file, value):
    file.write('@' + str(value) + '\n')
    file.write('A=M' + '\n')


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
    set_a_to_m(file, address)
    file.write('D=M' + '\n')


def set_m_to_d_pointer(file, address):
    set_a_to_m(file, address)
    file.write('M=D' + '\n')


def set_d_to_m_pointer_plus_d(file, base, address):
    set_d_to_value(file, address)
    set_a_to_m(file, base)
    file.write('D=D+A' + '\n')
    file.write('A=D' + '\n')
    file.write('D=M' + '\n')


def set_m_to_d_pointer_plus_d(file, base, address, temp_address):
    set_d_to_value(file, address)
    set_a_to_m(file, base)
    file.write('D=D+A' + '\n')
    set_m_to_d(file, temp_address)


def sp_plus(file):
    file.write('@SP' + '\n')
    file.write('M=M+1' + '\n')


def sp_minus(file):
    file.write('@SP' + '\n')
    file.write('M=M-1' + '\n')


def sp_plus_two(file):
    sp_plus(file)
    file.write('M=M+1' + '\n')


def sp_minus_two(file):
    sp_minus(file)
    file.write('M=M-1' + '\n')


def write_label(file, label):
    file.write('(' + label + ')\n')


def write_goto(file, label):
    file.write('@' + label + '\n')
    file.write('0;JMP' + '\n')

# possible operator: + - & |


def basic_operation_to_d(file, operator):
    set_a_to_m(file, 'SP')
    file.write('A=A-1' + '\n')
    file.write('A=A-1' + '\n')
    file.write('D=M' + '\n')
    file.write('A=A+1' + '\n')
    file.write('D=D' + operator + 'M' + '\n')

# possible operator: - !


def single_operation_to_d(file, operator):
    set_a_to_m(file, 'SP')
    file.write('A=A-1' + '\n')
    file.write('D=M' + '\n')
    file.write('D=' + operator + 'D' + '\n')

# possible operator: EQ LT GT


def eq_operation_to_d(file, index, operator):
    label_true = 'true.' + str(index)
    label_end = 'end.' + str(index)
    file.write('@' + label_true + '\n')
    file.write('D;J' + operator + '\n')
    set_a_to_m(file, 'SP')
    file.write('M=0' + '\n')
    #file.write('@' + label_end + '\n')
    #file.write('0;JMP' + '\n')
    write_goto(file, label_end)
    #file.write('(' + label_true + ')\n')
    write_label(file, label_true)
    set_a_to_m(file, 'SP')
    file.write('M=-1' + '\n')
    #file.write('(' + label_end + ')\n')
    write_label(file, label_end)
    sp_plus(file)

def get_return_address(file, index, address):
    file.write('@' + index + '\n')
    file.write('D=D-A' + '\n')
    file.write('A=D' + '\n')
    file.write('D=M' + '\n')
    set_m_to_d(file, address)

def restore_caller_address(file, index, address):
    set_d_to_m_pointer(file, 'endFrame')
    get_return_address(file, index, address)
