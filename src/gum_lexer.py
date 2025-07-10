from grammar_ast import *

from sly import Lexer
from sly.lex import Token

class GumLexer(Lexer):
    """
    This is a parser for the Gum Language. The syntax is complex and can be viewed and
    understood in the README.

    Implementation Note: The more complex rules are defined at the top of this Lexer so
    they take precedence over some of the simpler rules.
    """

    tokens = {
        "AND",
        "ASSIGN",
        "BOOLEAN",
        "COMMA",
        "CONS",
        "ELSE",
        "EQ",
        "EXPONENT",
        "FLOAT",
        "FUNCTION",
        "GE",
        "GT",
        "ID",
        "IF",
        "INTEGER",
        "INT_DIV",
        "LE",
        "LT",
        "L_BRAK",
        "L_CURLY",
        "L_PAREN",
        "MEMBER",
        "MOD",
        "NEQ",
        "NOT",
        "OR",
        "PRINT",
        "RETURN",
        "R_BRAK",
        "R_CURLY",
        "R_PAREN",
        "STRING_LITERAL",
        "WHILE",
    }

    ignore_whitespace = r"\s+"
    ignore_tabs = r"\t+"

    @_(r"\d+\.\d+", r"\d*\.\d+", r"\d+\.\d*")
    def FLOAT(self, t: Token) -> Token:
        t.value = float(t.value)
        return t

    @_(r"\d+")
    def INTEGER(self, t: Token) -> Token:
        t.value = int(t.value)
        return t

    @_(r"True", r"False")
    def BOOLEAN(self, t: Token) -> Token:
        if t.value == "False":
            t.value = False
        elif t.value == "True":
            t.value = True
        return t

    # NOTE: -----------------------------------------------------------------------------
    # I chose to match these as STRING_LITERAL to make the parser simpler for strings
    # if this causes issues in the future something akin to the following can be
    # implemented:
    #
    #    STRING -> QUOTE CHAR* QUOTE
    #    CHAR -> ID
    #    QUOTE -> " | '
    # ------------------------------------------------------------------------------------
    @_(r'"[^"]*"', r"'[^']*'")
    def STRING_LITERAL(self, t: Token) -> Token:
        # strip outer quotes
        t.value = t.value[1:][:-1]
        return t

    @_(r"\n+")
    def newline(self, t):
        self.lineno += t.value.count("\n")

    literals = {"*", "+", "-", "/", "#", ";"}

    ID = r"[a-zA-Z_][a-zA-Z0-9_]*"

    ID["not"] = "NOT"
    ID["andalso"] = "AND"
    ID["orelse"] = "OR"
    ID["div"] = "INT_DIV"
    ID["in"] = "MEMBER"
    ID["mod"] = "MOD"
    ID["print"] = "PRINT"
    ID["while"] = "WHILE"
    ID["if"] = "IF"
    ID["else"] = "ELSE"
    ID["fun"] = "FUNCTION"
    ID["return"] = "RETURN"

    COMMA = r","
    CONS = r"::"
    EQ = r"=="
    ASSIGN = r"="
    EXPONENT = r"\*{2}"
    NEQ = r"<>"
    GE = r">="
    GT = r">"
    LE = r"<="
    LT = r"<"

    L_BRAK = r"\["
    R_BRAK = r"\]"

    L_PAREN = r"\("
    R_PAREN = r"\)"

    L_CURLY = r"\{"
    R_CURLY = r"\}"

    def error(self, t):
        raise GumSyntaxError(
            f"Illegal character {t.value[0]} at line no = {self.lineno}"
        )

