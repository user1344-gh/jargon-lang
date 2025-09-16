import lexer
import sys

lexer_ = lexer.Lexer("1234")
lexer_res = lexer_.lex_text()

if lexer_res[1]:
    print(lexer_res[1], file=sys.stderr)
else:
    print(lexer_res[0])
