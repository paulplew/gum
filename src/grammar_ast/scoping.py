
from copy import deepcopy

from .errors import GumSemanticError

# singleton referenced from here https://python-patterns.guide/gang-of-four/singleton/
class GlobalTable:
    _instance = None
    previous_closures = []
    current_closure = None
    stack = [{}]

    class SymbolTableError(Exception):
        pass

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalTable, cls).__new__(cls)
        return cls._instance

    def pop(self):
        if len(self.stack) == 1:
            raise self.SymbolTableError("You cannot pop the last item from a symbol table")

        shadow_scope = self.stack.pop()
        for key in shadow_scope:
            if key in self.stack[-1]:
                self.stack[-1][key] = shadow_scope[key]

    def get(self, key):
        index = -1

        if self.current_closure is not None:
            try:
                return self.current_closure.table[key]
            except KeyError:
                pass

        while True:
            try:
                return self.stack[index][key]
            except KeyError:
                index -= 1
            except IndexError: 
                break
        
        raise GumSemanticError(f"ID: '{key}' is not defined in the current ")
    
    def set(self, key, value):
        if self.current_closure is None:
            self.stack[-1][key] = value
        else:
            self.current_closure.set(key, value)

    def shadow(self):
        self.stack.append(deepcopy(self.stack[-1]))

    def set_closure(self, closure):
        if self.current_closure is not None:
            self.previous_closures.append(self.current_closure)
        self.current_closure = closure

    def clear_closure(self):
        try:
            self.current_closure = self.previous_closures.pop()
        except IndexError:
            self.current_closure = None

    def copy_stack(self):
        copy = []
        for i in self.stack:
            copy.append(deepcopy(i))
        return copy


class Closure:
    return_value = None

    def __init__(self, name):
        self.table = {}
        self.table[name] = GlobalTable().get(name)

    def assign_return(self, val):
        self.return_value = val

    def get(self, key):
        try:
            return self.table[key]
        except KeyError:
            GlobalTable().get(key)

        raise GumSemanticError(f"ID: '{key}' is not defined in the current ")
    
    def set(self, key, value):
        self.table[key] = deepcopy(value)

