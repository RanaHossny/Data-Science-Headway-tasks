"""
Ingestor Module

This module defines the Ingestor class responsible for ingesting data from 
various data sources. It utilizes a factory pattern to create and connect 
to a specified data source type, allowing for flexibility in handling 
different data input methods.

Classes:
    - Ingestor: Handles data ingestion from the specified data source.
"""
from ...my_data_source.data_source_factory import DataSourceFactory 
class Ingestor:
    """
    Ingestor Class

    This class is responsible for ingesting data from various data sources 
    using the Factory pattern. It connects to a specified data source and 
    allows fetching data from it.
    """
    def __init__(self,data_source_type="Text",*args):
        """
        Initialize the Ingestor.

        This constructor creates a data source instance using the factory 
        and establishes a connection to it.

        Args:
            data_source_type (str): The type of the data source to be used (default is "Text").
            *args: Additional arguments passed to the data source constructor.
        """
        self.data_source = DataSourceFactory.create_data_source(data_source_type, *args)
        self.data_source.connect()
    def send_msg(self):
        """
        Fetch data from the connected data source.

        This method retrieves data from the data source.

        Returns:
            The data fetched from the data source.
        """
        return self.data_source.fetch_data()







    



