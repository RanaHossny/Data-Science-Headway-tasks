"""
exceptions.py

This module defines custom exceptions for the software processing framework.
These exceptions are used to handle specific error scenarios that may occur
during data ingestion and processing.
"""
class IngestorError(Exception):
    """Exception raised for errors in the ingestor."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ProcessingEngineError(Exception):
    """Exception raised for errors in the processing engine."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
