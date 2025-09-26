from tokens import Token, TokenType
from result import LexerResult as Result
from pos import Position
from copy import copy
from error import Error

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.current_char: str = "\0"
        self.pos = Position(-1, 0, -1)
        self.tokens: list[Token] = []
        self.advance()

    def advance(self):
        "Advances to the next character then returns it. Returns EOF if there are no characters left"
        self.pos.increment()
        if self.pos.index >= len(self.text):
            self.current_char = "\x1a" 
        else:
            if self.current_char == "\n":
                self.pos.newline()
            self.current_char = self.text[self.pos.index]
        return self.current_char
        
    def lex_text(self) -> tuple[list[Token], Error | None]:
        while True:
            gen_result = self.gen_token()
            if not gen_result.is_success():
                return ([], gen_result.err)
            if not gen_result.ok:
                continue
            token = gen_result.get_success()
            self.tokens.append(token)
            if token.token_type == TokenType.EOF: 
                break
        return (self.tokens, None)
    
    def gen_token(self) -> Result:
        "Generates a token from the current character and advances as necessary."
        current_char = self.current_char
        pos_start = copy(self.pos)
        if self.current_char == "\x1a":
            return Result(Token(TokenType.EOF, None, pos_start, pos_start + 1))
        elif self.current_char in "0123456789.":
            return self.gen_number()
        elif self.current_char in " \n\t":
            self.advance()
            return Result(None)
        elif self.current_char == "+":
            self.advance()
            return Result(Token(TokenType.PLUS, None, pos_start, copy(self.pos)))
        elif self.current_char == "-":
            self.advance()
            return Result(Token(TokenType.MINUS, None, pos_start, copy(self.pos)))
        elif self.current_char == "*":
            self.advance()
            return Result(Token(TokenType.ASTERISK, None, pos_start, copy(self.pos)))
        elif self.current_char == "/":
            self.advance()
            return Result(Token(TokenType.SLASH, None, pos_start, copy(self.pos)))
        elif self.current_char == "(":
            self.advance()
            return Result(Token(TokenType.L_PAREN, None, pos_start, copy(self.pos)))
        elif self.current_char == ")":
            self.advance()
            return Result(Token(TokenType.R_PAREN, None, pos_start, copy(self.pos)))
        elif self.current_char == '"':
            return self.gen_string()
        return Result(None, Error(f"Unexpected character: {current_char!r}", pos_start, self.pos+1))
    
    def gen_number(self) -> Result:
        num_str = ""
        pos_start = copy(self.pos)
        token_type: TokenType = TokenType.INT
        contains_decimal_point = False
        while self.current_char in "0123456789.":
            if self.current_char == ".":
                if contains_decimal_point:
                    break
                contains_decimal_point = True
                token_type = TokenType.FLOAT
            num_str += self.current_char
            self.advance()
        if num_str == ".":
            num_str = "0.0"
        return Result(Token(token_type, num_str, pos_start, copy(self.pos)))
    
    def gen_string(self) -> Result:
        string = ""
        pos_start = copy(self.pos)
        escape = False
        while True:
            self.advance()
            if self.current_char == '"' and not escape:
                break
            if self.current_char == "\\" and not escape:
                escape = True
            else:
                escape = False
            if self.current_char == "\x1a":
                return Result(None, Error("Unterminated string literal, expected '\"'", pos_start, copy(self.pos)))
            string += self.current_char
        pos_end = copy(self.pos)
        self.advance()
        return Result(Token(TokenType.STR, string, pos_start, pos_end))
