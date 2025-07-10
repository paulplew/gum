class TestGumLexer:
    def test_tokenize_integer_1(self, lexer):
        text = "20304"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "INTEGER"
        assert data.value == 20304

    def test_tokenize_integer_2(self, lexer):
        text = "-9758"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "-"
        assert data.value == "-"

        data = list(lexer.tokenize(text))[1]
        assert data.type == "INTEGER"
        assert data.value == 9758

    def test_tokenize_float_1(self, lexer):
        text = "3.141592"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "FLOAT"
        assert data.value == 3.141592

    def test_tokenize_float_2(self, lexer):
        text = "-0.0007"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "-"
        assert data.value == "-"

        data = list(lexer.tokenize(text))[1]
        assert data.type == "FLOAT"
        assert data.value == 0.0007

    def test_tokenize_float_3(self, lexer):
        text = ".9277"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "FLOAT"
        assert data.value == 0.9277

    def test_tokenize_float_4(self, lexer):
        text = "-.9277"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "-"
        assert data.value == "-"

        data = list(lexer.tokenize(text))[1]
        assert data.type == "FLOAT"
        assert data.value == 0.9277

    def test_tokenize_float_and_integer_1(self, lexer):
        text = "-.9277 123456"
        data = list(lexer.tokenize(text))
        assert data[0].type == "-"
        assert data[0].value == "-"
        assert data[1].type == "FLOAT"
        assert data[1].value == 0.9277
        assert data[2].type == "INTEGER"
        assert data[2].value == 123456

    def test_tokenize_single_quote_string_uppercase(self, lexer):
        text = "'ZYXWVUTSRQPONMLKJIHGFEDCBA'"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip("'")

    def test_tokenize_single_quote_string_lowercase(self, lexer):
        text = "'zyxwvutsrqponmlkjihgfedcba'"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip("'")

    def test_tokenize_single_quote_string_1(self, lexer):
        text = "'abcdefABCDEF'"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip("'")

    def test_tokenize_single_quote_string_symbols(self, lexer):
        text = "'!@#$%^&*()'"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip("'")

    def test_tokenize_single_quote_hello_world(self, lexer):
        text = "'Hello, World!'"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip("'")

    def test_tokenize_empty_single_quote_string(self, lexer):
        text = "''"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip("'")

    def test_tokenize_double_quote_string_uppercase(self, lexer):
        text = '"ZYXWVUTSRQPONMLKJIHGFEDCBA"'
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip('"')

    def test_tokenize_double_quote_string_lowercase(self, lexer):
        text = '"zyxwvutsrqponmlkjihgfedcba"'
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip('"')

    def test_tokenize_double_quote_string_1(self, lexer):
        text = '"abcdefABCDEF"'
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip('"')

    def test_tokenize_double_quote_string_symbols(self, lexer):
        text = '"!@#$%^&*()"'
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip('"')

    def test_tokenize_double_quote_hello_world(self, lexer):
        text = '"Hello, World!"'
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip('"')

    def test_tokenize_empty_double_quote_string(self, lexer):
        text = '""'
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip('"')

    def test_tokenize_single_quote_numbers(self, lexer):
        text = "'0987654321'"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip("'")

    def test_tokenize_double_quote_numbers(self, lexer):
        text = '"0987654321"'
        data = list(lexer.tokenize(text))[0]
        assert data.type == "STRING_LITERAL"
        assert data.value == text.strip('"')

    def test_tokenize_empty_list(self, lexer):
        text = "[]"
        data = list(lexer.tokenize(text))
        assert data[0].type == "L_BRAK"
        assert data[0].value == "["
        assert data[1].type == "R_BRAK"
        assert data[1].value == "]"

    def test_tokenize_integer_list(self, lexer):
        text = "[4, 3, 3, 1]"
        data = list(lexer.tokenize(text))
        assert data[0].type == "L_BRAK"
        assert data[0].value == "["
        assert data[-1].type == "R_BRAK"
        assert data[-1].value == "]"

        assert data[1].type == "INTEGER"
        assert data[1].value == 4
        assert data[2].type == "COMMA"
        assert data[2].value == ","
        assert data[3].type == "INTEGER"
        assert data[3].value == 3
        assert data[4].type == "COMMA"
        assert data[4].value == ","
        assert data[5].type == "INTEGER"
        assert data[5].value == 3
        assert data[6].type == "COMMA"
        assert data[6].value == ","
        assert data[7].type == "INTEGER"
        assert data[7].value == 1

    def test_tokenize_empty_tuple(self, lexer):
        text = "()"
        data = list(lexer.tokenize(text))
        assert data[0].type == "L_PAREN"
        assert data[0].value == "("
        assert data[1].type == "R_PAREN"
        assert data[1].value == ")"

    def test_tokenize_integer_tuple(self, lexer):
        text = "(4, 3, 3, 1)"
        data = list(lexer.tokenize(text))
        assert data[0].type == "L_PAREN"
        assert data[0].value == "("
        assert data[-1].type == "R_PAREN"
        assert data[-1].value == ")"

        assert data[1].type == "INTEGER"
        assert data[1].value == 4
        assert data[2].type == "COMMA"
        assert data[2].value == ","
        assert data[3].type == "INTEGER"
        assert data[3].value == 3
        assert data[4].type == "COMMA"
        assert data[4].value == ","
        assert data[5].type == "INTEGER"
        assert data[5].value == 3
        assert data[6].type == "COMMA"
        assert data[6].value == ","
        assert data[7].type == "INTEGER"
        assert data[7].value == 1

    def test_tokenize_bool_true(self, lexer):
        text = "True"
        data = list(lexer.tokenize(text))
        assert data[0].type == "BOOLEAN"
        assert data[0].value is True

    def test_tokenize_bool_false(self, lexer):
        text = "False"
        data = list(lexer.tokenize(text))
        assert data[0].type == "BOOLEAN"
        assert data[0].value is False

    def test_tokenize_boolean_negation_not(self, lexer):
        text = "not False"
        data = list(lexer.tokenize(text))
        assert data[0].type == "NOT"
        assert data[0].value == "not"
        assert data[1].type == "BOOLEAN"
        assert data[1].value is False

    def test_tokenize_boolean_conjunction_and(self, lexer):
        text = "True andalso False"
        data = list(lexer.tokenize(text))
        assert data[0].type == "BOOLEAN"
        assert data[0].value is True
        assert data[1].type == "AND"
        assert data[1].value == "andalso"
        assert data[2].type == "BOOLEAN"
        assert data[2].value is False

    def test_tokenize_boolean_disjunction_or(self, lexer):
        text = "True orelse False"
        data = list(lexer.tokenize(text))
        assert data[0].type == "BOOLEAN"
        assert data[0].value is True
        assert data[1].type == "OR"
        assert data[1].value == "orelse"
        assert data[2].type == "BOOLEAN"
        assert data[2].value is False

    def test_tokenize_exponentaion(self, lexer):
        text = "8 ** 2"
        data = list(lexer.tokenize(text))
        assert data[0].type == "INTEGER"
        assert data[0].value == 8
        assert data[1].type == "EXPONENT"
        assert data[1].value == "**"
        assert data[2].type == "INTEGER"
        assert data[2].value == 2

    def test_tokenize_multiplication(self, lexer):
        text = "*"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "*"
        assert data.value == "*"

    def test_tokenize_division(self, lexer):
        text = "/"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "/"
        assert data.value == "/"

    def test_tokenize_integer_division(self, lexer):
        text = "div"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "INT_DIV"
        assert data.value == "div"

    def test_tokenize_addition(self, lexer):
        text = "+"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "+"
        assert data.value == "+"

    def test_tokenize_subtraction(self, lexer):
        text = "-"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "-"
        assert data.value == "-"

    def test_tokenize_membership(self, lexer):
        text = "in"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "MEMBER"
        assert data.value == "in"

    def test_tokenize_cons(self, lexer):
        text = "::"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "CONS"
        assert data.value == "::"

    def test_tokenize_less_than(self, lexer):
        text = "<"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "LT"
        assert data.value == "<"

    def test_tokenize_less_than_equal_to(self, lexer):
        text = "<="
        data = list(lexer.tokenize(text))[0]
        assert data.type == "LE"
        assert data.value == "<="

    def test_tokenize_equal_to(self, lexer):
        text = "=="
        data = list(lexer.tokenize(text))[0]
        assert data.type == "EQ"
        assert data.value == "=="

    def test_tokenize_not_equal_to(self, lexer):
        text = "<>"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "NEQ"
        assert data.value == "<>"

    def test_tokenize_greater_than_equal_to(self, lexer):
        text = ">="
        data = list(lexer.tokenize(text))[0]
        assert data.type == "GE"
        assert data.value == ">="

    def test_tokenize_greater_than(self, lexer):
        text = ">"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "GT"
        assert data.value == ">"

    def test_tokenize_modulo(self, lexer):
        text = "mod"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "MOD"
        assert data.value == "mod"

    def test_tokenize_index_tuple(self, lexer):
        text = "#"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "#"
        assert data.value == "#"

    def test_tokenize_r_paren(self, lexer):
        text = "("
        data = list(lexer.tokenize(text))[0]
        assert data.type == "L_PAREN"
        assert data.value == "("

    def test_tokenize_l_paren(self, lexer):
        text = ")"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "R_PAREN"
        assert data.value == ")"

    def test_tokenize_l_brak(self, lexer):
        text = "["
        data = list(lexer.tokenize(text))[0]
        assert data.type == "L_BRAK"
        assert data.value == "["

    def test_tokenize_r_brak(self, lexer):
        text = "]"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "R_BRAK"
        assert data.value == "]"


    def test_tokenize_comma(self, lexer):
        text = ","
        data = list(lexer.tokenize(text))[0]
        assert data.type == "COMMA"
        assert data.value == ","

    def test_tokenize_l_curly(self, lexer):
        text = "{"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "L_CURLY"
        assert data.value == "{"

    def test_tokenize_r_curly(self, lexer):
        text = "}"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "R_CURLY"
        assert data.value == "}"

    def test_tokenize_print(self, lexer):
        text = "print(1)"
        data = list(lexer.tokenize(text))[0]
        assert data.type == "PRINT"
