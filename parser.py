import nodes as n
from tokens import Token, TokenType
from result import ParseResult as Result
from pos import Position
from operators import Operator
from typing import Callable
from error import Error

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
        output = self.parse_expression()
        if output.err:
            return output
        if self.index < len(self.tokens) - 1:
            print(self.index, len(self.tokens))
            return output.error(Error("Unexpected token.", self.current_token.pos_start, self.current_token.pos_end))
        return output
    
    # PARSING

    def parse_expression(self) -> Result:
        return self.parse_comparison()
    def parse_comparison(self) -> Result:
        return self.parse_binary_operation(
            self.parse_arithmetic,
            [TokenType.EQEQ, TokenType.GT, TokenType.LT, TokenType.GE, TokenType.LE],
            [Operator.EQ, Operator.GT, Operator.LT, Operator.GE, Operator.LE]
        )
    def parse_arithmetic(self) -> Result:
        return self.parse_binary_operation(
            self.parse_term, [TokenType.PLUS, TokenType.MINUS], [Operator.ADD, Operator.SUB]
        )
    def parse_term(self) -> Result:
        return self.parse_binary_operation(
            self.parse_factor, [TokenType.ASTERISK, TokenType.SLASH], [Operator.MUL, Operator.DIV]
        )
    def parse_factor(self) -> Result:
        res = Result()
        
        if self.current_token.token_type == TokenType.MINUS:
            op_token = self.current_token
            self.advance()
            value = res.process(self.parse_factor())
            if res.err:
                return res
            return res.success(n.UnaryOpNode(Operator.NEG, value.get_success(), self.current_token.pos_start))
        
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
