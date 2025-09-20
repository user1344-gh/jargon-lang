import tokens
import nodes
import error

class LexerResult:
    def __init__(self, ok: tokens.Token | None, err: error.Error | None = None):
        self.ok = ok
        self.err = err
    def get_success(self) -> tokens.Token:
        if self.ok:
            return self.ok
        raise TypeError("Expected success, got error")
    def get_error(self) -> error.Error:
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

class Result:
    def __init__(self):
        self.ok = None
        self.err = None
    def get_success(self):
        if self.ok:
            return self.ok
        raise TypeError(f"Expected success, got error: {self.err}")
    def get_error(self) -> error.Error:
        if self.err:
            return self.err
        raise TypeError("Expected error, got success")
    def is_success(self) -> bool:
        if self.err is None:
            return True
        return False
    def process(self, res):
        if res.err:
            self.err = res.err
        return res
    def success(self, ok):
        self.ok = ok
        return self
    def error(self, err: error.Error):
        self.err = err
        return self
    def __repr__(self) -> str:
        return f"[OK:{self.ok},ERR:{self.err}]"
    def __str__(self) -> str:
        if self.is_success():
            return f"[OK:{self.ok}]"
        return f"[ERR:{self.err}]"

class ParseResult(Result):
    def __init__(self):
        self.ok: None | nodes.Node = None
        self.err = None
