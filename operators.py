from enum import Enum

Operator = Enum("Operator", [
    "ADD", "SUB", "MUL", "DIV", "NEG", "EQ", "GT", "LT", "GE", "LE", "NOT_EQ", "OR", "LOGIC_OR", "AND", "LOGIC_AND", "XOR",
    "NOT", "LOGIC_NOT"
])