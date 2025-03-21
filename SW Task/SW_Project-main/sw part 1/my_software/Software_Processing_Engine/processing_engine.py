"""
Processing_Engine.py

This module is responsible for processing expressions and operations in the parsing framework.

Usage:
Import this module to utilize the Parser class and handle mathematical and logical expressions.
"""
from my_data_source.data_source_factory import Data_Source_Factory
from my_software.Software_Processing_Engine.lexer import Lexer
from my_software.Software_Processing_Engine.my_parser import Parser
from my_software.Software_Processing_Engine.interpreter import Interpreter
from my_software.Software_Output_Message_Producer.output_message_producer import OutputMessageProducer
class ProcessingEngine():
    """
    class Processing_Engine which is responsible for the proceesiong on the expression and 
    give the result for the ths software output preducer
    """
    def __init__(self,processing_engine_arg=None,data_sink_args=None):
        """"
        args:
        -the args of the data_souce to connect the  processing engine with the data source
        -the args of data sink to pass them for Output_Message_Producer
        """
        self.data_source = Data_Source_Factory.create_data_source(*processing_engine_arg)
        self.data_source.connect()
        self.eq=self.data_source.fetch_data()
        self.output_producer=OutputMessageProducer(data_sink_args)
    def start(self,current_msg):
        """
        start method to start processing the msg
        input: msg which include the asset informations
        """
        lexer=Lexer(self.eq)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        parser.attr_value=current_msg.get("value")
        result = interpreter.interpret()
        self.output_producer.start(current_msg,result)
