
"""
raw output data sink 
"""
from my_data_sink.data_sink import DataSink
class RawDataSink(DataSink):
    """A simple data sink that writes to the console."""
    def __init__(self):
        self.state=0
        self.data=None
    def connect(self):
        self.state=1
        print("Connected to  Data Sink.")
    def write(self, data):
        if (self.state==0):
            print("the datasink is not connected")
        else:
            self.data=data  
    def close(self):
        self.state=0
        print("Closed Console Data Sink.")
