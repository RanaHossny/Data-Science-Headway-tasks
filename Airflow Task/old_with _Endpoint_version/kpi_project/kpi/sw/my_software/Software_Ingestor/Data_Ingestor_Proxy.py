"""
This module defines the Ingestor_Proxy class, which acts as a proxy for the
Data Ingestor. It handles fetching messages from the ingestor and processing 
them with the specified processing engine. Messages are sent every 5 seconds
until there are no more messages to process.
"""
import time
from .Data_Ingestor import Ingestor
from ..Software_Processing_Engine.processing_engine import ProcessingEngine
from .error import IngestorError,ProcessingEngineError


class Ingestor_Proxy:
    def __init__(self,ingerstor_args=None,processing_engine_arg=None,data_sink_args=None):
        # Initialize the Data_Ingestor with the provided data source type and arguments

        self.ingestor = Ingestor(*ingerstor_args)
        self.lock = 0  # Initial lock state
        self.processing_engine= ProcessingEngine(processing_engine_arg,data_sink_args)

    def send_msg(self):
        """Fetch and send one message every 5 seconds."""
        try:
            # Fetch the next message from Ingestor
            message = self.ingestor.send_msg()
            while(True):
                self.processing_engine.start(message) 
                message = self.ingestor.send_msg()
                if  message is None:
                    break
            # Wait for 5 seconds before unlocking and allowing next message to be fetched
                time.sleep(5)

        except IngestorError as e:
            print(f"Ingestor error: {e}")
        except ProcessingEngineError as e:
            print(f"Processing engine error: {e}")
            return None

