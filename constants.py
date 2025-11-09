from types_ import Type as _Type
LETTERS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LETTERS_LOWER = "abcdefghijklmnopqrstuvwxyz"
LETTERS = LETTERS_UPPER + LETTERS_LOWER
KEYWORDS: dict[str, str] = {
    "declare_var": "var",
}
TYPES: dict[str, _Type] = {
    "int": _Type.INT,
    "float": _Type.FLOAT,
    "char": _Type.CHAR,
    "str": _Type.STR,
}