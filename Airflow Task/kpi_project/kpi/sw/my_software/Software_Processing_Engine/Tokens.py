"""
token.py

This module defines various token classes used in the parsing process of
mathematical expressions. Each token class corresponds to a specific
type of token that can be encountered in the input, including
operators, numbers, parentheses, and attributes.

Classes:
- Token: Abstract base class for all tokens.
- Num: Represents an integer token.
- Plus: Represents the plus operator token.
- Minus: Represents the minus operator token.
- Multiply: Represents the multiplication operator token.
- Divide: Represents the division operator token.
- LParen: Represents the left parenthesis token.
- RParen: Represents the right parenthesis token.
- Attr: Represents an attribute token.
- Regex: Represents a regex token.
- Word: Represents a word token.
- Comma: Represents a comma token.
- Not: Represents a logical NOT operator token.
- And: Represents a logical AND operator token.
- Eof: Represents the end-of-file token.

This module is intended to be used in conjunction with the parser module
to tokenize input for expression evaluation and manipulation.
"""
from abc import ABC
class Token(ABC):
    """Abstract base class for tokens."""  
    def __init__(self, token_type, value, reserved_word=None):
        """Initialize a token with a specific type, value, and optional reserved word.
        
        Args:
            token_type (str): The type of the token.
            value (str): The value of the token.
            reserved_word (str, optional): An optional reserved word associated with the token.
        """
        self.token_type = token_type
        self.value = value
        self.reserved_word = reserved_word
    def __str__(self):
        """Return a string representation of the token."""
        return f'Token({self.token_type}, {repr(self.value)})'

    def __repr__(self):
        """Return the string representation of the token for debugging."""
        return self.__str__()

# Token classes
class Num(Token):
    """Token class for integers."""
    token_type = 'INTEGER'

    def __init__(self, value=0):
        """Initialize a Num token with a specified value (default is 0)."""
        super().__init__(self.token_type, value)

class Plus(Token):
    """Token class for the '+' operator."""
    token_type = 'PLUS'

    def __init__(self):
        """Initialize a Plus token."""
        super().__init__(self.token_type, '+')

class Minus(Token):
    """Token class for the '-' operator."""
    token_type = 'MINUS'

    def __init__(self):
        """Initialize a Minus token."""
        super().__init__(self.token_type, '-')

class Multiply(Token):
    """Token class for the '*' operator."""
    token_type = 'MUL'

    def __init__(self):
        """Initialize a Multiply token."""
        super().__init__(self.token_type, '*')

class Divide(Token):
    """Token class for the '/' operator."""
    token_type = 'DIV'

    def __init__(self):
        """Initialize a Divide token."""
        super().__init__(self.token_type, '/')

class LParen(Token):
    """Token class for the '(' (left parenthesis)."""
    token_type = 'LPAREN'

    def __init__(self):
        """Initialize a LParen token."""
        super().__init__(self.token_type, '(')

class RParen(Token):
    """Token class for the ')' (right parenthesis)."""
    token_type = 'RPAREN'

    def __init__(self):
        """Initialize a RParen token."""
        super().__init__(self.token_type, ')')

class Attr(Token):
    """Token class for attributes."""
    token_type = 'ATTR'

    def __init__(self):
        """Initialize an Attr token."""
        super().__init__(self.token_type, None, 'ATTR')

class Regex(Token):
    """Token class for regular expressions."""
    token_type = 'Regex'

    def __init__(self):
        """Initialize a Regex token."""
        super().__init__(self.token_type, 'Regex', 'Regex')

class Word(Token):
    """Token class for words."""
    token_type = 'WORD'

    def __init__(self, value=""):
        """Initialize a Word token with a specified value (default is empty)."""
        super().__init__(self.token_type, value)

class Comma(Token):
    """Token class for the ',' (comma)."""
    token_type = 'COMMA'

    def __init__(self):
        """Initialize a Comma token."""
        super().__init__(self.token_type, ',')

class Not(Token):
    """Token class for the 'NOT' operator."""
    token_type = 'NOT'

    def __init__(self):
        """Initialize a Not token."""
        super().__init__(self.token_type, '^')

class And(Token):
    """Token class for the 'AND' operator."""
    token_type = 'AND'

    def __init__(self):
        """Initialize an And token."""
        super().__init__(self.token_type, '&')

class Eof(Token):
    """Token class representing the end of the file/input."""
    token_type = 'EOF'

    def __init__(self):
        """Initialize an Eof token."""
        super().__init__(self.token_type, 'EOF')
