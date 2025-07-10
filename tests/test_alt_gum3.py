import pytest

from conftest import TEST_DATA_DIR

from grammar_ast import GumSyntaxError, GumSemanticError


class TestGum3:
    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p01_nofunction.gum"], indirect=True)
    def test_p01_nofunction(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'This program is testing program with no function.'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p02_justfunction.gum"], indirect=True)
    def test_p02_justfunction(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'This string reside inside function test_f().'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p02_justfunctionAlt.gum"], indirect=True)
    def test_p02_justfunctionAlt(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'This string reside inside function test_f().'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p03_justreturn.gum"], indirect=True)
    def test_p03_justreturn(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (outs[0] == 'None')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p03_justreturnAlt.gum"], indirect=True)
    def test_p03_justreturnAlt(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (outs[0] == 'None')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p04_onearg.gum"], indirect=True)
    def test_p04_onearg(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (outs[0] == 'Echo Message - Able to print echo the message')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p05_scopeA.gum"], indirect=True)
    def test_p05_scopeA(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'Mars')
        assert (outs[1] == 'Earth')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p06_scopeB.gum"], indirect=True)
    def test_p06_scopeB(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'It should print 190')
        assert (outs[1] == '190')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p07_returnexpr.gum"], indirect=True)
    def test_p07_returnexpr(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'Test Multiply = 50')
        assert (outs[1] == '50')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p08_multifunction.gum"], indirect=True)
    def test_p08_multifunction(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'Should be 13000')
        assert (outs[1] == '13000')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p09_max.gum"], indirect=True)
    def test_p09_max(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'minimum is -3')
        assert (outs[1] == '-3')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p10_reverse.gum"], indirect=True)
    def test_p10_reverse(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 2)
        assert (outs[0] == 'Are you able to read this?')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p11_factorial.gum"], indirect=True)
    def test_p11_factorial(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'fact(9) = 362880')
        assert (outs[1] == '362880')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p12_gcd.gum"], indirect=True)
    def test_p12_gcd(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == 'gcd(749, 91) = 7')
        assert (outs[1] == '7')

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p13_bubblesort.gum"], indirect=True)
    def test_p13_bubblesort(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
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

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p17_bubblesort_1.gum"], indirect=True)
    def test_p17_bubblesort_1(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
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

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p16_listargs.gum"], indirect=True)
    def test_p16_listargs(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == "['testing', 'completed', ['for', 'cs4400']]")
        assert (outs[1] == "['testing', 'complete', ['for', 'cs4400']]")

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p19_assignlistarg.gum"], indirect=True)
    def test_p19_assignlistarg(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == "[11, 32, 13, 34, 75]")
        assert (outs[1] == "['s', (11, 21), 733]")

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p20_globallist.gum"], indirect=True)
    def test_p20_globallist(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert (len(outs) == 3)
        assert (outs[0] == "[11, 32, 13, 34, 75]")
        assert (outs[1] == "['s', (11, 21), 733]")

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p14_nested_err.gum"], indirect=True)
    def test_p14_nested_err(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSyntaxError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p15_usebeforedef_err.gum"], indirect=True)
    def test_p15_usebeforedef_err(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSemanticError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "funcs_2" / "p18_argmismatch_err.gum"], indirect=True)
    def test_p18_argmismatch_err(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSemanticError):
            parser.parse(lexer.tokenize(gum_file_data))
