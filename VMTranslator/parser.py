class Parser:
    count = 0

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
        Parser.count += 1

    def command_type(self):
        line = self.lines[self.index].split(' ')
        if line[0] == 'push':
            return 'C_PUSH'
        elif line[0] == 'pop':
            return 'C_POP'
        elif line[0] == 'label':
            return 'C_LABEL'
        elif line[0] == 'goto':
            return 'C_GOTO'
        elif line[0] == 'if-goto':
            return 'C_IF'
        elif line[0] == 'call':
            return 'C_CALL'
        elif line[0] == 'function':
            return 'C_FUNCTION'
        elif line[0] == 'return':
            return 'C_RETURN'
        elif line[0] in ['add', 'sub', 'eq', 'lt', 'gt', 'neg', 'not', 'and', 'or']:
            return 'C_ARITHMETIC'
        else:
            return None

    def arg1(self):
        line = self.lines[self.index].split(' ')

        command_type = self.command_type()

        if command_type in ['C_PUSH', 'C_POP', 'C_LABEL', 'C_GOTO', 'C_IF', 'C_FUNCTION', 'C_CALL']:
            return line[1]
        elif command_type == 'C_ARITHMETIC':
            return line[0]

    def arg2(self):
        line = self.lines[self.index].split(' ')

        command_type = self.command_type()

        if command_type in ['C_PUSH', 'C_POP', 'C_FUNCTION', 'C_CALL']:
            return line[2]
        # elif command_type == 'C_ARITHMETIC':
        else:
            return None
