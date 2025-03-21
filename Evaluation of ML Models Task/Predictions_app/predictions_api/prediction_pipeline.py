import os
import pickle
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from .dataset_processing import DataPreprocessingPipeline
import pandas as pd
class ModelPredictionPipeline:
    def __init__(self, model_path):
        # Load the pre-trained model from the pickle file
        with open(model_path, 'rb') as file:
            model_data = pickle.load(file)
            self.model = model_data['model']  # Extract the model from the dictionary
        self.feature_pipeline = DataPreprocessingPipeline()

    def predict(self, X):
        # Preprocess features
        X_transformed = self.feature_pipeline.fit_transform(X)
        feature_names = (['Income', 'Own_Car', 'Own_Housing','Gender_Female','Gender_Male','Num_Children'])
        X_transformed=pd.DataFrame(X_transformed,columns=feature_names)
        # X_transformed=X_transformed[feature_names]

        # Make predictions using the pre-trained model
        return self.model.predict(X_transformed)
