import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.deterministic import DeterministicProcess
import json
import os
import copy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
# Specify the JSON file path
json_file_path = os.path.join(BASE_DIR, 'predictions', 'train_datasets_summary.json')
with open(json_file_path, 'r') as json_file:
        train_dataset_summary = json.load(json_file)

class Dataset_Processing():
    def __init__(self, df, key_number, value_column_name):
        """
        Initialize the Dataset_Processing class with the given parameters.
        
        Parameters:
        df (pd.DataFrame): The DataFrame containing the dataset.
        key_number (int): Key or index associated with the dataset (used for missing value filling).
        value_column_name (str): The column name for the target variable (e.g., 'value').
        type (str): Dataset type, either 'train' or 'test'.
        """
        self.df = copy.deepcopy(df)  # Create a copy of the DataFrame to avoid modifying the original data
        self.value = value_column_name  # Name of the column containing target values
        self.key_number = key_number  # Key or index to identify the dataset

            


    def data_processing(self, lags=5, threshold=0.2):
        """
        Process the dataset by extracting time features, filling missing values, 
        selecting lags, adding lag features, and extracting Fourier features.

        Parameters:
        lags (int): Number of lags to consider when selecting lag features.
        threshold (float): Threshold for PACF values to determine the number of lags.
        """
        self.extract_time_features()  # Extract time-related features
        self.fill_missing_values(self.key_number)  # Fill missing values in the dataset
        num_lags = train_dataset_summary[str(self.key_number)]['num_lags']
        # self.add_leg_feature(num_lags)  # Add lag features based on the number of selected lags
        self.fill_missing_values(self.key_number)  # Refill missing values after adding lag features
        self.extract_fourier_features()  # Extract Fourier features


    def extract_time_features(self):
        """
        Converts the 'timestamp' column to datetime format, extracts date and time features,
        and sorts the DataFrame based on the 'timestamp' column.
        """
        self.df['time'] = pd.to_datetime(self.df['time'], errors='coerce')  # Convert timestamp to datetime
        self.df = self.df.sort_values(by='time')  # Sort by the 'timestamp' column

        # Extract various time-related features
        self.df['year'] = self.df['time'].dt.year
        self.df['month'] = self.df['time'].dt.month
        self.df['day'] = self.df['time'].dt.day
        self.df['dayofweek'] = self.df['time'].dt.dayofweek  # 0 = Monday, 6 = Sunday
        self.df['hour'] = self.df['time'].dt.hour
        self.df['minute'] = self.df['time'].dt.minute
        self.df['second'] = self.df['time'].dt.second

        # Drop the original 'timestamp' column
        self.df.drop(columns=['time'], inplace=True)


    def fill_missing_values(self, key):
        """
        Fill missing values in the 'value' column and lag columns.

        Parameters:
        key (int): Key or index of the dataset (used to match with the training set when filling test data).
        """
        # Forward fill to fill missing values in the 'value' column
        self.df['value'] = self.df['value'].ffill()

        num_lags = train_dataset_summary[str(self.key_number)]['num_lags']
        # For test data, fill missing values using the corresponding training data
        # self.df[leg_cols] = self.df[leg_cols].fillna(train_dataset_summary[str(self.key_number)]['mean_lags'])
        self.df['value'] = self.df['value'].fillna(self.df['value'].rolling(window=num_lags).mean()).fillna(0)


    def select_lags_pacf(self, lags, threshold):
        """
        Select the number of significant lags based on the PACF (Partial Autocorrelation Function).

        Parameters:
        lags (int): Number of lags to consider for PACF.
        threshold (float): Threshold for PACF values to select significant lags.

        Returns:
        int: The number of significant lags.
        """
        # Calculate PACF values for the target variable
        pacf_values = pacf(self.df[self.value], nlags=lags)

        # List to store significant lags based on PACF values
        significant_lags = []

        # Loop through PACF values and store the significant lags
        for i, val in enumerate(pacf_values):
            if val > threshold or (val < 0 and val < (-1 * threshold)):
                significant_lags.append(i)
            else:
                break  # Stop when the PACF value doesn't meet the threshold

        return len(significant_lags) - 1  # Return the number of significant lags


    def add_leg_feature(self, num_leg):
        """
        Add lag features to the dataset.

        Parameters:
        num_leg (int): Number of lag features to add.
        """
        for leg in range(num_leg):
            leg_name = 'Lag_' + str(leg + 1)  # Create a new column name for each lag
            self.df[leg_name] = self.df[self.value].shift(leg + 1)  # Add shifted values for lag


    def extract_fourier_features(self):
        """
        Extract Fourier transformation-based features for time-related periodicity.
        """
        # Fourier features for hour, day, and month periodicity using sine and cosine transformations
        self.df['fourier_hour_sin'] = np.sin(2 * np.pi * self.df['hour'] / 24)
        self.df['fourier_hour_cos'] = np.cos(2 * np.pi * self.df['hour'] / 24)

        self.df['fourier_day_sin'] = np.sin(2 * np.pi * self.df['dayofweek'] / 7)
        self.df['fourier_day_cos'] = np.cos(2 * np.pi * self.df['dayofweek'] / 7)

        self.df['fourier_month_sin'] = np.sin(2 * np.pi * self.df['month'] / 12)
        self.df['fourier_month_cos'] = np.cos(2 * np.pi * self.df['month'] / 12)


    def extract_trend(self, window_size=2):
        """
        Extract trend features from the time series using a moving average with a specified window size.

        Parameters:
        window_size (int): The window size for the moving average (default is 2).
        """
        # Calculate the moving average
        trend = self.df[self.value].rolling(window=window_size, min_periods=1).mean()

        # Add the trend as a new column in the DataFrame
        self.df['trend'] = trend

