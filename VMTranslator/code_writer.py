from code_writer_helpers import *


class CodeWriter:
    def __init__(self, filename, partialname):
        self.lines = []
        self.file = open(filename, 'w')
        self.TMP = 5
        self.static_name = partialname.split('/')[-1]
        print(self.static_name)

    def set_file_name(self, partialname):
        self.static_name = partialname.split('/')[-1]

    def write_init(self):
        self.file.write('//  init' + '\n')
        set_d_to_value(self.file, '256')
        set_m_to_d(self.file, 'SP')
        self.file.write('\n')

    def write_arithmetic(self, action, parser_index):
        self.file.write('// ' + action + '\n')

        if action == 'add':
            basic_operation_to_d(self.file, '+')
            sp_minus_two(self.file)
            set_m_to_d_pointer(self.file, 'SP')
            sp_plus(self.file)

        elif action == 'sub':
            basic_operation_to_d(self.file, '-')
            sp_minus_two(self.file)
            set_m_to_d_pointer(self.file, 'SP')
            sp_plus(self.file)

        elif action == 'or':
            basic_operation_to_d(self.file, '|')
            sp_minus_two(self.file)
            set_m_to_d_pointer(self.file, 'SP')
            sp_plus(self.file)

        elif action == 'and':
            basic_operation_to_d(self.file, '&')
            sp_minus_two(self.file)
            set_m_to_d_pointer(self.file, 'SP')
            sp_plus(self.file)

        elif action == 'neg':
            single_operation_to_d(self.file, '-')
            sp_minus(self.file)
            set_m_to_d_pointer(self.file, 'SP')
            sp_plus(self.file)

        elif action == 'not':
            single_operation_to_d(self.file, '!')
            sp_minus(self.file)
            set_m_to_d_pointer(self.file, 'SP')
            sp_plus(self.file)

        elif action == 'eq':
            basic_operation_to_d(self.file, '-')
            sp_minus_two(self.file)
            eq_operation_to_d(self.file, parser_index, 'EQ')

        elif action == 'lt':
            basic_operation_to_d(self.file, '-')
            sp_minus_two(self.file)
            eq_operation_to_d(self.file, parser_index, 'LT')

        elif action == 'gt':
            basic_operation_to_d(self.file, '-')
            sp_minus_two(self.file)
            eq_operation_to_d(self.file, parser_index, 'GT')

        self.file.write("\n")

    def write_push_pop(self, command, segment, index):
        if command == 'C_PUSH':
            self.file.write('// push ' + segment + ' ' + index + '\n')

            if segment == 'constant':
                set_d_to_value(self.file, index)
                set_m_to_d_pointer(self.file, 'SP')
                sp_plus(self.file)

            elif segment == 'pointer':
                if index == '0':
                    set_d_to_m(self.file, 'THIS')
                    set_m_to_d_pointer(self.file, 'SP')
                    sp_plus(self.file)
                else:
                    set_d_to_m(self.file, 'THAT')
                    set_m_to_d_pointer(self.file, 'SP')
                    sp_plus(self.file)

            elif segment == 'static':
                address = self.static_name[:-3] + '$' + index
                set_d_to_m(self.file, address)
                set_m_to_d_pointer(self.file, 'SP')
                sp_plus(self.file)

            elif segment == 'temp':
                address = self.TMP + int(index)
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
                address = self.TMP + int(index)
                set_m_to_d(self.file, address)

            elif segment == 'pointer':
                if index == '0':
                    sp_minus(self.file)
                    set_d_to_m_pointer(self.file, 'SP')
                    set_m_to_d(self.file, 'THIS')
                else:
                    sp_minus(self.file)
                    set_d_to_m_pointer(self.file, 'SP')
                    set_m_to_d(self.file, 'THAT')

            elif segment == 'static':
                sp_minus(self.file)
                set_d_to_m_pointer(self.file, 'SP')
                address = self.static_name[:-3] + '$' + index
                set_m_to_d(self.file, address)

            elif segment == 'local':
                sp_minus(self.file)
                set_m_to_d_pointer_plus_d(self.file, 'LCL', index, 'R13')
                set_d_to_m_pointer(self.file, 'SP')
                set_m_to_d_pointer(self.file, 'R13')

            elif segment == 'argument':
                sp_minus(self.file)
                set_m_to_d_pointer_plus_d(self.file, 'ARG', index, 'R13')
                set_d_to_m_pointer(self.file, 'SP')
                set_m_to_d_pointer(self.file, 'R13')

            elif segment == 'this':
                sp_minus(self.file)
                set_m_to_d_pointer_plus_d(self.file, 'THIS', index, 'R13')
                set_d_to_m_pointer(self.file, 'SP')
                set_m_to_d_pointer(self.file, 'R13')

            elif segment == 'that':
                sp_minus(self.file)
                set_m_to_d_pointer_plus_d(self.file, 'THAT', index, 'R13')
                set_d_to_m_pointer(self.file, 'SP')
                set_m_to_d_pointer(self.file, 'R13')
            self.file.write('\n')

    def write_label(self, command, label, file):
        self.file.write('// label ' + label + '\n')
        write_label(self.file, file + '$' + label)
        self.file.write('\n')

    def write_goto(self, command, label, file):
        self.file.write('// goto ' + label + '\n')
        write_goto(self.file, file + '$' + label)
        self.file.write('\n')

    def write_if(self, command, label, file):
        self.file.write('// if-goto ' + label + '\n')
        sp_minus(self.file)
        set_d_to_m_pointer(self.file, 'SP')
        self.file.write('@' + file + '$' + label + '\n')
        self.file.write('D;JNE' + '\n')
        self.file.write('\n')

    def write_call(self, command, name, args, index):
        self.file.write('// call ' + name + ' ' + args + '\n')
        set_d_to_value(self.file, 'RETURN$' + index)
        set_m_to_d_pointer(self.file, 'SP')

        sp_plus(self.file)
        set_d_to_m(self.file, 'LCL')
        set_m_to_d_pointer(self.file, 'SP')

        sp_plus(self.file)
        set_d_to_m(self.file, 'ARG')
        set_m_to_d_pointer(self.file, 'SP')

        sp_plus(self.file)
        set_d_to_m(self.file, 'THIS')
        set_m_to_d_pointer(self.file, 'SP')

        sp_plus(self.file)
        set_d_to_m(self.file, 'THAT')
        set_m_to_d_pointer(self.file, 'SP')

        sp_plus(self.file)
        self.file.write('D=M' + '\n')
        self.file.write('@' + args + '\n')
        self.file.write('D=D-A' + '\n')
        self.file.write('@5' + '\n')
        self.file.write('D=D-A' + '\n')
        set_m_to_d(self.file, 'ARG')

        set_d_to_m(self.file, 'SP')
        set_m_to_d(self.file, 'LCL')
        self.file.write('@' + name + '\n')
        self.file.write('0;JMP' + '\n')
        write_label(self.file, 'RETURN$' + index)
        self.file.write('\n')

    def write_function(self, command, name, args, file):
        self.file.write('// function ' + file + ' ' + args + '\n')
        write_label(self.file, name)
        for i in range(int(args)):
            set_a_to_m(self.file, 'SP')
            self.file.write('M=0' + '\n')
            sp_plus(self.file)
        self.file.write('\n')

    def write_return(self, command):
        self.file.write('// return ' + '\n')
        set_d_to_m(self.file, 'LCL')
        set_m_to_d(self.file, 'endFrame')

        get_return_address(self.file, '5', 'retAddr')

        sp_minus(self.file)
        self.file.write('A=M' + '\n')
        self.file.write('D=M' + '\n')
        set_m_to_d_pointer(self.file, 'ARG')

        self.file.write('@ARG' + '\n')
        self.file.write('D=M+1' + '\n')
        set_m_to_d(self.file, 'SP')

        restore_caller_address(self.file, '1', 'THAT')
        restore_caller_address(self.file, '2', 'THIS')
        restore_caller_address(self.file, '3', 'ARG')
        restore_caller_address(self.file, '4', 'LCL')

        set_a_to_m(self.file, 'retAddr')
        self.file.write('0;JMP' + '\n')
        self.file.write('\n')

    def close(self):
        self.file.close()
