# serializers.py
# This file defines serializers for the KPI and AssetKPI models.
# The serializers convert model instances to JSON format and validate data when creating or updating model instances.
# They are essential for API views, allowing data to be easily converted and validated.

from rest_framework import serializers
from .models import KPI, AssetKPI

class KPISerializer(serializers.ModelSerializer):
    """
    Serializer for the KPI model, handling conversion between model instances and JSON format.
    
    Fields:
        id (int): Unique identifier for the KPI instance.
        name (str): Name of the KPI.
        expression (str): Formula or regex associated with the KPI.
        description (str, optional): Description of the KPI.
    """
    class Meta:
        model = KPI
        fields = ['id', 'name', 'expression', 'description']  # Fields exposed in the API for KPI


class AssetKPISerializer(serializers.ModelSerializer):
    """
    Serializer for the AssetKPI model, handling conversion and validation.
    
    Fields:
        id (int): Unique identifier for the AssetKPI instance.
        asset_id (str): Identifier for the asset linked to the KPI.
        kpi (int): Foreign key to the KPI instance.
        timestamp (datetime): The timestamp when the asset-KPI association was created.
    """
    class Meta:
        model = AssetKPI
        fields = ['id', 'asset_id', 'kpi', 'timestamp']  # Fields exposed in the API for AssetKPI
