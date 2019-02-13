import sys
import getopt

from JackTokenizer import JackTokenizer

def main(argv):
    print(argv)

    opts, args = getopt.getopt(argv, "")

    if not args:
        print('JackAnalyzer.py <inputfile.jack> or <directory> containing jack files')
        sys.exit(2)
    else:
        filename = args[0]
        print(filename)

        tokenizer = JackTokenizer(filename)
        tokenizer.test()

        #init_output_file(filename, code_writer)
        #build_output_file(filename, code_writer)

        #close_file(code_writer)


if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])
