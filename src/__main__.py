from gum_lexer import GumLexer
from gum_parser import GumParser

if __name__ == "__main__":
    file = './data/funcs/p06_scopeB.gum'

    try:
        with open(file, 'r') as f:
            text = f.read()
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
    except FileNotFoundError:
        print('File not found : ' + file)
    except IOError:
        print('Error reading file : ' + file)
