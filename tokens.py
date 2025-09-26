from enum import Enum
from typing import Any
from pos import Position

TokenType = Enum("TokenType", [
    "EOF", "INT", "FLOAT", "PLUS", "MINUS", "ASTERISK", "SLASH", "L_PAREN", "R_PAREN",
    "STR",
])

class Token:
    def __init__(self, token_type: TokenType, value: Any, pos_start: Position, pos_end: Position):
        self.token_type = token_type
        self.value = value
        self.pos_start = pos_start
        self.pos_end = pos_end
    def __repr__(self):
        string_repr: str = f"[{self.token_type.name}"
        if self.value:
            string_repr += f":{self.value!r}"
        string_repr += "]"
        return string_repr
