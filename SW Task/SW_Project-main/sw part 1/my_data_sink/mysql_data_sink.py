"""
mysql data sink
"""
from my_data_sink.data_sink import DataSink
import mysql.connector

class MysqlDataSink(DataSink):
    def __init__(self,host,database,user,password):
        self.connection = None
        self.cursor = None
        self.host=host
        self.database=database
        self.user=user
        self.password=password
    def connect(self):
        """Connect to the MySQL database."""
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        """Create the assets_data table if it does not exist."""
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS assets_data (
            asset_id VARCHAR(255),
            attribute_id VARCHAR(255),
            timestamp VARCHAR(255),  -- Storing timestamp as string to keep original format
            value VARCHAR(255)
        );
        '''
        try:
            self.cursor.execute(create_table_query)
            print("Table 'assets_data' created successfully.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def write(self, data):
        """Insert data into the assets_data table."""
        insert_query = '''
        INSERT INTO assets_data (asset_id, attribute_id, timestamp, value)
        VALUES (%s, %s, %s, %s);
        '''
        values = (data['asset_id'], data['attribute_id'], data['timestamp'], data['value'])
        try:
            self.cursor.execute(insert_query, values)
            self.connection.commit()
            print("Data inserted successfully.")
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")

    def close(self):
        """Close the database connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("MySQL connection closed.")
