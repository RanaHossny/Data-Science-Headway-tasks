# prediction/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionRequestSerializer, PredictionResponseSerializer
from .ml_model_loader import ML_Model_Loader
from .dataset_processing import Dataset_Processing
import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
import numpy as np
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 
from .dataset_processing import train_dataset_summary
# Define the list of keys
keys = [
    256, 185, 211, 115, 177, 110, 103, 287, 200, 242,
    272, 218, 165, 119, 212, 294, 198, 131, 246, 301,
    227, 188, 209, 118, 151, 153, 161, 310, 102, 386,
    43, 439, 348, 483, 29, 314, 66, 297, 290, 383,
    401, 440, 155, 176, 354, 469, 447, 335, 325, 12,
    507, 251, 482, 306, 9, 21, 74, 361, 321, 141,
    23, 506, 39, 338, 352, 367, 495, 205, 105, 204,
    300, 217, 446, 428, 79, 75, 391, 490, 370, 453,
    437, 491, 430, 499, 397, 435, 462, 451, 92, 429,
    505, 42, 465, 461, 498, 421
]

class PredictionAPIView(APIView):
    def post(self, request):
        serializer = PredictionRequestSerializer(data=request.data)
        if serializer.is_valid():
            dataset_id = serializer.validated_data['dataset_id']
            values = serializer.validated_data['values']

            try:
                # Check if dataset_id is in keys
                if dataset_id not in keys:
                    return Response({'error': 'dataset_id not found'}, status=status.HTTP_404_NOT_FOUND)

                
                # Process the incoming values
                df = pd.DataFrame(values)
                if 'anomaly' in df.columns:
                    df = df.drop(columns=['anomaly'])
                # Ensure 'time' is in datetime format
                df['time'] = pd.to_datetime(df['time'])
                df['value'] = pd.to_numeric(df['value'], errors='coerce')
                # Create new records based on the number of lags
                num_lags = train_dataset_summary[str(dataset_id)]['num_lags']
                data_processor = Dataset_Processing(df,dataset_id, 'value')  
                data_processor.data_processing()
                data_processor.extract_trend()
                processed_values = data_processor.df
                processed_values['trend']=processed_values['trend'].fillna(processed_values['trend'].mean())
                X_lagged = []
                X_lagged.append(processed_values)
                X_lagged = np.array(X_lagged)
                n_samples, n_lags, n_features = X_lagged.shape
                X_lagged = X_lagged.reshape(n_samples, n_lags * n_features) 
                # Load the model
                model_path = os.path.join(BASE_DIR, r'predictions\models', f"{dataset_id}_model.pkl")
                # Check if model path exists
                if not os.path.exists(model_path):
                    return Response({'error': 'Model file not found'}, status=status.HTTP_404_NOT_FOUND)
                
                model = ML_Model_Loader.load_model(model_path)  # Fixed string formatting
                # Make predictions
                prediction = model.predict(X_lagged)
                
                response_data = {'prediction': prediction}  # Convert prediction to list if necessary
                response_serializer = PredictionResponseSerializer(response_data)

                return Response(response_serializer.data, status=status.HTTP_200_OK)


            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
