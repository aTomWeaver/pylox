from typing import Optional
from token import Token
from tokentype import TokenType as tt


class Scanner:
    def __init__(self, parent, source: str):
        self.parent = parent
        self.source: str = source
        self.tokens: list[Token] = []

        self.start: int = 0     # points to first char in current lexeme
        self.current: int = 0   # points at current char being considered
        self.line: int = 1      # tracks current source line

    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.__scanToken()
        self.tokens.append(Token(tt.EOF, "", None, self.line))
        return self.tokens

    def isAtEnd(self):
        return self.current >= len(self.source)

    def __scanToken(self):
        # single-char tokens
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
        # possible multi-char tokens
        elif c == '!':
            self.__addToken(tt.BANG_EQUAL if self.__match('=') else tt.BANG)
        elif c == '=':
            self.__addToken(tt.EQUAL_EQUAL if self.__match('=') else tt.EQUAL)
        elif c == '<':
            self.__addToken(tt.LESS_EQUAL if self.__match('=') else tt.LESS)
        elif c == '>':
            self.__addToken(tt.GREATER_EQUAL if self.__match('=') else tt.GREATER)
        elif c == '/':
            if self.__match('/'):
                # // This is a comment
                while self.__peek() != '\n' and not self.isAtEnd():
                    self.__advance()
            else:
                self.__addToken(tt.SLASH)
        # Whitespace
        elif c == ' ':
            pass
        elif c == '\r':
            pass
        elif c == '\t':
            pass
        elif c == '\n':
            self.line += 1
        elif c == '"':
            self.__string()
        else:
            self.parent.error(self.line, f"Unexpected character: \"{c}\"")

    def __advance(self):
        '''Consume and return current character then increment self.current
        index by 1.'''
        char = self.source[self.current]
        self.current += 1
        return char

    def __addToken(self,
                   type_: tt,
                   literal: Optional[str | float | bool] = None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type_, text, literal, self.line))

    def __match(self, expected):
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True

    def __peek(self):
        '''Peek ahead at next character without consuming it like __advance()
        does.'''
        if self.isAtEnd():
            return '\0'
        return self.source[self.current]

    def __string(self):
        while self.__peek() != '"' and not self.isAtEnd():
            if self.__peek() == '\n':
                self.line += 1
            self.__advance()

        if self.isAtEnd():
            self.parent.error(self.line, "Unterminated string.")
            return

        self.__advance()  # This is the closing "

        value = self.source[self.start + 1:self.current - 1]
        self.__addToken(tt.STRING, value)
