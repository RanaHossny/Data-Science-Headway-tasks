"""
file  data source : to define the behavior of all data source (abstact class)
"""
from abc import abstractmethod
import re
REGISTRY = {}

def get_first_word(class_name):
    """Use regex to find the first capitalized word"""
    match = re.match(r'([A-Z][a-z]*)', class_name)
    return match.group(0) if match else None

def register_class(target_class):
    """Registers a class in the global registry using only the first part of its name."""
    class_name_key = get_first_word(target_class.__name__)
    REGISTRY[class_name_key] = target_class


class MetaRegistry(type):
    """Metaclass for automatic registration of subclasses."""
    def __new__(meta, name, bases, class_dict):
        cls = super().__new__(meta, name, bases, class_dict)
        register_class(cls)
        return cls

class DataSource(metaclass=MetaRegistry):
    """Base class for data sources."""
    @abstractmethod
    def connect(self):
        """Connect to the data source."""
    @abstractmethod
    def fetch_data(self):
        """Fetch data from the data source."""
    @abstractmethod
    def close_connection(self):
        """Close the connection to the data source."""  
