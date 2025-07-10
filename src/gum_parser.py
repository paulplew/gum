from grammar_ast import *
from gum_lexer import GumLexer

from sly import Parser

class GumParser(Parser):
    debugfile = "debug.out"
    tokens = GumLexer.tokens
    literals = GumLexer.literals
    symbol_table = [{}]

    precedence = (
        ("left", "FUNCTION"),
        ("left", "OR"),
        ("left", "AND"),
        ("left", "NOT"),
        ("left", "GT", "LT", "EQ", "NEQ", "GE", "LE"),
        ("right", "CONS"),
        ("left", "MEMBER"),
        ("left", "+", "-"),
        ("left", "*", "/", "INT_DIV", "MOD"),
        ("left", "EXPONENT"),
        ("left", "ASSIGN"),
    )

    ############################### TOP LEVEL ################################################

    @_("blocks")
    def prog(self, p):
        assert isinstance(p.blocks, BlocksNode)
        # create the initial symbol table
        GlobalTable()
        p.blocks.eval()

    ############################### blocks ###################################################
    @_("function_block blocks")
    def blocks(self, p):
        return BlocksNode(p.function_block, p.blocks)

    @_("function_block")
    def blocks(self, p):
        return BlocksNode(p.function_block, EmptyNode())

    @_("FUNCTION ID L_PAREN id_list R_PAREN ASSIGN block")
    def function_block(self, p):
        return FunctionNode(TerminalNode(p.ID), p.id_list, p.block)

    @_("block")
    def function_block(self, p):
        return SimpleNode(p.block)

    ############################### block ####################################################

    @_("L_CURLY statement_list R_CURLY")
    def block(self, p):
        return BlockNode(p.statement_list)

    ############################### statement_list ###########################################

    @_("statement_list statement")
    def statement_list(self, p):
        return StatementListNode(p[0], p[1])

    @_("statement")
    def statement_list(self, p):
        return SimpleNode(p[0])

    ############################### statement ################################################

    @_("function ';'")
    def statement(self, p):
        return SimpleNode(p[0])

    @_("return_statement ';'")
    def statement(self, p):
        return SimpleNode(p[0])

    @_("block_statement")
    def statement(self, p):
        return SimpleNode(p[0])

    @_("ID ASSIGN expr ';'")
    def statement(self, p):
        return AssignmentNode(TerminalNode(p.ID), p.expr)

    @_("ID L_BRAK expr R_BRAK ASSIGN expr ';'")
    def statement(self, p):
        return ListAssignmentNode(TerminalNode(p.ID), p.expr0, p.expr1)

    ############################### function #################################################

    @_("print_function")
    def function(self, p):
        return SimpleNode(p.print_function)

    ############################### block statements #########################################

    # these statements define a new scope but aren't the top level block
    @_("while_expr", "if_expr", "if_else_expr", "block")
    def block_statement(self, p):
        return SimpleNode(p[0])

    ############################### while loop ###############################################

    @_("WHILE L_PAREN expr R_PAREN block")
    def while_expr(self, p):
        return WhileLoop(p.expr, p.block)

    ############################### if/if else ###############################################

    @_("IF L_PAREN expr R_PAREN block")
    def if_expr(self, p):
        return IfNode(p.expr, p.block)

    @_("IF L_PAREN expr R_PAREN block ELSE block")
    def if_else_expr(self, p):
        return IfElseNode(p.expr, p.block0, p.block1)

    ############################### special functions ########################################

    @_("PRINT L_PAREN expr R_PAREN")
    def print_function(self, p):
        return PrintNode(p.expr)

    @_("RETURN expr")
    def return_statement(self, p):
        return ReturnNode(p.expr)

    ############################### END BLOCKS ###############################################

    ############################### START EXPR ###############################################
    @_("bool_expr")
    def expr(self, p):
        return SimpleNode(p.bool_expr)

    @_("bool_expr AND comp_expr", "bool_expr OR comp_expr")
    def bool_expr(self, p):
        return BoolNode(p.bool_expr, p.comp_expr, p[1])

    @_("comp_expr")
    def bool_expr(self, p):
        return SimpleNode(p[0])

    ############################### comparison expressions ###################################

    @_(
        "comp_expr GT comp_expr",
        "comp_expr LT comp_expr",
        "comp_expr EQ comp_expr",
        "comp_expr NEQ comp_expr",
        "comp_expr GE comp_expr",
        "comp_expr LE comp_expr",
    )
    def comp_expr(self, p):
        return ComparisonNode(p.comp_expr0, p.comp_expr1, p[1])

    @_("add_expr")
    def comp_expr(self, p):
        return SimpleNode(p.add_expr)

    ############################### addition expressions #####################################

    @_('add_expr "+" mul_expr', 'add_expr "-" mul_expr')
    def add_expr(self, p):
        return AddNode(p.add_expr, p.mul_expr, p[1])

    @_("mul_expr")
    def add_expr(self, p):
        return SimpleNode(p.mul_expr)

    ############################### multiplication expressions ###############################

    @_(
        'mul_expr "*" exp_expr',
        'mul_expr "/" exp_expr',
        "mul_expr INT_DIV exp_expr",
        "mul_expr MOD exp_expr",
    )
    def mul_expr(self, p):
        return MulExp(p.mul_expr, p.exp_expr, p[1])

    @_("exp_expr")
    def mul_expr(self, p):
        return SimpleNode(p.exp_expr)

    ############################### exponent expressions #####################################

    @_("factor EXPONENT exp_expr")
    def exp_expr(self, p):
        return ExpNode(p.factor, p.exp_expr)

    @_("factor")
    def exp_expr(self, p):
        return SimpleNode(p.factor)

    ############################### factor ###################################################

    @_("NOT factor")
    def factor(self, p):
        return NegationFactor(p.factor)

    @_("list_expr", "tuple_expr", "membership_check")
    def factor(self, p):
        return SimpleNode(p[0])

    ############################### list expressions #########################################

    @_("L_BRAK R_BRAK", "L_BRAK elements R_BRAK")
    def list_expr(self, p):
        if p[1] != "]":
            return SimpleNode(p.elements)
        else:
            return TerminalNode([])

    @_("factor L_BRAK expr R_BRAK")
    def list_expr(self, p):
        return IndexNode(p[0], p[2])

    @_("factor CONS factor")
    def list_expr(self, p):
        return ConsNode(p.factor0, p.factor1)

    ############################### membership check #########################################

    @_("factor MEMBER factor")
    def membership_check(self, p):
        return MemberNode(p[0], p[2])

    @_("atom")
    def membership_check(self, p):
        return SimpleNode(p[0])

    ############################### tuple expressions ########################################

    @_("L_PAREN elements COMMA R_PAREN")
    def tuple_expr(self, p):
        return TupleNode(p.elements)

    @_("'#' expr atom")
    def tuple_expr(self, p):
        return TupleIndexNode(p[2], p.expr)

    ############################### elements in lists and tuples #############################
    @_("id_list COMMA ID")
    def id_list(self, p):
        return IDListNode(p.id_list, p.ID)

    @_("ID", "")
    def id_list(self, p):
        try:
            return ElementNode(TerminalNode(p.ID))
        except AttributeError:
            return EmptyNode()

    @_("elements COMMA element")
    def elements(self, p):
        return ListNode(p.elements, p.element)

    @_("element", "")
    def elements(self, p):
        try: 
            return ElementNode(p.element)
        except AttributeError:
            return EmptyNode()

    ############################### elements in element list #################################

    @_("expr")
    def element(self, p):
        return SimpleNode(p.expr)

    ############################### the atomic type ##########################################

    @_("ID L_PAREN elements R_PAREN")
    def atom(self, p):
        return FunctionCallNode(p.ID, p.elements)


    @_("number", "STRING_LITERAL", "BOOLEAN")
    def atom(self, p):
        if isinstance(p[0], ASTNode):
            return SimpleNode(p[0])
        else:
            return TerminalNode(p[0])

    @_("ID")
    def atom(self, p):
        return IDNode(p.ID)

    @_("L_PAREN expr R_PAREN")
    def atom(self, p):
        return SimpleNode(p[1])

    @_("'-' INTEGER", "'-' FLOAT")
    def number(self, p):
        return NegativeNode(TerminalNode(p[1]))

    @_("INTEGER", "FLOAT")
    def number(self, p):
        return TerminalNode(p[0])

    ############################### END EXPRESSIONS ##########################################

    def error(self, p):
        raise GumSyntaxError(f"syntax error at {p}")
