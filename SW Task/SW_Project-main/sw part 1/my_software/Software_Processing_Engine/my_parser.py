"""
parser.py

This module defines the Parser class and related functionalities for parsing
mathematical expressions and handling operations including addition, 
subtraction, multiplication, division, and logical operations such as AND.

Classes:
- Parser: The main class responsible for parsing expressions.
- Token: Base class for all token types used in the parsing process.
- AST: Abstract base class for the Abstract Syntax Tree nodes.
- UnaryOp, BinOp, PlusOp, MinusOp, MultiplyOp, DivideOp, AtterOp, RegexOperationOp, AndOp: 
  Classes representing different operations in the AST.

Decorators:
- add_and_operation: A decorator that enhances the parsing function to handle AND operations.

Exceptions:
- SyntaxErrorException: Custom exception raised for syntax errors encountered during parsing.
"""
from my_software.Software_Processing_Engine.my_operator import PlusOp,MinusOp,MultiplyOp,DivideOp
from my_software.Software_Processing_Engine.my_operator import AtterOp,RegexOperationOp,AndOp
from my_software.Software_Processing_Engine.syntax_error import SyntaxErrorException
###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################
def add_and_operation(func):
    """
    Decorator to enhance the expression parsing function with AND operation handling.
    
    Args:
        func (function): The original parsing function to be wrapped.

    Returns:
        function: A wrapper function that adds AND operation handling to the parsed expression.
    """
    def wrapper(self, *args, **kwargs):
        # Call the original `expr` function to build the initial node
        node = func(self, *args, **kwargs)
        # Check for AND tokens after the main expr parsing
        while self.current_token.token_type in ("PLUS", "MINUS",'AND') :
            operation_name= self.current_token.token_type.capitalize()+'Op'
            self.eat(self.current_token.token_type)
            operation_func = globals()[operation_name]
            node = operation_func(node, self.term())
        return node
    return wrapper

class Parser(object):
    """Class for parsing expressions."""
    def __init__(self, lexer,attr_value=0):
        """
        Initialize the Parser.

        Args:
            lexer (Lexer): The lexer to tokenize input.
            attr_value (int, optional): Default attribute value to use. Defaults to 0.
        """
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()
        self.attr_value=attr_value
        self.first_factor_sets=["Regex","PLUS","MINUS","INTEGER","ATTR","LPAREN"]


    def error(self):
        """Return an error indicating invalid syntax."""
        raise SyntaxErrorException('Invalid syntax')

    def eat(self, token_type):
        """ Compare the current token type with the passed token type 
        and if they match then "eat" the current token and assign 
        the next token to self.current_token, otherwise raise an exception.
        """
        if self.current_token.token_type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN | Regex(ATTR, ^WORD)"""
        token = self.current_token
        for token_itr in self.first_factor_sets:
            if token.token_type == token_itr:
                function_name=token.token_type.lower()+'_factor'
                if hasattr(self, function_name):
                    return getattr(self, function_name)()
        # Raise an error if none of the conditions are met
        self.error()
    def minus_factor(self):
        """Parse a minus factor and return a MinusOp node."""
        self.eat("MINUS")
        return MinusOp(left=self.factor(), right=None)

    def plus_factor(self):
        """Parse a plus factor and return a PlusOp node."""
        self.eat("PLUS")
        return PlusOp(left=self.factor(), right=None)
    def and_factor(self):
        """Parse an AND factor and return an AndOp node."""
        self.eat("AND")
        return AndOp(left=self.factor(), right=None)

    def integer_factor(self):
        """Parse an integer factor and return an AtterOp node."""
        token=self.current_token
        self.eat("INTEGER")
        return AtterOp(token)

    def attr_factor(self):
        """Parse an attribute factor and return an AtterOp node with attribute value."""
        token=self.current_token
        token.value=self.attr_value
        self.eat("ATTR")
        return AtterOp(token)

    def lparen_factor(self):
        """Parse a left parenthesis and return the corresponding expression node."""
        self.eat("LPAREN")
        node = self.expr()
        self.eat("RPAREN")
        return node

    def regex_factor(self):
        """Parse a regex operation and return a RegexOperationOp node."""
        self.eat("Regex")
        self.eat("LPAREN")
        attr_token = self.current_token
        attr_token.value=self.attr_value
        self.eat("ATTR")
        self.eat("COMMA")
        self.eat("NOT")
        word_token = self.current_token  # Expecting WORD next
        self.eat('WORD')
        self.eat("RPAREN")
        return RegexOperationOp(left=attr_token, right=word_token)


    def term(self):
        """term : factor ((MUL | DIV) factor)*"""
        node = self.factor()
        while self.current_token.token_type in ("MUL", "DIV"):
            token = self.current_token
            if token.token_type == "MUL":
                self.eat("MUL")
                node = MultiplyOp(left=node, right=self.factor())
            elif token.token_type == "DIV":
                self.eat("DIV")
                node = DivideOp(left=node, right=self.factor())
            # node = BinOp(left=node, op=token, right=self.factor())

        return node
    @add_and_operation
    def expr(self):
        """
        expr   : term ((PLUS | MINUS|AND) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN | Regex(ATTR, ^WORD)
        """
        node = self.term()
        while self.current_token.token_type in ("PLUS", "MINUS"):
            operation_name= self.current_token.token_type.capitalize()+'Op'
            self.eat(self.current_token.token_type)
            operation_func = globals()[operation_name]
            node = operation_func(node, self.term())

        return node

    def parse(self):
        """Apply parsing"""
        return self.expr()
        