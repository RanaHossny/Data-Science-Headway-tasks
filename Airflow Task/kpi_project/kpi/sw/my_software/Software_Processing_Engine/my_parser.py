# Import necessary token types
from ..Software_Processing_Engine.my_operator import PlusOp,MinusOp,MultiplyOp,DivideOp,AtterOp,RegexOperationOp
from ..Software_Processing_Engine.syntax_error import SyntaxErrorException

###############################################################################
#                                                                             #
#  PARSER                                                                     #
#                                                                             #
###############################################################################
class Parser(object):
    """Class Parser"""
    def __init__(self, lexer,attr_value=0):
        self.lexer = lexer
        # Set current token to the first token taken from the input
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
        self.error()  # Raise an error if none of the conditions are met
        
    def minus_factor(self):
            self.eat("MINUS")
            return MinusOp(left=self.factor(), right=None)

    def plus_factor(self):
            self.eat("PLUS")
            return PlusOp(left=self.factor(), right=None)

    def integer_factor(self):
            token=self.current_token
            self.eat("INTEGER")
            return AtterOp(token)

    def attr_factor(self):
            token=self.current_token
            token.value=self.attr_value
            self.eat("ATTR")
            return AtterOp(token)

    def lparen_factor(self):
            self.eat("LPAREN")
            node = self.expr()
            self.eat("RPAREN")
            return node

    def regex_factor(self):
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

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        term   : factor ((MUL | DIV) factor)*
        factor : INTEGER | LPAREN expr RPAREN | Regex(ATTR, ^WORD)
        """
        node = self.term()
        while self.current_token.token_type in ("PLUS", "MINUS"):
            token = self.current_token
            if token.token_type == "PLUS":
                self.eat("PLUS")
                node = PlusOp(node, self.term())  # Use Plus class
            elif token.token_type == "MINUS":
                self.eat("MINUS")
                node = MinusOp(node, self.term())  # Use Minus class
        return node

    def parse(self):
        """Apply parsing"""
        return self.expr()