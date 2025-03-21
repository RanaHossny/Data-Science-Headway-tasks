# prediction/serializers.py
from rest_framework import serializers

class PredictionRequestSerializer(serializers.Serializer):
    """
    Serializer to validate input data for predictions.
    Ensures that all list fields are of equal length and conform to the specified constraints.
    """
    
    # Field definitions with constraints on value choices
    Num_Children = serializers.ListField(
        child=serializers.IntegerField()
    )
    Gender = serializers.ListField(
        child=serializers.ChoiceField(choices=["Male", "Female"])
    )
    Income = serializers.ListField(
        child=serializers.FloatField()
    )
    Own_Car = serializers.ListField(
        child=serializers.ChoiceField(choices=["No", "Yes"])
    )
    Own_Housing = serializers.ListField(
        child=serializers.ChoiceField(choices=["No", "Yes"])
    )

    def validate(self, data):
        """
        Validates that all lists have the same length.
        
        Args:
            data (dict): Dictionary containing input lists for each field.
        
        Raises:
            serializers.ValidationError: If the lists have different lengths.
        
        Returns:
            dict: Validated data if all lists have the same length.
        """
        # Ensure all lists have the same length
        list_lengths = {len(value) for value in data.values()}
        if len(list_lengths) > 1:
            raise serializers.ValidationError("All lists must have the same length.")
        return data


class PredictionResponseSerializer(serializers.Serializer):
    """
    Serializer to format the response data for predictions.
    Contains a single list field 'prediction' for prediction outputs.
    """
    
    prediction = serializers.ListField(
        child=serializers.FloatField()
    )
