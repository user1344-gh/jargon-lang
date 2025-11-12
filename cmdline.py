import sys
import lexer
import parser
import constants as c

FLAG_LIST = {"-d"}
OPTION_LIST = {}

def run(input_args: list[str]):
    if len(input_args) == 0:
        print("COMMAND LIST: -v / --version")
        print("FLAGS: -d")
        print("OPTIONS: NONE")
        sys.exit()

    input_args = sys.argv[1:]
    if input_args[0] == "-v" or input_args[0] == "--version":
        print(f"Jargonlang v{c.VERSION_MAJOR}.{c.VERSION_MINOR}.{c.VERSION_PATCH} [{c.RELEASE_YEAR}-{c.RELEASE_MONTH}-{c.RELEASE_DAY}]")
    else:
        args, flags, options = process(input_args)
        if len(args) == 0:
            raise ValueError("Expected filename")
        elif len(args) > 1:
            raise ValueError("Too many arguments")
        with open(args[0], "r") as file:
            text = file.read()
        lexer_ = lexer.Lexer(text)
        lexer_res = lexer_.lex_text()

        if lexer_res[1]:
            print(lexer_res[1].display(lexer_.text), file=sys.stderr, sep="")
            exit()
        if "-d" in flags:
            print("LEXER OUTPUT:", lexer_res[0])
        parser_ = parser.Parser(lexer_res[0])
        parser_res = parser_.parse()
        if parser_res.err:
            print(parser_res.err.display(text), file=sys.stderr, sep="")
            sys.exit()
        if "-d" in flags:
            print("PARSER OUTPUT:", parser_res.ok)
        print(parser_res.ok)

def process(input_args: list[str]) -> tuple[list[str], set[str], dict[str, str]]: # (args, flags, options)
    args = []
    flags = set()
    options = {}

    i = 0
    while i < len(input_args):
        v: str = input_args[i]
        if v.startswith("-"):
            if v in FLAG_LIST:
                flags.add(v)
            elif v in OPTION_LIST:
                option = v
                i += 1
                if i == len(input_args):
                    raise ValueError("Expected argument for option: " + option)
                options[option] = input_args[i]
            else:
                raise ValueError("Invalid flag or option: " + v)
        else:
            args.append(v)
        i += 1
    return (args, flags, options)