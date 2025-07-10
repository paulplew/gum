import pytest
import os

from conftest import TEST_DATA_DIR

from grammar_ast import GumSyntaxError, GumSemanticError

class TestGum3:
    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p01_nofunction.gum"], indirect=True)
    def test_p01_nofunction(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'This program has no function definitions.'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p02_justfunction.gum"], indirect=True)
    def test_p02_justfunction(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'Printed inside function f().'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p02_justfunctionAlt.gum"], indirect=True)
    def test_p02_justfunctionAlt(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'Printed inside function f().'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p03_justreturn.gum"], indirect=True)
    def test_p03_justreturn(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (outs[0] == 'None')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p03_justreturnAlt.gum"], indirect=True)
    def test_p03_justreturnAlt(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (outs[0] == 'None')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p04_onearg.gum"], indirect=True)
    def test_p04_onearg(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (outs[0] == 'The argument has been returned.')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p05_scopeA.gum"], indirect=True)
    def test_p05_scopeA(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'function')
        assert (outs[1] == 'main')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p06_scopeB.gum"], indirect=True)
    def test_p06_scopeB(self, capsys, lexer, parser, gum_file_data):
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'Should print 20')
        assert (outs[1] == '20')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p07_returnexpr.gum"], indirect=True)
    def test_p07_returnexpr(self, capsys, lexer, parser, gum_file_data):
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'Tester = 15')
        assert (outs[1] == '15')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p08_multifunction.gum"], indirect=True)
    def test_p08_multifunction(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'Should be 1115')
        assert (outs[1] == '1115')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p09_max.gum"], indirect=True)
    def test_p09_max(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'max is 330')
        assert (outs[1] == '330')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p10_reverse.gum"], indirect=True)
    def test_p10_reverse(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 2)
        assert (outs[0] == 'This string is forwards.')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p11_factorial.gum"], indirect=True)
    def test_p11_factorial(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'factorial(7) = 5040')
        assert (outs[1] == '5040')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p12_gcd.gum"], indirect=True)
    def test_p12_gcd(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'gcd(36, 16) = 4')
        assert (outs[1] == '4')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p13_bubblesort.gum"], indirect=True)
    def test_p13_bubblesort(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
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

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p17_bubblesort_1.gum"], indirect=True)
    def test_p17_bubblesort_1(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
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

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p16_listargs.gum"], indirect=True)
    def test_p16_listargs(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == "['hello', 'p', []]")
        assert (outs[1] == "['hello', 'cs4400', []]")

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p19_assignlistarg.gum"], indirect=True)
    def test_p19_assignlistarg(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == "[1, 2, 3]")
        assert (outs[1] == "['l', (1, 2)]")

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p20_globallist.gum"], indirect=True)
    def test_p20_globallist(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == "[1, 2, 3]")
        assert (outs[1] == "['l', (1, 2)]")

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p14_nested_err.gum"], indirect=True)
    def test_p14_nested_err(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSyntaxError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p15_usebeforedef_err.gum"], indirect=True)
    def test_p15_usebeforedef_err(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSemanticError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs" / "p18_argmismatch_err.gum"], indirect=True)
    def test_p18_argmismatch_err(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSemanticError):
            parser.parse(lexer.tokenize(gum_file_data))
