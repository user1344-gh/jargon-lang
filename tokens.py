from enum import Enum
from typing import Any

TokenType = Enum("TokenType", [
    "INT", "EOF"
])

class Token:
    def __init__(self, token_type: TokenType, value: Any = None):
        self.token_type = token_type
        self.value = value
    def __repr__(self):
        string_repr: str = f"[{self.token_type.name}"
        if self.value:
            string_repr += f":{self.value}]"
        else:
            string_repr += "]"
        return string_repr
