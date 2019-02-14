import sys
import getopt
import os

from JackTokenizer import JackTokenizer
#from CompilationEngine import CompilationEngine

def main(argv):
    print(argv)

    opts, args = getopt.getopt(argv, "")

    if not args:
        print('JackAnalyzer.py <inputfile.jack> or <directory> containing jack files')
        sys.exit(2)
    else:
        filename = args[0]

        if os.path.isdir(filename):
            for f in os.listdir(filename):
                file_n, file_ext = os.path.splitext(f)
                if file_ext == '.jack':
                    tokenizer = JackTokenizer(
                        os.path.join(filename, f),
                        os.path.join(filename, file_n + 'T' + '.xml')
                    )
                    tokenizer.write_file()

        else:
            file_n, file_ext = os.path.splitext(filename)
            tokenizer = JackTokenizer(
                filename,
                os.path.join(filename, file_n + 'T' + '.xml')
                )
            tokenizer.test()

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])
