"""
data_sink_factory.py:
define DataSinkFactory which is responsible of the data source selection
"""
from .data_sink import DATA_SINK_REGISTRY
from .mysql_data_sink import MysqlDataSink  
from .raw_output_data_sink import  RawDataSink
class DataSinkFactory:
    """
    Create a data sink instance based on the type provided.
    """
    @staticmethod
    def create_data_sink(data_sink_type, *args, **kwargs):
        """Create a data source instance based on the type provided."""
        if data_sink_type in DATA_SINK_REGISTRY:
            return DATA_SINK_REGISTRY[data_sink_type](*args, **kwargs)
        else:
            raise ValueError(f"Data source type '{data_sink_type}' is not recognized.")