import pos

class Error:
    def __init__(self, value: str, pos_start: pos.Position, pos_end: pos.Position):
        self.value = value
        self.pos_start = pos_start
        self.pos_end = pos_end
    
    def __repr__(self):
        return f"[ERROR {self.value} {self.pos_start}-{self.pos_end}]"
    
    def __str__(self):
        return f"Error: {self.value}"
    
    def display(self, text: str) -> str:
        disp_text: str = (
            f"Error at line {self.pos_start.line + 1}, col {self.pos_start.col + 1}:\n"
            f"{self.value}\n"
        )
        line_text = text.split("\n")[self.pos_start.line]
        disp_text += line_text
        disp_text += "\n"
        disp_text += " " * self.pos_start.col
        if self.pos_start.line == self.pos_end.line:
            disp_text += "^" * (self.pos_end.col - self.pos_start.col)
        else:
            disp_text += "^" * (self.pos_end.col - len(line_text) - 1)

        return disp_text
