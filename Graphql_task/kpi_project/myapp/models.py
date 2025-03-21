
from django.db import models
import uuid

def generate_unique_asset_id():
    return f"ASSET-{uuid.uuid4().hex[:8].upper()}"

class KPI(models.Model):
    """
    Represents a Key Performance Indicator (KPI) in the system.
    
    Attributes:
        name (str): Unique name of the KPI. It must be unique across all KPIs.
        expression (str): Formula or regex associated with this KPI.
        description (str, optional): Detailed description of the KPI's purpose.
    """
    name = models.CharField(max_length=255, unique=True)  
    expression = models.TextField()  
    description = models.TextField(blank=True, null=True) 

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
    asset_id = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    asset_value=models.CharField(max_length=10)
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, related_name='asset_kpis')  
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        """Returns a formatted string with the asset ID and KPI name for easy identification."""
        return f"{self.asset_id} - {self.kpi.name}"
    


class Simulator(models.Model):
    """
    Model representing a simulation of a KPI over a period.

    Attributes:
        start_date (datetime): The start date of the simulation.
        interval (str): The interval for the simulation (e.g., daily, monthly).
        kpi_id (ForeignKey): The KPI related to this simulation.
    """
    start_date = models.DateTimeField()
    interval = models.CharField(max_length=255) 
    kpi_id = models.ForeignKey(KPI, on_delete=models.CASCADE) 

    def __str__(self):
        """
        String representation of the Simulator instance.

        Returns:
            str: A formatted string showing the associated KPI and the simulation start date.
        """
        return f"Simulator {self.kpi_id} starting at {self.start_date}"



