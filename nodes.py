import pos
import operators
import tokens
import types_

class Node:
    def __init__(self, pos_start: pos.Position, pos_end: pos.Position):
        self.pos_start = pos_start
        self.pos_end = pos_end
    def __repr__(self):
        return "(Node)"
    
class IntNode:
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class FloatNode:
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class StringNode:
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class BinaryOpNode:
    "Used for binary operations"
    def __init__(self, left: Node, operator: operators.Operator, right: Node):
        self.left = left
        self.operator = operator
        self.right = right
        self.pos_start = left.pos_start
        self.pos_end = right.pos_end
    
    def __repr__(self):
        return f"({self.left} {self.operator.name} {self.right})"

class UnaryOpNode:
    "Used for unary operations"
    def __init__(self, operator: operators.Operator, value: Node, pos_start: pos.Position):
        self.value = value
        self.operator = operator
        self.pos_start = pos_start
        self.pos_end = value.pos_end
    
    def __repr__(self):
        return f"({self.operator.name} {self.value})"

class CharNode:
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class VarNode:
    def __init__(self, token: tokens.Token):
        self.var_name = token.value
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
    def __repr__(self):
        return f"({self.var_name})"

class VarAssignNode:
    def __init__(self, var_name: str, value: Node, pos_start: pos.Position):
        self.var_name = var_name
        self.value = value
        self.pos_start = pos_start
        self.pos_end = value.pos_end
    def __repr__(self):
        return f"({self.var_name} = {self.value})"

class VarDeclareNode:
    def __init__(self, var_name: str, var_type: types_.Type, value: Node | None, pos_start: pos.Position, pos_end = pos.Position):
        self.var_name = var_name
        self.var_type = var_type
        self.value = value
        self.pos_start = pos_start
        self.pos_end = pos_end
    def __repr__(self):
        return f"(variable {self.var_name}: {self.var_type}" + (
            f" = {self.value})" if self.value else ")"
        )