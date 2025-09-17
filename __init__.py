import lexer
import sys

lexer_ = lexer.Lexer("12.34")
lexer_res = lexer_.lex_text()

if lexer_res[1]:
    print(lexer_res[1].display(lexer_.text), file=sys.stderr)
else:
    print(lexer_res[0])
