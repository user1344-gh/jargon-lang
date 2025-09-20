import pos
import operators
import tokens

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
        return f"(IntNode({self.value}))"

class FloatNode:
    def __init__(self, value: str, pos_start: pos.Position, pos_end: pos.Position):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.value = value

    def __repr__(self):
        return f"(FloatNode({self.value}))"

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