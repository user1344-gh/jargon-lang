import pos

class LexerError:
    def __init__(self, value: str, pos_start: pos.Position, pos_end: pos.Position):
        self.value = value
        self.pos_start = pos_start
        self.pos_end = pos_end
    
    def __repr__(self):
        return f"[ERROR {self.value} {self.pos_start}-{self.pos_end}]"
    
    def __str__(self):
        return f"Error: {self.value}"
    
    def display(self, text) -> str:
        disp_text: str = (
            f"Error at line {self.pos_start.line}, col {self.pos_start.col}:\n"
            + self.value
        )
        return disp_text