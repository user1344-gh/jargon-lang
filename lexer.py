from tokens import Token, TokenType
from result import LexerResult as Result
from pos import Position
from copy import copy
from error import LexerError as Error

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
        elif self.current_char in "0123456789":
            return self.gen_number()
        elif self.current_char in " \n\t":
            self.advance()
            return Result(None)
        return Result(None, Error(f"Invalid character: {current_char!r}", pos_start, copy(self.pos)+1))
    
    def gen_number(self) -> Result:
        num_str = self.current_char
        pos_start = copy(self.pos)
        while self.advance() in "0123456789":
            num_str += self.current_char
        return Result(Token(TokenType.INT, int(num_str), pos_start, copy(self.pos)))
    