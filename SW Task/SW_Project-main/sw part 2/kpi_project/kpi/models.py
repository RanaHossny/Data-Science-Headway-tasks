# models.py
# This file defines the database models for the KPI and AssetKPI entities used in the Django application.
# The KPI model stores information about each KPI, including its name, formula, and description.
# The AssetKPI model links an asset to a specific KPI, along with a timestamp to record the association.

from django.db import models

class KPI(models.Model):
    """
    Represents a Key Performance Indicator (KPI) in the system.
    
    Attributes:
        name (str): Unique name of the KPI. It must be unique across all KPIs.
        expression (str): Formula or regex associated with this KPI.
        description (str, optional): Detailed description of the KPI's purpose.
    """
    name = models.CharField(max_length=255, unique=True)  # Added uniqueness constraint
    expression = models.TextField()  # This will store the formula or regex
    description = models.TextField(blank=True, null=True)  # Optional field

    def __str__(self):
        return self.name

class AssetKPI(models.Model):
    """
    Represents an association between an asset and a specific KPI.
    
    Attributes:
        asset_id (str): Unique identifier for the asset associated with the KPI.
        kpi (ForeignKey): Reference to the associated KPI, with cascading delete.
        timestamp (datetime): The time when the association was created, set automatically.
    """
    asset_id = models.CharField(max_length=255)
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, related_name='asset_kpis')  # Added related_name
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp

    def __str__(self):
        """Returns a formatted string with the asset ID and KPI name for easy identification."""
        return f"{self.asset_id} - {self.kpi.name}"


