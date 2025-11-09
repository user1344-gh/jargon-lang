import nodes as n
from tokens import Token, TokenType
from result import ParseResult as Result
from pos import Position
from operators import Operator
from typing import Callable
from error import Error
from constants import KEYWORDS, TYPES

class Parser:
    def __init__(self, tokens: list[Token]):
        self.tokens = tokens
        self.index = -1
        self.current_token: Token = self.advance()
    def advance(self, amount: int = 1):
        self.index += amount
        if self.index >= len(self.tokens):
            self.current_token = self.tokens[-1]
        else:
            self.current_token = self.tokens[self.index]
        return self.current_token

    def parse(self) -> Result:
        if len(self.tokens) == 1:
            return Result()
        output = self.parse_statement()
        if output.err:
            return output
        if self.index < len(self.tokens) - 1:
            return output.error(Error("Unexpected token.", self.current_token.pos_start, self.current_token.pos_end))
        return output
    
    # PARSING
    
    def parse_statement(self) -> Result:
        res = Result()
        if self.current_token.match_keyword(KEYWORDS["declare_var"]):
            pos_start = self.current_token.pos_start
            self.advance()
            if self.current_token.token_type != TokenType.IDENTIFIER:
                return res.error(Error("Expected identifier", self.current_token.pos_start, self.current_token.pos_end))
            variable = self.current_token.value
            self.advance()
            if self.current_token.token_type != TokenType.COLON:
                return res.error(Error("Expected ':'", self.current_token.pos_start, self.current_token.pos_end))
            self.advance()
            if self.current_token.token_type != TokenType.TYPE:
                return res.error(Error("Expected type", self.current_token.pos_start, self.current_token.pos_end))
            var_type = TYPES[self.current_token.value]
            self.advance()
            if self.current_token.token_type == TokenType.EQUALS:
                self.advance()
                value = res.process(self.parse_expression())
                if res.err: return res
                value = value.get_success()
            else:
                value = None

            return res.success(n.VarDeclareNode(variable, var_type, value, pos_start, self.current_token.pos_end)) # pyright: ignore[reportArgumentType]
        else:
            return self.parse_expression()
    def parse_expression(self) -> Result:
        return self.parse_equality_expr()
    def parse_equality_expr(self) -> Result:
        return self.parse_binary_operation(
            self.parse_logical,
            [TokenType.EQEQ, TokenType.NOTEQ],
            [Operator.EQ, Operator.NOT_EQ]
        )
    def parse_logical(self) -> Result:
        return self.parse_binary_operation(
            self.parse_comparison,
            [TokenType.ANDAND, TokenType.PIPEPIPE],
            [Operator.LOGIC_AND, Operator.LOGIC_OR]
        )
    def parse_comparison(self) -> Result:
        return self.parse_binary_operation(
            self.parse_arithmetic,
            [TokenType.LT, TokenType.GE, TokenType.LE],
            [Operator.LT, Operator.GE, Operator.LE]
        )
    def parse_arithmetic(self) -> Result:
        return self.parse_binary_operation(
            self.parse_bitwise, [TokenType.PLUS, TokenType.MINUS], [Operator.ADD, Operator.SUB]
        )
    def parse_bitwise(self) -> Result:
        return self.parse_binary_operation(
            self.parse_term,
            [TokenType.AND, TokenType.PIPE, TokenType.CARET],
            [Operator.AND, Operator.OR, Operator.XOR]
        )
    def parse_term(self) -> Result:
        return self.parse_binary_operation(
            self.parse_factor, [TokenType.ASTERISK, TokenType.SLASH], [Operator.MUL, Operator.DIV]
        )
    def parse_factor(self) -> Result:
        res = Result()  
        
        if self.current_token.token_type in (TokenType.MINUS, TokenType.TILDE, TokenType.EXCLAMATION):
            op_token = self.current_token
            self.advance()
            value = res.process(self.parse_factor())
            if res.err:
                return res
            return res.success(n.UnaryOpNode((
                Operator.LOGIC_NOT if op_token.token_type == TokenType.NOTEQ else
                Operator.NOT if op_token.token_type == TokenType.TILDE else
                Operator.NEG
            ), value.get_success(), self.current_token.pos_start))
        
        return self.parse_atom()
    def parse_atom(self) -> Result:
        res = Result()
        
        if self.current_token.token_type == TokenType.INT:
            res = res.success(n.IntNode(self.current_token))
            self.advance()
            return res
        elif self.current_token.token_type == TokenType.FLOAT:
            res = res.success(n.FloatNode(self.current_token))
            self.advance()
            return res
        elif self.current_token.token_type == TokenType.STR:
            res = res.success(n.StringNode(self.current_token))
            self.advance()
            return res
        elif self.current_token.token_type == TokenType.CHAR:
            res = res.success(n.CharNode(self.current_token))
            self.advance()
            return res
        elif self.current_token.token_type == TokenType.L_PAREN:
            self.advance()
            expr = res.process(self.parse_expression())
            if res.err:
                return res
            if self.current_token.token_type != TokenType.R_PAREN:
                return res.error(Error("Expected ')'", self.current_token.pos_start, self.current_token.pos_end))
            self.advance()
            return expr
        elif self.current_token.token_type == TokenType.IDENTIFIER:
            identifier = self.current_token
            self.advance()
            if self.current_token.token_type == TokenType.EQUALS:
                self.advance()
                value = res.process(self.parse_expression())
                if res.err: return res
                return res.success(n.VarAssignNode(identifier.value, value.get_success(), identifier.pos_start))
            return res.success(n.VarNode(identifier))
        elif self.current_token.token_type == TokenType.EOF:
            return res.error(Error("Expected expression", self.current_token.pos_start, self.current_token.pos_end))
        return res.error(Error("Unexpected token", self.current_token.pos_start, self.current_token.pos_end))
    ####
    def parse_binary_operation(self, left_func: Callable, operator_tokentypes: list[TokenType], operators: list[Operator]) -> Result:
        res = Result()
        
        left = res.process(left_func())
        if res.err:
            return res
        if self.current_token.token_type in operator_tokentypes:
            operator = operators[operator_tokentypes.index(self.current_token.token_type)]
            self.advance()
            right = res.process(self.parse_binary_operation(left_func, operator_tokentypes, operators))
            if res.err:
                return res
            return res.success(n.BinaryOpNode(left.get_success(), operator, right.get_success()))
        return left
