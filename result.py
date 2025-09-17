import tokens
import error

class LexerResult:
    def __init__(self, ok: tokens.Token | None, err: error.LexerError | None = None):
        self.ok = ok
        self.err = err
    def get_success(self) -> tokens.Token:
        if self.ok:
            return self.ok
        raise TypeError("Expected success, got error")
    def get_error(self) -> error.LexerError:
        if self.err:
            return self.err
        raise TypeError("Expected error, got success")
    def is_success(self) -> bool:
        if self.err is None:
            return True
        return False
    def __repr__(self) -> str:
        return f"[OK:{self.ok},ERR:{self.err}]"
    def __str__(self) -> str:
        if self.is_success():
            return f"[OK:{self.ok}]"
        return f"[ERR:{self.err}]"
