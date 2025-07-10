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


class TestGum3:
    def test_p01_nofunction(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p01_nofunction.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'This program has no function definitions.'
        else:
            raise GumTestErr

    def test_p02_justfunction(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p02_justfunction.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'Printed inside function f().'
        else:
            raise GumTestErr

    def test_p02_justfunctionAlt(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p02_justfunctionAlt.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'Printed inside function f().'
        else:
            raise GumTestErr

    def test_p03_justreturn(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p03_justreturn.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (outs[0] == 'None')
        else:
            raise GumTestErr

    def test_p03_justreturnAlt(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p03_justreturnAlt.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (outs[0] == 'None')
        else:
            raise GumTestErr

    def test_p04_onearg(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p04_onearg.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (outs[0] == 'The argument has been returned.')
        else:
            raise GumTestErr

    def test_p05_scopeA(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p05_scopeA.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'function')
            assert (outs[1] == 'main')
        else:
            raise GumTestErr

    def test_p06_scopeB(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p06_scopeB.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'Should print 20')
            assert (outs[1] == '20')
        else:
            raise GumTestErr

    def test_p07_returnexpr(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p07_returnexpr.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'Tester = 15')
            assert (outs[1] == '15')
        else:
            raise GumTestErr

    def test_p08_multifunction(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p08_multifunction.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'Should be 1115')
            assert (outs[1] == '1115')
        else:
            raise GumTestErr

    def test_p09_max(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p09_max.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'max is 330')
            assert (outs[1] == '330')
        else:
            raise GumTestErr

    def test_p10_reverse(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p10_reverse.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 2)
            assert (outs[0] == 'This string is forwards.')
        else:
            raise GumTestErr

    def test_p11_factorial(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p11_factorial.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'factorial(7) = 5040')
            assert (outs[1] == '5040')
        else:
            raise GumTestErr

    def test_p12_gcd(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p12_gcd.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'gcd(36, 16) = 4')
            assert (outs[1] == '4')
        else:
            raise GumTestErr

    def test_p13_bubblesort(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p13_bubblesort.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 10)
            assert (outs[0] == 'Sorted list is: [7, 17, 32, 44, 56, 89, 122, 330]')
            assert (outs[1] == '7')
            assert (outs[2] == '17')
            assert (outs[3] == '32')
            assert (outs[4] == '44')
            assert (outs[5] == '56')
            assert (outs[6] == '89')
            assert (outs[7] == '122')
            assert (outs[8] == '330')
        else:
            raise GumTestErr

    def test_p17_bubblesort_1(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p17_bubblesort_1.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 10)
            assert (outs[0] == '7')
            assert (outs[1] == '17')
            assert (outs[2] == '32')
            assert (outs[3] == '44')
            assert (outs[4] == '56')
            assert (outs[5] == '89')
            assert (outs[6] == '122')
            assert (outs[7] == '330')
            assert (outs[8] == '[122, 44, 32, 7, 89, 56, 330, 17]')
        else:
            raise GumTestErr

    def test_p16_listargs(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p16_listargs.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == "['hello', 'p', []]")
            assert (outs[1] == "['hello', 'cs4400', []]")
        else:
            raise GumTestErr

    def test_p19_assignlistarg(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p19_assignlistarg.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == "[1, 2, 3]")
            assert (outs[1] == "['l', (1, 2)]")
        else:
            raise GumTestErr

    def test_p20_globallist(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p20_globallist.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == "[1, 2, 3]")
            assert (outs[1] == "['l', (1, 2)]")
        else:
            raise GumTestErr

    def test_p14_nested_err(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p14_nested_err.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSyntaxError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p15_usebeforedef_err(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p15_usebeforedef_err.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSemanticError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p18_argmismatch_err(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs', 'p18_argmismatch_err.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSemanticError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr
