from pathlib import Path, PurePath

import pytest

from gum_lexer import GumLexer
from gum_parser import GumParser

TEST_DATA_DIR = Path(__file__).parent.resolve() / "test_data"

@pytest.fixture(name="lexer")
def lexer_fixture():
    return GumLexer()

@pytest.fixture(name="parser")
def parser_fixture():
    return GumParser()

@pytest.fixture(name="gum_file_data")
def gum_file_data_fixture(request):
    assert isinstance(request.param, PurePath)
    with open(request.param, "r") as gum_file:
        text = gum_file.read()
        yield text


