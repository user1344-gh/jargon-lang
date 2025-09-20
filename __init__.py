import lexer
import parser
import sys

text = " ".join(sys.argv[1:])
lexer_ = lexer.Lexer(text)
lexer_res = lexer_.lex_text()

if lexer_res[1]:
    print("LEXER ERROR\n", lexer_res[1].display(lexer_.text), file=sys.stderr)
    exit()
print("LEXER OUTPUT:", lexer_res[0])
parser_ = parser.Parser(lexer_res[0])
parser_res = parser_.parse()
if parser_res.err:
    print("PARSER ERROR\n", parser_res.err.display(text), file=sys.stderr)
    sys.exit()
print("PARSER OUTPUT:", parser_res.ok)
