from types_ import Type as _Type
LETTERS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_LOWER = "abcdefghijklmnopqrstuvwxyz"
LETTERS = LETTERS_UPPER + LETTERS_LOWER
NUMBERS = "0123456789"
ALPHANUMERIC = LETTERS + NUMBERS
KEYWORDS: dict[str, str] = {
    "declare_var": "var",
    "declare_func": "func",
    "return_value": "return",
}
TYPES: dict[str, _Type] = {
    "int": _Type.INT,
    "float": _Type.FLOAT,
    "char": _Type.CHAR,
    "str": _Type.STR,
}

VERSION_MAJOR = 0
VERSION_MINOR = 16
VERSION_PATCH = 0

RELEASE_YEAR  = 2025
RELEASE_MONTH = 11
RELEASE_DAY   = 13
