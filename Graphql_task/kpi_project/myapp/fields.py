from .models import KPI, AssetKPI, Simulator
from graphene_django.types import DjangoObjectType

class KPIType(DjangoObjectType):
    """
    GraphQL Type for the KPI model. This represents the data related to a Key Performance Indicator (KPI).

    Attributes:
        id (int): The unique identifier of the KPI.
        name (str): The name of the KPI.
        expression (str): The formula or expression used for the KPI.
        description (str): A description of the KPI (optional).
    """
    class Meta:
        model = KPI
        fields = ("id", "name", "expression", "description")

class AssetKPIType(DjangoObjectType):
    """
    GraphQL Type for the AssetKPI model. This represents the data related to a specific asset's KPI.

    Attributes:
        id (int): The unique identifier of the AssetKPI.
        asset_id (str): The identifier of the asset.
        asset_value (str): The value associated with the asset for this KPI.
        kpi (KPIType): The KPI associated with the asset.
        timestamp (datetime): The timestamp when the KPI value was recorded.
    """
    class Meta:
        model = AssetKPI
        fields = ("id", "asset_id", "asset_value", "kpi", "timestamp")

class SimulatorType(DjangoObjectType):
    """
    GraphQL Type for the Simulator model. This represents the data related to the simulator for KPIs.

    Attributes:
        id (int): The unique identifier of the Simulator.
        start_date (datetime): The start date of the simulation.
        interval (str): The interval at which the simulation runs.
        kpi_id (KPIType): The KPI associated with the simulator.
    """
    class Meta:
        model = Simulator
        fields = ("id", "start_date", "interval", "kpi_id")
