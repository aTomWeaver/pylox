from tokentype import TokenType
from typing import Optional


class Token:
    def __init__(self,
                 type_: TokenType,
                 lexeme: str,
                 literal: Optional[str | float | bool],
                 line: int):
        self.type = type_
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def toString(self):
        return f"{self.type} {self.lexeme} {self.literal}"
