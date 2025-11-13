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
    
class IntNode(Node):
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class FloatNode(Node):
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class StringNode(Node):
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class BinaryOpNode(Node):
    "Used for binary operations"
    def __init__(self, left: Node, operator: operators.Operator, right: Node):
        self.left = left
        self.operator = operator
        self.right = right
        self.pos_start = left.pos_start
        self.pos_end = right.pos_end
    
    def __repr__(self):
        return f"({self.left} {self.operator.name} {self.right})"

class UnaryOpNode(Node):
    "Used for unary operations"
    def __init__(self, operator: operators.Operator, value: Node, pos_start: pos.Position):
        self.value = value
        self.operator = operator
        self.pos_start = pos_start
        self.pos_end = value.pos_end
    
    def __repr__(self):
        return f"({self.operator.name} {self.value})"

class CharNode(Node):
    def __init__(self, token: tokens.Token):
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
        self.value = token.value

    def __repr__(self):
        return f"({type(self).__name__}({self.value}))"

class VarNode(Node):
    def __init__(self, token: tokens.Token):
        self.var_name = token.value
        self.pos_start = token.pos_start
        self.pos_end = token.pos_end
    def __repr__(self):
        return f"({self.var_name})"

class VarAssignNode(Node):
    def __init__(self, var_name: str, value: Node, pos_start: pos.Position):
        self.var_name = var_name
        self.value = value
        self.pos_start = pos_start
        self.pos_end = value.pos_end
    def __repr__(self):
        return f"({self.var_name} = {self.value})"

class VarDeclareNode(Node):
    def __init__(self, var_name: str, var_type: types_.Type, value: Node | None, pos_start: pos.Position, pos_end = pos.Position):
        self.var_name = var_name
        self.var_type = var_type
        self.value = value
        self.pos_start = pos_start
        self.pos_end = pos_end
    def __repr__(self):
        return f"[variable {self.var_name}: {self.var_type}" + (
            f" = {self.value}]" if self.value else "]"
        )

class BlockNode(Node):
    def __init__(self, nodes: list[Node], pos_start: pos.Position, pos_end: pos.Position):
        self.nodes = nodes
        self.pos_start = pos_start
        self.pos_end = pos_end
    def __repr__(self):
        return f"(block: {self.nodes})"

class FuncDeclNode(Node):
    def __init__(self, name: str, args: dict[str, types_.Type], return_type: types_.Type, body: BlockNode, pos_start: pos.Position, pos_end: pos.Position):
        self.name = name
        self.args = args
        self.return_type = return_type
        self.body = body
        self.pos_start = pos_start
        self.pos_end = pos_end
    def __repr__(self):
        return f"(function {self.name}({self.args})) -> {self.return_type} {self.body})"

class ReturnNode(Node):
    def __init__(self, value: Node, pos_start: pos.Position):
        self.value = value
        self.pos_start = pos_start
        self.pos_end = value.pos_end
    def __repr__(self):
        return f"(return {self.value})"

class CallNode(Node):
    def __init__(self, node: Node, arguments: list[Node], pos_end: pos.Position):
        self.node = node
        self.arguments = arguments
        self.pos_end = pos_end
        self.pos_start = node.pos_start
    def __repr__(self):
        return f"(call {self.node} {self.arguments})"