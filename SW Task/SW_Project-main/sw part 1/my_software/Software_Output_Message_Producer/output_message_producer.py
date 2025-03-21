"""
Output Message Producer Module

This module defines the OutputMessageProducer class, which is responsible 
for producing output messages and sending them to a data sink. The class 
utilizes a data sink factory to create a suitable data sink implementation 
based on the provided arguments. It manages the connection, message formatting, 
and writing process, as well as closing the data sink when finished.

Classes:
    - OutputMessageProducer: Manages the creation and writing of output 
      messages to a specified data sink.
"""
from my_data_sink.data_sink_factory import DataSinkFactory

class OutputMessageProducer():
    """
    Output Message Producer Class

    This class manages the creation and writing of output messages to a specified data sink.
    It utilizes a data sink factory to create a suitable data sink implementation based on 
    the provided arguments. The class handles connection management, message formatting, 
    and writing processes.
    """
    def __init__(self,datasink_args=None):
        """
        Initialize the Output_Message_Producer.

        Args:
            datasink_args (list): Arguments to create a data sink instance.
        """
        self.data_sink=DataSinkFactory.create_data_sink(*datasink_args)
        self.data_sink.connect()

    def start(self,msg,value):
        """
        Start the message production process.

        This method modifies the input message by adding a prefix to the 
        attribute_id and setting its value. The formatted message is then 
        printed and sent to the data sink.

        Args:
            msg (dict): The message to be processed, containing 'attribute_id' and other keys.
            value (any): The value to be associated with the message.
        """
        msg["attribute_id"]='output_'+msg.get("attribute_id")
        msg["value"]=value
        print(msg)
        self.data_sink.write(msg)

    def end(self):
        """
        Close the data sink connection.

        This method closes the connection to the data sink, ensuring that 
        all resources are released properly.
        """
        self.data_sink.close()
