from expr import Expr, Binary
from token_ import Token
from tokentype import TokenType as tt


class Parser:
    def __init__(self, tokens: list[tt]):
        self.tokens: list[tt] = tokens
        self.current: int = 0           # points to next token to parse

    def expression(self):
        return self.equality()

    def equality(self) -> Expr:
        expr: Expr = self.comparison()
        while (self.match(tt.BANG_EQUAL, tt.EQUAL_EQUAL)):
            operator: Token = self.previous()
            right: Expr = self.comparison()
            expr: Binary = Binary(expr, operator, right)
        return expr

    def match(self, *types):
        for type_ in types:
            if self.check(type_):
                self.advance()
                return True
        return False

    def check(self, type_: tt):
        if self.is_at_end():
            return False
        return self.peek().type_ == type_

    def advance(self):
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().type == tt.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def comparison(self) -> Expr:
        expr: Expr = self.term()

    def term(self):
        pass
