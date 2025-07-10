import inspect
from debug import debuggable
from abc import abstractmethod, ABC

from .scoping import GlobalTable, Closure
from .errors import GumSyntaxError, GumSemanticError


def new_scope(func):
    def wrapper(*args, **kwargs):
        assert isinstance(
            args[0], ASTNode
        ), "Decorator new_scope must be used with ASTNode objects"

        symbol_table = GlobalTable()
        symbol_table.shadow()

        result = func(*args, **kwargs)
        symbol_table.pop()
        return result

    return wrapper


class ASTNode(ABC, object):
    @abstractmethod
    def eval(self):
        """
        Evaluate this node to some value
        """
        pass

    def call_chain(self):
        """
        This is helpful for debugging the abstract syntax tree it shows the nodes and
        their children as well as all terminal values. These can get pretty long tho.
        """
        items = {type(self).__name__: []}

        for key, member in inspect.getmembers(self):
            if key[0:1] == "_" or callable(member):
                continue

            try:
                items[type(self).__name__].append(getattr(self, key).call_chain())
            except AttributeError:
                items[type(self).__name__].append(getattr(self, key))

        return items


################################### HERE ARE SOME HELPFUL ABSTRACT NODES ################


class SimpleNode(ASTNode):
    """
    A simple node that evaluates with nothing else
    """

    def __init__(self, value: ASTNode):
        self.value = value

    # @debuggable
    def eval(self):
        return self.value.eval()


class TerminalNode(ASTNode):
    """
    This node only returns the value stored in it
    """

    def __init__(self, value):
        self.value = value

    ##@debuggable
    def eval(self):
        return self.value


class EmptyNode(ASTNode):
    """
    A Node that does nothing.

    This is essentially a placeholder node
    """

    def __init__(self):
        pass

    # @debuggable
    def eval(self):
        return


class OperationNode(ASTNode):
    def __init__(self, e1: ASTNode, e2: ASTNode, op):
        self.e1 = e1
        self.e2 = e2
        self.op = op


################################### BEGIN REAL NODES ###################################


class BlocksNode(ASTNode):
    def __init__(self, current_block, next_blocks):
        self.current_block = current_block
        self.next_blocks = next_blocks

    def eval(self):
        # there is no scope here because outer blocks don't share scope
        self.current_block.eval()
        self.next_blocks.eval()


class BlockNode(SimpleNode):
    # @debuggable
    @new_scope
    def eval(self):
        super().eval()

class FunctionNode(ASTNode):
    def __init__(self, name, elements, block):
        self.name = name
        self.elements = elements
        self.block = block

    def eval(self):
        name = self.name.eval()
        argument_names = self.elements.eval()

        symbol_table = GlobalTable()
        symbol_table.set(name, (argument_names, self.block))


class FunctionCallNode(ASTNode):
    def __init__(self, id, elements):
        self.id = id
        self.elements = elements
    
    def eval(self):
        elements = self.elements.eval()

        global_table = GlobalTable()
        closure = Closure(self.id)
        global_table.set_closure(closure)

        argument_names, block = global_table.get(self.id)

        if elements is None and argument_names is None:
            block.eval()
        elif elements is None:
            raise GumSemanticError("Missing elements")
        elif argument_names is None:
            raise GumSemanticError("Too many arguments")
        else:
            if len(argument_names) != len(elements):
                raise GumSemanticError("Argument Mismatching")

            for name, element in zip(argument_names, elements):
                closure.set(name, element)


            block.value.eval()

        global_table.clear_closure()
        return closure.return_value


class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

    # @debuggable
    def eval(self):
        expr_value = self.expr.eval()
        print(expr_value)
        return


class WhileLoop(ASTNode):
    def __init__(self, expr, lines):
        self.expr = expr
        self.lines = lines

    # @debuggable
    def eval(self):
        while self.expr.eval():
            self.lines.eval()


class IfNode(ASTNode):
    def __init__(self, expr, lines):
        self.expr = expr
        self.lines = lines

    # @debuggable
    def eval(self):
        if self.expr.eval():
            self.lines.eval()


class IfElseNode(ASTNode):
    def __init__(self, expr, if_block, else_block):
        self.expr = expr
        self.if_block = if_block
        self.else_block = else_block

    # @debuggable
    def eval(self):
        if self.expr.eval():
            self.if_block.eval()
        else:
            self.else_block.eval()


class NegationFactor(ASTNode):
    def __init__(self, value: ASTNode):
        self.value = value

    # @debuggable
    def eval(self):
        evaluated = self.value.eval()

        if not isinstance(evaluated, bool):
            raise GumSemanticError(f"Cannot negate with type {type(evaluated)}")

        return not evaluated


class NegativeNode(ASTNode):
    def __init__(self, value: ASTNode):
        self.value = value

    # @debuggable
    def eval(self):
        evaluated = self.value.eval()

        if not isinstance(evaluated, (float, int)):
            raise GumSemanticError(f"Cannot negate type {type(evaluated)}")

        return -1 * evaluated


class AddNode(OperationNode):
    def __init__(self, e1, e2, op):
        super().__init__(e1, e2, op)

    # @debuggable
    def eval(self):
        # it really shouldn't be anything else unless theres a deeper issue
        assert self.op in ["+", "-"]

        e1_evaluated = self.e1.eval()
        e2_evaluated = self.e2.eval()

        are_strings = [isinstance(x, str) for x in [e1_evaluated, e2_evaluated]]
        if self.op == "+":
            if any(are_strings) and not all(are_strings):
                raise GumSemanticError(
                    f"Unsupported Operand type: {self.op} for "
                    f"{type(e1_evaluated)} and {type(e2_evaluated)}"
                )
            return e1_evaluated + e2_evaluated
        else:
            if not isinstance(e1_evaluated, (int, float)) or not isinstance(
                e2_evaluated, (int, float)
            ):
                raise GumSemanticError(
                    f"Operator '-' not supported between types '{type(e1_evaluated)}' and '{type(e2_evaluated)}'"
                )
            return e1_evaluated - e2_evaluated


class MulExp(OperationNode):
    def __init__(self, e1, e2, op):
        assert op in ["*", "/", "div", "mod"]
        super().__init__(e1, e2, op)

    # @debuggable
    def eval(self):
        e1_evaluated = self.e1.eval()
        e2_evaluated = self.e2.eval()

        if not any(
            [
                isinstance(x, float) or isinstance(x, int)
                for x in [e1_evaluated, e2_evaluated]
            ]
        ):
            raise GumSemanticError(
                f"Operator {self.op} does not support operation on one "
                f"of {type(e1_evaluated)}, {type(e2_evaluated)}"
            )
        if self.op == "*":
            return e1_evaluated * e2_evaluated
        elif self.op == "mod":
            return e1_evaluated % e2_evaluated

        if e2_evaluated == 0:
            raise GumSemanticError("Divide by 0 Error")

        if self.op == "/":
            return e1_evaluated / e2_evaluated
        elif self.op == "div":
            return e1_evaluated // e2_evaluated
        else:
            assert False, "Operator Invalid"


class ExpNode(OperationNode):
    def __init__(self, e1, e2):
        super().__init__(e1, e2, "**")

    # @debuggable
    def eval(self):
        e1_evaluated = self.e1.eval()
        e2_evaluated = self.e2.eval()

        if not any(
            [
                isinstance(x, float) or isinstance(x, int)
                for x in [e1_evaluated, e2_evaluated]
            ]
        ):
            raise GumSemanticError(
                f"Operator {self.op} does not support operation on one "
                f"of {type(e1_evaluated)}, {type(e2_evaluated)}"
            )

        return e1_evaluated**e2_evaluated


class BoolNode(OperationNode):
    def __init__(self, e1, e2, op):
        assert op in ["andalso", "orelse"]
        super().__init__(e1, e2, op)

    # @debuggable
    def eval(self):
        e1_evaluated = self.e1.eval()
        e2_evaluated = self.e2.eval()

        if not all([isinstance(x, bool) for x in [e1_evaluated, e2_evaluated]]):
            raise GumSemanticError(
                f"Operator {self.op} does not support operation on one "
                f"of {type(e1_evaluated)}, {type(e2_evaluated)}"
            )

        if self.op == "andalso":
            return e1_evaluated and e2_evaluated
        else:
            return e1_evaluated or e2_evaluated


class ComparisonNode(OperationNode):
    def __init__(self, e1, e2, op):
        assert op in [">", "<", "==", "<>", ">=", "<="]
        super().__init__(e1, e2, op)

    # @debuggable
    def eval(self):
        e1_evaluated = self.e1.eval()
        e2_evaluated = self.e2.eval()

        are_str_or_int = [
            isinstance(x, (str, int, float)) for x in [e1_evaluated, e2_evaluated]
        ]
        if not all(are_str_or_int):
            raise GumSemanticError(
                f"Operator {self.op} does not support operation on one "
                f"of {type(e1_evaluated)}, {type(e2_evaluated)}"
            )

        if self.op == ">":
            return e1_evaluated > e2_evaluated
        elif self.op == "<":
            return e1_evaluated < e2_evaluated
        elif self.op == "==":
            return e1_evaluated == e2_evaluated
        elif self.op == "<>":
            return e1_evaluated != e2_evaluated
        elif self.op == ">=":
            return e1_evaluated >= e2_evaluated
        elif self.op == "<=":
            return e1_evaluated <= e2_evaluated


class IDListNode(ASTNode):
    def __init__(self, first_element, last_ID):
        self.first_element = first_element
        self.remaining_elements = last_ID

    # @debuggable
    def eval(self):
        first_element_evaluated = self.first_element.eval()
        remaining_evaluated = [self.remaining_elements]

        if remaining_evaluated is not None:
            first_element_evaluated.extend(remaining_evaluated)
            return first_element_evaluated
        else:
            return [first_element_evaluated]

class ListNode(ASTNode):
    def __init__(self, first_element, remaining_elements):
        self.first_element = first_element
        self.remaining_elements = remaining_elements

    # @debuggable
    def eval(self):
        first_element_evaluated = self.first_element.eval()
        remaining_evaluated = [self.remaining_elements.eval()]

        if remaining_evaluated is not None:
            first_element_evaluated.extend(remaining_evaluated)
            return first_element_evaluated
        else:
            return [first_element_evaluated]


class TupleNode(ASTNode):
    def __init__(self, list_expr: ListNode):
        assert isinstance(list_expr, ListNode) or isinstance(list_expr, ElementNode)
        self.list_expr = list_expr

    # @debuggable
    def eval(self):
        list_expr_evaluated = self.list_expr.eval()
        if isinstance(list_expr_evaluated, list):
            return tuple(list_expr_evaluated)
        else:
            return list_expr_evaluated


class IndexNode(ASTNode):
    def __init__(self, list, index):
        self.list = list
        self.index = index

    # @debuggable
    def eval(self):
        list_evaluated = self.list.eval()
        index_evaluated = self.index.eval()

        if not isinstance(index_evaluated, int):
            raise GumSemanticError(
                f"Indices must be an int not {type(index_evaluated)}"
            )

        # isinstance with bool and int returns true
        if str(index_evaluated) == "True" or str(index_evaluated) == "False":
            raise GumSemanticError(
                f"Indices must be an int not {type(index_evaluated)}"
            )

        try:
            return list_evaluated[index_evaluated]
        except IndexError:
            raise GumSemanticError(f"Index {index_evaluated} out of bounds")


class TupleIndexNode(IndexNode):
    def __init__(self, tuple, index):
        self.tuple = tuple
        self.index = index

    # @debuggable
    def eval(self):
        tuple_evaluated = self.tuple.eval()
        index_evaluated = self.index.eval() - 1

        if not isinstance(index_evaluated, int):
            raise GumSemanticError(
                f"Indices must be an int not {type(index_evaluated)}"
            )

        try:
            return tuple_evaluated[index_evaluated]
        except IndexError:
            raise GumSemanticError(f"Index {index_evaluated} out of bounds")


class ElementNode(SimpleNode):
    def __init__(self, element):
        super().__init__(element)

    def eval(self):
        return [super().eval()]


class ConsNode(ASTNode):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2

    # @debuggable
    def eval(self):
        e1_evaluated = self.e1.eval()
        e2_evaluated = self.e2.eval()

        e2_evaluated.insert(0, e1_evaluated)
        return e2_evaluated


class MemberNode(ASTNode):
    def __init__(self, value, iterable):
        self.value = value
        self.iterable = iterable

    # @debuggable
    def eval(self):
        value_evaluated = self.value.eval()
        iterable_evaluated = self.iterable.eval()

        if not isinstance(iterable_evaluated, (str, list)):
            raise GumSemanticError(
                f"Cannot check membership for type {type(iterable_evaluated)}"
            )

        return value_evaluated in iterable_evaluated


### NODES THAT USE THE SYMBOL TABLE #####################################################
class IDNode(TerminalNode):
    def __init__(self, ID):
        super().__init__(ID)

    def eval(self):
        id = super().eval()
        symbol_table = GlobalTable()
        return symbol_table.get(id)


class AssignmentNode(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    # @debuggable
    def eval(self):
        name_evaluated = self.name.eval()
        value_evaluated = self.value.eval()
        if not isinstance(name_evaluated, str):
            raise GumSyntaxError(f"Cannot assign a value to literal '{name_evaluated}'")

        symbol_table = GlobalTable()
        symbol_table.set(name_evaluated, value_evaluated)

        # return the value, which will do nothing unless something needs to be done with it
        return value_evaluated


class StatementListNode(ASTNode):
    def __init__(self, previous_statements, statement):
        self.previous_statements = previous_statements
        self.statement = statement

    def eval(self):
        # evaluate all previous statments then this statement
        self.previous_statements.eval()
        self.statement.eval()


class ListAssignmentNode(ASTNode):
    def __init__(self, id, index, value):
        self.id = id
        self.index = index
        self.value = value

    # @debuggable
    def eval(self):
        id_evaluated = self.id.eval()
        index_evaluated = self.index.eval()
        value_evaluated = self.value.eval()

        symbol_table = GlobalTable()
        the_list = symbol_table.get(id_evaluated)
        assert isinstance(the_list, list)

        try:
            the_list[index_evaluated] = value_evaluated
        except IndexError:
            raise GumSemanticError("Index out of bounds")

        # return the value, which will do nothing unless something needs to be done with it
        return value_evaluated


class ReturnNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def eval(self):
        table = GlobalTable()
        current_closure = table.current_closure

        if current_closure is None:
            raise GumSemanticError("Return statement used out of the appropriate context")
        else:
            current_closure.assign_return(self.value.eval())

