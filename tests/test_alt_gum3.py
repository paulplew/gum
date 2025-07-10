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
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p01_nofunction.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'This program is testing program with no function.'
        else:
            raise GumTestErr

    def test_p02_justfunction(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p02_justfunction.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'This string reside inside function test_f().'
        else:
            raise GumTestErr

    def test_p02_justfunctionAlt(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p02_justfunctionAlt.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert outs[0] == 'This string reside inside function test_f().'
        else:
            raise GumTestErr

    def test_p03_justreturn(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p03_justreturn.gum')
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
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p03_justreturnAlt.gum')
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
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p04_onearg.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (outs[0] == 'Echo Message - Able to print echo the message')
        else:
            raise GumTestErr

    def test_p05_scopeA(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p05_scopeA.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'Mars')
            assert (outs[1] == 'Earth')
        else:
            raise GumTestErr

    def test_p06_scopeB(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p06_scopeB.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'It should print 190')
            assert (outs[1] == '190')
        else:
            raise GumTestErr

    def test_p07_returnexpr(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p07_returnexpr.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'Test Multiply = 50')
            assert (outs[1] == '50')
        else:
            raise GumTestErr

    def test_p08_multifunction(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p08_multifunction.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'Should be 13000')
            assert (outs[1] == '13000')
        else:
            raise GumTestErr

    def test_p09_max(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p09_max.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'minimum is -3')
            assert (outs[1] == '-3')
        else:
            raise GumTestErr

    def test_p10_reverse(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p10_reverse.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 2)
            assert (outs[0] == 'Are you able to read this?')
        else:
            raise GumTestErr

    def test_p11_factorial(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p11_factorial.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'fact(9) = 362880')
            assert (outs[1] == '362880')
        else:
            raise GumTestErr

    def test_p12_gcd(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p12_gcd.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == 'gcd(749, 91) = 7')
            assert (outs[1] == '7')
        else:
            raise GumTestErr

    def test_p13_bubblesort(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p13_bubblesort.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 12)
            assert (outs[0] == 'Sorted list is: [-96,-34,0,4,43,123,142,222,1000,1001]')
            assert (outs[1] == '-96')
            assert (outs[2] == '-34')
            assert (outs[3] == '0')
            assert (outs[4] == '4')
            assert (outs[5] == '43')
            assert (outs[6] == '123')
            assert (outs[7] == '142')
            assert (outs[8] == '222')
            assert (outs[9] == '1000')
            assert (outs[10] == '1001')
        else:
            raise GumTestErr

    def test_p17_bubblesort_1(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p17_bubblesort_1.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 12)
            assert (outs[0] == '-96')
            assert (outs[1] == '-34')
            assert (outs[2] == '0')
            assert (outs[3] == '4')
            assert (outs[4] == '43')
            assert (outs[5] == '123')
            assert (outs[6] == '142')
            assert (outs[7] == '222')
            assert (outs[8] == '1000')
            assert (outs[9] == '1001')
            assert (outs[10] == '[-34, 0, 123, 43, 222, 142, 4, -96, 1000, 1001]')
        else:
            raise GumTestErr

    def test_p16_listargs(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p16_listargs.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == "['testing', 'completed', ['for', 'cs4400']]")
            assert (outs[1] == "['testing', 'complete', ['for', 'cs4400']]")
        else:
            raise GumTestErr

    def test_p19_assignlistarg(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p19_assignlistarg.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == "[11, 32, 13, 34, 75]")
            assert (outs[1] == "['s', (11, 21), 733]")
        else:
            raise GumTestErr

    def test_p20_globallist(self, capsys):
        file = './data/funcs_sagar/p20_globallist.gum'
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            parser.parse(lexer.tokenize(text))
            outs = capsys.readouterr().out.split('\n')
            assert (len(outs) == 3)
            assert (outs[0] == "[11, 32, 13, 34, 75]")
            assert (outs[1] == "['s', (11, 21), 733]")
        else:
            raise GumTestErr

    def test_p14_nested_err(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p14_nested_err.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSyntaxError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p15_usebeforedef_err(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p15_usebeforedef_err.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSemanticError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr

    def test_p18_argmismatch_err(self, capsys):
        file = os.path.join(os.getcwd(), 'data', 'funcs_sagar', 'p18_argmismatch_err.gum')
        text = readProg(file)
        if text:
            lexer = GumLexer()
            parser = GumParser()
            with pytest.raises(GumSemanticError):
                parser.parse(lexer.tokenize(text))
        else:
            raise GumTestErr
