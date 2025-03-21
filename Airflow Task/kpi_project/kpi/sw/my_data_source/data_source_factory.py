"""
data_source_factory.py:
define Data_Source_Factory which is responsible of the data source selection
"""
from .data_source import REGISTRY
#this include is a must to ensure that the complier doesnt optimize the code in runtime
from .text_data_source import TextDataSource
from .json_data_source  import JsonDataSource
class DataSourceFactory:
    """
    class Data_Source_Factory which is responsible for the data source selection based on the
    given type
    """
    @staticmethod
    def create_data_source(data_source_type, *args, **kwargs):
        """Create a data source instance based on the type provided."""
        if data_source_type in REGISTRY:
            return (REGISTRY[data_source_type](*args, **kwargs))
        else:
            raise ValueError(f"Data source type '{data_source_type}' is not recognized.")
