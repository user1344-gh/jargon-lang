import lexer
import parser
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("COMMAND LIST: -D / --debug-line, -v / --version")
        sys.exit()

    cmd = sys.argv[1]
    args = sys.argv[2:]
    if cmd == "-D" or cmd == "--debug-line":
        text = " ".join(args)
        lexer_ = lexer.Lexer(text)
        lexer_res = lexer_.lex_text()

        if lexer_res[1]:
            print("LEXER ERROR\n", lexer_res[1].display(lexer_.text), file=sys.stderr, sep="")
            exit()
        print("LEXER OUTPUT:", lexer_res[0])
        parser_ = parser.Parser(lexer_res[0])
        parser_res = parser_.parse()
        if parser_res.err:
            print("PARSER ERROR\n", parser_res.err.display(text), file=sys.stderr, sep="")
            sys.exit()
        print("PARSER OUTPUT:", parser_res.ok)
    elif cmd == "-v" or cmd == "--version":
        print("Jargonlang v0.13.0 [251110]")
    else:
        print("Invalid command, refer to ./cmdline.md")
