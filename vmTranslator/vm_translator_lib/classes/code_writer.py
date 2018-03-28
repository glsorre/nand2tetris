from vm_translator_lib.classes.code_writer_helpers import *

class CodeWiter:
  def __init__(self, filename, partialname):
    self.lines = []
    self.file = open(filename, 'w')
    self.TMP = 5
    self.static_name = partialname.split('/')[-2]
    print('STATTTTTTTTTTTTTTTTTIC')
    print(self.static_name) 
  
  def write_arithmetic(self, action, parser_index):
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

    elif action == 'or':
      or_to_d(self.file)
      sp_minus_two(self.file)
      set_m_to_d_pointer(self.file, 'SP')
      sp_plus(self.file)

    elif action == 'and':
      and_to_d(self.file)
      sp_minus_two(self.file)
      set_m_to_d_pointer(self.file, 'SP')
      sp_plus(self.file)
    
    elif action == 'neg':
      neg_to_d(self.file)
      sp_minus(self.file)
      set_m_to_d_pointer(self.file, 'SP')
      sp_plus(self.file)

    elif action == 'not':
      not_to_d(self.file)
      sp_minus(self.file)
      set_m_to_d_pointer(self.file, 'SP')
      sp_plus(self.file)

    elif action == 'eq':
      sub_to_d(self.file)
      sp_minus_two(self.file)
      operator_to_d(self.file, parser_index, 'EQ')

    elif action == 'lt':
      sub_to_d(self.file)
      sp_minus_two(self.file)
      operator_to_d(self.file, parser_index, 'LT')

    elif action == 'gt':
      sub_to_d(self.file)
      sp_minus_two(self.file)
      operator_to_d(self.file, parser_index, 'GT')

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
        address = self.static_name + '.' + index
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
        address = self.static_name + '.' + index
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