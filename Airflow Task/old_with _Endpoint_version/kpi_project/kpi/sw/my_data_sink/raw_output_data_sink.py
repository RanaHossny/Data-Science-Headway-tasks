
"""
raw output data sink 
"""
from .data_sink import DataSink
class RawDataSink(DataSink):
    """A simple data sink that writes to the console."""
    def __init__(self):
        "init the raw data sink"
        self.state=0
        self.data=None
    def connect(self):
        "start connection"
        self.state=1
        print("Connected to  Data Sink.")
    def write(self, data):
        "write data"
        if (self.state==0):
            print("the datasink is not connected")
        else:
            self.data=data  
    def close(self):
        "to end connection"
        self.state=0
        print("Closed Console Data Sink.")
