from django.shortcuts import render

# prediction/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from .serializers import PredictionInputSerializer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from lightgbm import LGBMClassifier
import pickle  # for loading the pre-trained model

##########################################################################################################################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Load your pre-trained models
try:
    model_path = os.path.join(BASE_DIR, 'prediction', 'final_model.pkl')
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)

    scaler_path = os.path.join(BASE_DIR, 'prediction', 'scaler.pkl')
    with open(scaler_path, 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    class_encoder_path = os.path.join(BASE_DIR, 'prediction', 'class_encoder.pkl')
    with open(class_encoder_path, 'rb') as encoder_file:
        class_encoder = pickle.load(encoder_file)
except FileNotFoundError as e:
    raise RuntimeError(f"Missing file: {e}")
except Exception as e:
    raise RuntimeError(f"Error loading models or scalers: {e}")
##########################################################################################################################

class PredictAPI(APIView):
    def post(self, request):
        serializer = PredictionInputSerializer(data=request.data)

        if serializer.is_valid():
            input_data = request.data  # Data should already be validated by the serializer
            response_data = {}

            try:
                for idx, features in input_data.items():
                    # Ensure input features are provided in a valid format
                    input_features = list(features.values())

                    # Scale the input features
                    scaled_features = scaler.transform([input_features])

                    # Predict probabilities
                    prediction_probs = model.predict_proba(scaled_features)

                    # Decode probabilities and class labels
                    decoded_probabilities = {
                        class_encoder.inverse_transform([i])[0]: prob
                        for i, prob in enumerate(prediction_probs[0])
                    }

                    # Add to response
                    response_data[idx] = decoded_probabilities

                return Response(response_data, status=status.HTTP_200_OK)

            except KeyError as e:
                return Response(
                    {"error": f"Key error in input data: {e}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except ValueError as e:
                return Response(
                    {"error": f"Value error during prediction: {e}"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Exception as e:
                return Response(
                    {"error": f"An unexpected error occurred: {e}"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
