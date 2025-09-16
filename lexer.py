from tokens import Token, TokenType
from result import LexerResult as Result

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.current_char: str = "\0"
        self.position = -1
        self.tokens: list[Token] = []
        self.advance()

    def advance(self):
        "Advances to the next character then returns it. Returns EOF if there are no characters left"
        if self.position >= len(self.text) -1:
            self.current_char = "\x1a" 
        else:
            self.position += 1
            self.current_char = self.text[self.position]
        return self.current_char
        
    def lex_text(self) -> tuple[list[Token], str | None]:
        while True:
            gen_result = self.gen_token()
            if not gen_result.is_success():
                return ([], gen_result.err)
            token = gen_result.get_success()
            self.tokens.append(token)
            if token.token_type == TokenType.EOF: 
                break
        return (self.tokens, None)
    
    def gen_token(self) -> Result:
        "Generates a token from the current character and advances as necessary."
        current_char = self.current_char
        if self.current_char == "\x1a":
            return Result(Token(TokenType.EOF))
        elif self.current_char in "0123456789":
            return self.gen_number()
        return Result(None, f"Invalid character: {current_char}")
    
    def gen_number(self) -> Result:
        num_str = self.current_char
        while self.advance() in "0123456789":
            num_str += self.current_char
        return Result(Token(TokenType.INT, int(num_str)))
    