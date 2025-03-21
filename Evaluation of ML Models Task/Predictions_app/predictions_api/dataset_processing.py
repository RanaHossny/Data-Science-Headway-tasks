from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import pandas as pd

class BooleanConverter(BaseEstimator, TransformerMixin):
    """Convert boolean columns ('Yes'/'No') to 1/0."""
    def __init__(self, columns=None):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        for col in self.columns:
            X[col] = X[col].map({'Yes': 1, 'No': 0})
        return X

class CustomMinMaxScaler(BaseEstimator, TransformerMixin):
    """Custom MinMaxScaler that scales data to a specified range."""
    def __init__(self):
        self.data_min = 30000
        self.data_max = 119999
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        # Scale data between 0 and 1 based on data min and max
        scaled_data = (X - self.data_min) / (self.data_max - self.data_min)
        # Scale to the custom range
        # custom_scaled_data = scaled_data * (self.max_val - self.min_val) + self.min_val
        return scaled_data

class DataPreprocessingPipeline:
    """Pipeline for feature preprocessing."""
    def __init__(self):
        self.pipeline = Pipeline(steps=[
            ('normalization', ColumnTransformer(transformers=[
                ('normalize_income', CustomMinMaxScaler(), ['Income']),
                ('convert_booleans', BooleanConverter(columns=['Own_Car', 'Own_Housing']), ['Own_Car', 'Own_Housing']),
                ('one_hot_gender', OneHotEncoder(), ['Gender'])  # Keep all categories for Gender
            ], remainder='passthrough'))
        ])
    
    def fit_transform(self, df):
        return self.pipeline.fit_transform(df)

class TargetPreprocessingPipeline:
    """Pipeline for target preprocessing."""
    def __init__(self):
        pass
    
    def fit_transform(self, y):
        return y.map({'Denied': 0, 'Approved': 1})

