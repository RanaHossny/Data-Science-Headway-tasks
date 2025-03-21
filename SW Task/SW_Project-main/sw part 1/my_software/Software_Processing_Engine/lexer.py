"""
Lexer Module

This module defines the Lexer class responsible for tokenizing input text 
into a list of tokens. The Lexer reads the input character by character and 
identifies valid tokens based on predefined rules. It utilizes various token 
types defined in the tokens module and raises exceptions for invalid characters.

Classes:
    - Lexer: The main class that performs the tokenization.
"""
from my_software.Software_Processing_Engine.syntax_error import InvalidCharacterException
# this include to insure that the complier not optimize those code as the used one depend on the user
from my_software.Software_Processing_Engine.tokens import *

class Lexer(object):
    """ class lexer"""
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None
        self.token_list=self._get_all_token_types()

    def _get_all_token_types(self):
        token_types = []
        for subclass in Token.__subclasses__():
            token_types.append(subclass())
        return token_types


    def error(self):
        """Raise an invalid character exception."""
        raise InvalidCharacterException(self.current_char)

    def advance(self):
        "get the next char"
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        "skip white space"
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def match_word(self):
        "get the word"
        result = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char.isalpha()):
            result += self.current_char
            self.advance()
        return self.matched_token(result)

    def matched_token(self, result):
        "get the token type word or integer or attr or regex"
        for token_type in  self.token_list :
            if(result == token_type.reserved_word ):
                return token_type
        if result.isdigit():
            return Num(int(result))
        
        else:
            return Word(result)

    def get_next_token(self):
        "get next token"
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit() or self.current_char.isalpha():
                return self.match_word()
            for current_token_type in  self.token_list :
                if(current_token_type.token_type not in ['INTEGER','WORD']):
                    if(self.current_char == current_token_type.value and not current_token_type.reserved_word):
                        self.advance()
                        return current_token_type

            # Raise error if none of the above conditions are met
            self.error()

        return Eof()
