"""
json data source which include the defination of the behaior of json data source type
"""
from .data_source import DataSource
class JsonDataSource(DataSource):
    """JSON data source implementation."""

    def __init__(self, json_msgs=None):
        if json_msgs is None:
            json_msgs = []  # Initialize with an empty list if no messages are provided
        self.json_msgs = json_msgs
        self.status = "disconnected"
        self.current_index = 0  # Index to track the current message being fetched

    def connect(self):
        """Simulate a connection to the JSON data source."""
        self.status = "connected"
        self.current_index = 0  # Reset index on connect
        print("Connected to JSON data source.")

    def fetch_data(self):
        """Fetch the next JSON message from the messages."""
        if self.status != "connected":
            print("Not connected to the data source.")
        # Check if there are more messages to fetch
        if self.current_index < len(self.json_msgs):
            message = self.json_msgs[self.current_index]
            self.current_index += 1  # Move to the next message
            print("Fetching data from JSON data source...")
            print(message)
            return message
        else:
            return None  # Return None if there are no more messages

    def close_connection(self):
        """Close the connection to the JSON data source."""
        self.status = "disconnected"
        self.current_index = 0  # Reset index on close
        print("Connection to JSON data source closed.")
