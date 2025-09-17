class Position:
    def __init__(self, index: int, line: int, col: int):
        self.index = index
        self.line = line
        self.col = col
    def increment(self, amount: int = 1):
        self.index += amount
        self.col += amount
    def newline(self):
        self.col = 0
        self.line += 1
    def __repr__(self):
        return f"({self.index}:{self.col},{self.line})"
    def __add__(self, right: int):
        return Position(self.index + 1, self.line, self.col + 1)