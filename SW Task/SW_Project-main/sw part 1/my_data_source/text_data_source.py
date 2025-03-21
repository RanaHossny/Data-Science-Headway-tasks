"""
file text data source : to define the behavior of the text source
"""
import json
from my_data_source.data_source import DataSource
class TextDataSource(DataSource):
    """Text file data source implementation."""
    def __init__(self, file_path,json_format=True):
        self.file_path = file_path
        self.file = None
        self.current_position = 0  # To track the current line position
        self.json_format=json_format

    def connect(self):
        """Open the text file for reading."""
        self.file = open(self.file_path, 'r')
        print(f"Connected to the file: {self.file_path}")

    def fetch_data(self):
        """Fetch the next JSON message from the text file."""
        if self.file is None:
            raise ValueError("File not connected. Please call connect() first.")
        
        # Move the file pointer to the last read position
        self.file.seek(self.current_position)
        
        # Read the next line from the file
        line = self.file.readline()
        if not line:  # End of file reached
            self.close_connection()
            return None
        
        line = line.strip()  # Remove whitespace and newline characters
        
        if line:  # Check if the line is not empty
            try:
                if self.json_format:
                    line = json.loads(line)
                
                    # Update the position after successfully reading the line
                    self.current_position = self.file.tell()


                
                return line  # Return the single JSON message
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e} for line: {line}")
                return None  # Skip the problematic line
        return None  # If the line is empty

    def close_connection(self):
        """Close the connection to the text file."""
        if self.file:
            self.file.close()
            print(f"Connection to the file closed: {self.file_path}")
