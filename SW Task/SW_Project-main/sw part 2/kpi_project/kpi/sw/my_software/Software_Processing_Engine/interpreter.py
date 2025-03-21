class Interpreter:
    """Class responsible for interpreting and evaluating parsed expressions."""
    
    def __init__(self, parser):
        """Initialize the Interpreter with a parser instance.
        
        Args:
            parser: An instance of the parser class to parse expressions.
        """
        self.parser = parser

    def interpret(self):
        """Interpret the parsed expression and return its value.
        
        Returns:
            The evaluated value of the expression tree.
        """
        tree = self.parser.parse()
        return tree.get_value()
