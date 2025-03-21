"""
file  data sink : to define the behavior of all data sink (abstact class)

"""
from abc import abstractmethod
import re
DATA_SINK_REGISTRY = {}
def get_first_word(class_name):
    """Use regex to find the first capitalized word"""
    match = re.match(r'([A-Z][a-z]*)', class_name)
    return match.group(0) if match else None

def register_class(target_class):
    """Registers a class in the global registry using only the first part of its name."""
    class_name_key = get_first_word(target_class.__name__)
    DATA_SINK_REGISTRY[class_name_key] = target_class


class MetaRegistry(type):
    """Metaclass for automatic registration of subclasses."""
    def __new__(meta, name, bases, class_dict):
        cls = super().__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class DataSink(metaclass=MetaRegistry):
    """
    abstract class to define the methods for all data sinks
    """
    @abstractmethod
    def connect(self):
        """Connects to the data sink, e.g., opening a file or a database connection."""
    @abstractmethod
    def write(self, data):
        """Writes data to the sink."""
    @abstractmethod
    def close(self):
        """Closes the connection to the sink."""
