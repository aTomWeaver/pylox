from token import Token
from tokentype import TokenType as tt
from typing import Optional


class Scanner:
    def __init__(self, source: str):
        self.source: str = source
        self.tokens: list[Token] = []

        self.start: int = 0     # points to first char in current lexeme
        self.current: int = 0   # points at current char being considered
        self.line: int = 1      # tracks current source line

    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        self.tokens.add(Token(tt.EOF, "", None, self.line))

    def isAtEnd(self):
        return self.current >= len(self.source)

    def __scanToken(self):
        c = self.__advance()
        if c == '(':
            self.__addToken(tt.LEFT_PAREN)
        elif c == ')':
            self.__addToken(tt.RIGHT_PAREN)
        elif c == '{':
            self.__addToken(tt.LEFT_BRACE)
        elif c == '}':
            self.__addToken(tt.RIGHT_BRACE)
        elif c == ',':
            self.__addToken(tt.COMMA)
        elif c == '.':
            self.__addToken(tt.DOT)
        elif c == '-':
            self.__addToken(tt.MINUS)
        elif c == '+':
            self.__addToken(tt.PLUS)
        elif c == ';':
            self.__addToken(tt.SEMICOLON)
        elif c == '*':
            self.__addToken(tt.STAR)

    def __advance(self):
        char = self.source[self.current]
        self.current += 1
        return char

    def __addToken(self,
                   type_: tt,
                   literal: Optional[str | float | bool] = None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type_, text, literal, self.line))
