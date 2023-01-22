#from lex import Lexer
#from parse import Parser
from ply_lex import *
from ply_parse import Parser
import sys

def main():
    print("Gãs Compiler")

    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file as argument.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
    
    if len(input) == 0:
        print('No text on the file')
    else:
        # Initialize the lexer and parser.
        #lexer = Lexer(input)
        lexer = lex.lex() # initialize ply lexer
        lexer.input(input+'\0') #pass de input to the lexer
        parser = Parser(lexer)

        parser.program() # Start the parser.
        print("Parsing completed.")


if __name__ == '__main__':
    main()