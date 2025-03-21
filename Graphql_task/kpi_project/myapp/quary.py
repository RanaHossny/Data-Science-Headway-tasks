import graphene
from .fields import KPIType, AssetKPIType, SimulatorType
from .models import KPI, AssetKPI, Simulator


class Query(graphene.ObjectType):
    """
    GraphQL query class to fetch data related to KPIs, Asset KPIs, Asset Attributes, and Simulators.
    """
    all_kpis = graphene.List(KPIType)
    kpi_by_id = graphene.Field(KPIType, id=graphene.String()) 
    
    all_asset_kpis = graphene.List(AssetKPIType)
    asset_kpi_by_id = graphene.Field(AssetKPIType, id=graphene.Int())

    
    all_simulators = graphene.List(SimulatorType)
    simulator_by_id = graphene.Field(SimulatorType, id=graphene.Int())

    def resolve_all_kpis(self, info):
        """
        Resolver to get all KPIs.
        """
        return KPI.objects.all()

    def resolve_kpi_by_id(self, info, id):
        """
        Resolver to get a specific KPI by its ID.

        Args:
            id (str): The ID of the KPI.
        """
        return KPI.objects.get(id=id)

    def resolve_all_asset_kpis(self, info):
        """
        Resolver to get all Asset KPIs.
        """
        return AssetKPI.objects.all()

    def resolve_asset_kpi_by_id(self, info, id):
        """
        Resolver to get a specific Asset KPI by its ID.

        Args:
            id (int): The ID of the Asset KPI.
        """
        return AssetKPI.objects.get(id=id)


    def resolve_all_simulators(self, info):
        """
        Resolver to get all Simulators.
        """
        return Simulator.objects.all()

    def resolve_simulator_by_id(self, info, id):
        """
        Resolver to get a specific Simulator by its ID.

        Args:
            id (int): The ID of the Simulator.
        """
        return Simulator.objects.get(id=id)
