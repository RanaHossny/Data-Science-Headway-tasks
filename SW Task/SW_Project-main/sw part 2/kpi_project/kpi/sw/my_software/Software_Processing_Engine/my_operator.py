from abc import ABC ,abstractmethod
import re 

class AST(ABC):
    """Abstract base class for all nodes in the AST."""
    @abstractmethod
    def get_value(self):
        """Get the value of the tree or node."""

class UnaryOp(AST):
    """Class for unary operations.""" 
    def __init__(self, op_type, expr):
        """
        Initialize a UnaryOp instance.

        Args:
            op_type (str): The type of the unary operation (e.g., '-', 'NOT').
            expr (AST): The expression that the unary operation applies to.
        """
        self.op_type = op_type
        self.expr = expr

    def __str__(self):
        """Return a string representation of the UnaryOp."""
        return f"UnaryOp({self.op_type}, {self.expr})"
class BinOp(AST):
    """Class for binary operations."""
    def __init__(self, left, op_type, right):
        """
        Initialize a BinOp instance.

        Args:
            left (AST): The left operand of the binary operation.
            op_type (str): The type of the binary operation (e.g., '+', '-').
            right (AST): The right operand of the binary operation.
        """
        self.left = left
        self.op_type = op_type
        self.right = right

    def __str__(self):
        """Return a string representation of the BinOp."""
        return f"BinOp({self.left}, {self.op_type}, {self.right})"


class PlusOp(BinOp):
    """Class for addition operation."""
    def __init__(self, left, right):
        """Initialize a PlusOp instance."""
        super().__init__(left, "+", right)

    def get_value(self):
        """Return the result of the addition."""
        return int(self.left.get_value()) + int(self.right.get_value())

    def __str__(self):
        """Return a string representation of the PlusOp."""
        return f"Plus({self.left}, {self.right})"

class MinusOp(BinOp):
    """Class for subtraction operation."""    
    def __init__(self, left, right):
        """Initialize a MinusOp instance."""
        super().__init__(left, "-", right)

    def get_value(self):
        """Return the result of the subtraction."""
        return int(self.left.get_value()) - int(self.right.get_value())

    def __str__(self):
        """Return a string representation of the MinusOp."""
        return f"Minus({self.left}, {self.right})"

class MultiplyOp(BinOp):
    """Class for multiplication operation."""    
    def __init__(self, left, right):
        """Initialize a MultiplyOp instance."""
        super().__init__(left, "*", right)

    def get_value(self):
        """Return the result of the multiplication."""
        return int(self.left.get_value()) * int(self.right.get_value())

    def __str__(self):
        """Return a string representation of the MultiplyOp."""
        return f"Multiply({self.left}, {self.right})"


class DivideOp(BinOp):
    """Class for division operation."""
    def __init__(self, left, right):
        """Initialize a DivideOp instance."""
        super().__init__(left, "/", right)

    def get_value(self):
        """Return the result of the division."""
        return int(self.left.get_value()) / int(self.right.get_value())

    def __str__(self):
        """Return a string representation of the DivideOp."""
        return f"Divide({self.left}, {self.right})"

class AtterOp(AST):
    """Class for attribute operations."""    
    def __init__(self, token):
        """
        Initialize an AtterOp instance.

        Args:
            token (Token): The token representing the attribute.
        """
        self.token = token
        self.value = token.value

    def get_value(self):
        """Return the value of the attribute."""
        return self.value

    def __str__(self):
        """Return a string representation of the AtterOp."""
        return f"Atter({self.token.value})"


class RegexOperationOp(AST):
    """Class to represent a regex operation in the AST."""    
    def __init__(self, left, right):
        """
        Initialize a RegexOperationOp instance.

        Args:
            left (AST): The left operand (could be an ATTR or other).
            right (AST): The right operand (expected to be a regex pattern or similar).
        """
        self.left = left
        self.token = None  # Placeholder for the token; set if needed
        self.right = right

    def get_value(self):
        """Get the value of the regex operation."""
        # Retrieve the attribute value (this part will depend on your Atter class implementation)
        value = self.left.value  # Modify as per your implementation
        pattern = self.right.value  # The regex pattern
        return re.match(pattern, value) is not None  # Return True/False based on match

    def __str__(self):
        """Return a string representation of the RegexOperation."""
        return f"RegexOperation({self.left}, {self.right})"


class AndOp(BinOp):
    """Class for logical AND operation."""    
    def __init__(self, left, right):
        """Initialize an AndOp instance."""
        super().__init__(left, "&", right)

    def get_value(self):
        """Return the result of the logical AND operation."""
        return int(self.left.get_value()) & int(self.right.get_value())

    def __str__(self):
        """Return a string representation of the AndOp."""
        return f"And({self.left}, {self.right})"
