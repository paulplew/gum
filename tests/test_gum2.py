import pytest
import os

from conftest import TEST_DATA_DIR

from gum_lexer import GumLexer
from gum_parser import GumParser
from grammar_ast import GumSyntaxError, GumSemanticError

class TestGum2:
    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_1.gum"], indirect=True)
    def test_p1_1(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '37'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_2.gum"], indirect=True)
    def test_p1_2(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '98.6'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_3.gum"], indirect=True)
    def test_p1_3(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'Goodnight'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_4.gum"], indirect=True)
    def test_p1_4(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'Moon'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_5.gum"], indirect=True)
    def test_p1_5(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'three'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_6.gum"], indirect=True)
    def test_p1_6(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'iv'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_7.gum"], indirect=True)
    def test_p1_7(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '3'
        assert outs[1] == '5.0'
        assert outs[2] == 'eight'
        assert outs[3] == 'xiii'
        assert outs[4] == '4'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_7_1.gum"], indirect=True)
    def test_p1_7_1(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSemanticError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_8_1.gum"], indirect=True)
    def test_p1_8_1(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '27.0'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_8_2.gum"], indirect=True)
    def test_p1_8_2(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSemanticError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_9.gum"], indirect=True)
    def test_p1_9(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'x is True'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_10.gum"], indirect=True)
    def test_p1_10(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'Nay'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_11.gum"], indirect=True)
    def test_p1_11(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'Yea'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_12.gum"], indirect=True)
    def test_p1_12(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '122.0'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p1_13.gum"], indirect=True)
    def test_p1_13(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'GoodnightMoon'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p2.gum"], indirect=True)
    def test_p2(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSemanticError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p3.gum"], indirect=True)
    def test_p3(self, capsys, lexer, parser, gum_file_data):
        with pytest.raises(GumSyntaxError):
            parser.parse(lexer.tokenize(gum_file_data))

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p4.gum"], indirect=True)
    def test_p4(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'isPrime is true'
        assert outs[1] == '6'
        assert outs[2] == '6'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p5.gum"], indirect=True)
    def test_p5(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'isPrime is false'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p6.gum"], indirect=True)
    def test_p6(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '[3, 1, 2, 200]'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p7.gum"], indirect=True)
    def test_p7(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == 'This string is forwards.'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p8.gum"], indirect=True)
    def test_p8(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '934'

    @pytest.mark.parametrize("gum_file_data", [TEST_DATA_DIR / "p9.gum"], indirect=True)
    def test_p9(self, capsys, lexer, parser, gum_file_data):
        parser.parse(lexer.tokenize(gum_file_data))
        outs = capsys.readouterr().out.split('\n')
        assert outs[0] == '23'
