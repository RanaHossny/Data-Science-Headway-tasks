"""
syntax_error.py

This module defines custom exceptions for syntax errors in the parsing process.

Classes:
- SyntaxErrorException: Custom exception raised when there is a syntax error in the input.

Usage:
Import this module to handle syntax errors gracefully during the parsing of expressions.
"""
class InvalidCharacterException(Exception):
    """Exception raised for invalid characters in the lexer."""
    def __init__(self, character):
        super().__init__(f'Invalid character: {character}')
        self.character = character

class SyntaxErrorException(Exception):
    """Syntax Error Exception"""
