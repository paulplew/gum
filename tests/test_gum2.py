import pytest
import os

from gum_lexer import GumLexer
from gum_parser import GumParser
from grammar_ast import GumSyntaxError, GumSemanticError


class GumTestErr(Exception):
    pass


def readProg(file):
    try:
        with open(file, 'r') as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print('File not found : ' + file)
    except IOError:
        print('Error reading file : ' + file)


class TestGum2:
    def test_p1_1(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_1.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '37'
        else:
            raise GumTestErr

    def test_p1_2(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_2.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '98.6'
        else:
            raise GumTestErr

    def test_p1_3(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_3.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'Goodnight'
        else:
            raise GumTestErr

    def test_p1_4(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_4.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'Moon'
        else:
            raise GumTestErr

    def test_p1_5(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_5.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'three'
        else:
            raise GumTestErr

    def test_p1_6(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_6.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'iv'
        else:
            raise GumTestErr

    def test_p1_7(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_7.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '3'
            assert outs[1] == '5.0'
            assert outs[2] == 'eight'
            assert outs[3] == 'xiii'
            assert outs[4] == '4'
        else:
            raise GumTestErr

    def test_p1_7_1(self, capsys):
        file = file = os.path.join(os.getcwd(), 'data', 'p1_7_1.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSemanticError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p1_8_1(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_8_1.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '27.0'
        else:
            raise GumTestErr

    def test_p1_8_2(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_8_2.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSemanticError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p1_9(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_9.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'x is True'
        else:
            raise GumTestErr

    def test_p1_10(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_10.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'Nay'
        else:
            raise GumTestErr

    def test_p1_11(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_11.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'Yea'
        else:
            raise GumTestErr

    def test_p1_12(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_12.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '122.0'
        else:
            raise GumTestErr

    def test_p1_13(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p1_13.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'GoodnightMoon'
        else:
            raise GumTestErr

    def test_p2(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p2.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSemanticError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p3(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p3.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSyntaxError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p4(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p4.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'isPrime is true'
            assert outs[1] == '6'
            assert outs[2] == '6'
        else:
            raise GumTestErr

    def test_p5(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p5.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'isPrime is false'
        else:
            raise GumTestErr

    def test_p6(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p6.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '[3, 1, 2, 200]'
        else:
            raise GumTestErr

    def test_p7(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p7.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'This string is forwards.'
        else:
            raise GumTestErr

    def test_p8(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p8.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '934'
        else:
            raise GumTestErr

    def test_p9(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'p9.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == '23'
        else:
            raise GumTestErr
