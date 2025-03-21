# prediction/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionRequestSerializer, PredictionResponseSerializer
from sklearn.linear_model import LogisticRegression
import os
from .prediction_pipeline import ModelPredictionPipeline
import pandas as pd
from sklearn.linear_model import Log
import numpy as np
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) 


class PredictionAPIView(APIView):
    def post(self, request):
        serializer = PredictionRequestSerializer(data=request.data)
        if serializer.is_valid():
            df = serializer.validated_data
            try:                
                df = pd.DataFrame(df)
                model_path = os.path.join(BASE_DIR, 'predictions_api', 'LogisticRegression_best_model.pkl')
                if not os.path.exists(model_path):
                    return Response({'error': 'Model file not found'}, status=status.HTTP_404_NOT_FOUND)
                feature_names = (['Income', 'Own_Car', 'Own_Housing','Gender','Num_Children'])
                df=df[feature_names]
                model_pipeline = ModelPredictionPipeline(model_path)
                predictions = model_pipeline.predict(df)      
                response_data = {'prediction': predictions} 
                response_serializer = PredictionResponseSerializer(response_data)

                return Response(response_serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
