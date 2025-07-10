from gum_lexer import GumLexer
from gum_parser import GumParser
from grammar_ast import GumSemanticError, GumSyntaxError

if __name__ == "__main__":
    lexer = GumLexer()
    parser = GumParser()
    while True:
        try:
            text = input("gum > ")
        except EOFError:
            break
        if text:
            parser.start = "statement"
            try:
                print(parser.parse(lexer.tokenize(text)))
            except (GumSemanticError, GumSyntaxError) as e:
                print(str(e))
