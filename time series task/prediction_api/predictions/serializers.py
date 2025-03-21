# prediction/serializers.py
from rest_framework import serializers

class PredictionRequestSerializer(serializers.Serializer):
    dataset_id = serializers.IntegerField()
    values = serializers.ListField(
        child=serializers.DictField(
            child=serializers.CharField(allow_null=True)
        ),
        allow_empty=False  # Ensure that `values` list has at least one item
    )

        
    
    def validate_values(self, value):
        """
        Custom validation for 'values' field to ensure it contains time-value pairs
        and that 'value' can be a float or NaN.
        """
        for item in value:
            if 'time' not in item or 'value' not in item:
                raise serializers.ValidationError("Each item must contain 'time' and 'value'.")
            
            # Check if 'value' is either null or a valid float
            if item['value'] is not None:
                try:
                    float(item['value'])
                except ValueError:
                    raise serializers.ValidationError("'value' must be a float or null.")
        
        return value

class PredictionResponseSerializer(serializers.Serializer):
    prediction = serializers.FloatField()