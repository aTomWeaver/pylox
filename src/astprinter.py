from Expr import Literal, Unary, Binary, Grouping
from token_ import Token
from tokentype import TokenType as tt


class AstPrinter:
    def print(self, expr):
        return expr.accept(self)

    def visitBinary(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visitGrouping(self, expr):
        return self.parenthesize("group", expr.expression)

    def visitLiteral(self, expr):
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visitUnary(self, expr):
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name, *args) -> str:
        '''return a string of a parenthesized expression from given args.'''
        pstring = f"({name}"
        for expr in args:
            pstring += f" {expr.accept(self)}"
        pstring += ")"
        return pstring


if __name__ == "__main__":
    # Just a test to check that it works
    a = AstPrinter()
    star, minus = Token(tt.STAR, "*", None, 1), Token(tt.MINUS, "-", None, 1)
    expr = Binary(
            Unary(minus, Literal(123)),
            star,
            Grouping(Binary(Literal(45.67), star, Literal("Cat")))
            )
    print(a.print(expr))
