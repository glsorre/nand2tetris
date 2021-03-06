import re

class JackTokenizer:

    keywords_code = {"class",
                     "constructor",
                     "function",
                     "method",
                     "field",
                     "static",
                     "var",
                     "int",
                     "char",
                     "boolean",
                     "void",
                     "true",
                     "false",
                     "null",
                     "this",
                     "let",
                     "do",
                     "if",
                     "else",
                     "while",
                     "return"}

    symbols_codes = {'{',
                     '}',
                     '(',
                     ')',
                     '[',
                     ']',
                     '.',
                     ',',
                     ';',
                     '+',
                     '-',
                     '*',
                     '/',
                     '&',
                     '<',
                     '>',
                     '=',
                     '~'}

    keywords_regex = r'(?!\w)|'.join(keywords_code) + '(?!\w)'
    symbols_regex = r'[' + re.escape('|'.join(symbols_codes)) + ']'
    integer_regex = r'\d+'
    string_regex = r'"[^"\n]*"'
    identifier_regex = r'[\w]+'

    word = re.compile(keywords_regex +
                      '|' +
                      symbols_regex +
                      '|' +
                      integer_regex +
                      '|' +
                      string_regex +
                      '|' +
                      identifier_regex)

    def __init__(self, file, file_to_write):
        self.file = open(file)
        self.lines = self.file.read()
        self.remove_commets()
        self.tokens = self.tokenize()
        self.tokens = self.replace_symbols()
        self.index = 0
        self.file_to_write = open(file_to_write, 'w')


    def remove_commets(self):
        current_index = 0
        filtered_text = ''
        end_index = 0
        while current_index < len(self.lines):
            current_char = self.lines[current_index]
            if current_char == "\"":
                end_index = self.lines.find("\"", current_index+1)
                filtered_text += self.lines[current_index:end_index+1]
                current_index = end_index + 1
            elif current_char == "/":
                if self.lines[current_index + 1] == "/":
                    end_index = self.lines.find("\n", current_index + 1)
                    current_index = end_index + 1
                    filtered_text += " "
                elif self.lines[current_index + 1] == "*":
                    end_index = self.lines.find("*/", current_index + 1)
                    current_index = end_index + 2
                    filtered_text += " "
                else:
                    filtered_text += self.lines[current_index]
                    current_index += 1
            else:
                filtered_text += self.lines[current_index]
                current_index += 1
        self.lines = filtered_text
        return

    def tokenize(self):
        return [self.token(word) for word in self.split(self.lines)]

    def token(self, word):
        if re.match(self.keywords_regex, word):
            return ("keyword", word)
        elif re.match(self.symbols_regex, word):
            return ("symbol", word)
        elif re.match(self.integer_regex, word):
            return ("integerConstant", word)
        elif re.match(self.string_regex, word):
            return ("stringConstant", word[1:-1])
        else: return ("identifier", word)

    def split(self, line):
        return self.word.findall(line)

    def replace_symbols(self):
        return [self.replace(pair) for pair in self.tokens]

    def replace(self, pair):
        token, value = pair
        if value == '<':
            return (token, '&lt;')
        elif value == '>':
            return (token, '&gt;')
        elif value == '"':
            return (token, '&quot;')
        elif value == '&':
            return (token, '&amp;')
        else:
            return (token, value)

    def has_more_tokens(self):
        try:
            if self.tokens[self.index]:
                return True
        except IndexError:
            return False

    def current_token(self):
        return self.tokens[self.index]

    def current_token_type(self):
        return self.current_token()[0]

    def current_token_value(self):
        return self.current_token()[1]

    def advance(self):
        self.index += 1

    def write_file(self):
        self.write_init()
        self.write_body()
        self.write_close()
        self.close()

    def write_init(self):
        self.file_to_write.write('<tokens>' + '\n')

    def write_body(self):
        while self.has_more_tokens():
            self.file_to_write.write('<' + self.current_token_type() + '>' + self.current_token_value() + '</' + self.current_token_type() + '>' + '\n')
            self.advance()

    def write_close(self):
        self.file_to_write.write('</tokens>' + '\n')

    def close(self):
        self.file_to_write.close()
