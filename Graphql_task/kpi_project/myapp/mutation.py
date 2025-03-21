import graphene
from .fields import KPIType,AssetKPIType,SimulatorType
from .models import KPI, AssetKPI, Simulator

class CreateKPI(graphene.Mutation):
    """
    Mutation to create a new KPI.
    Arguments:
        name (str): The name of the KPI.
        expression (str): The expression for the KPI.
        description (str): A description for the KPI.
    """
    kpi = graphene.Field(KPIType)

    class Arguments:
        name = graphene.String()
        expression = graphene.String()
        description = graphene.String()

    def mutate(self, info, name, expression, description=None):
        """
        Create and save a new KPI instance.

        Args:
            name (str): The name of the KPI.
            expression (str): The expression for the KPI.
            description (str, optional): A description for the KPI.
        """
        kpi = KPI(name=name, expression=expression, description=description)
        kpi.save()
        return CreateKPI(kpi=kpi)

class UpdateKPI(graphene.Mutation):
    """
    Mutation to update an existing KPI.

    Arguments:
        id (int): The ID of the KPI to update.
        name (str, optional): The new name for the KPI.
        expression (str, optional): The new expression for the KPI.
        description (str, optional): The new description for the KPI.
    """
    kpi = graphene.Field(KPIType)

    class Arguments:
        id = graphene.Int()
        name = graphene.String(required=False)  
        expression = graphene.String(required=False)  
        description = graphene.String(required=False)  

    def mutate(self, info, id, name=None, expression=None, description=None):
        """
        Update the fields of the existing KPI.

        Args:
            id (int): The ID of the KPI to update.
            name (str, optional): The new name for the KPI.
            expression (str, optional): The new expression for the KPI.
            description (str, optional): The new description for the KPI.
        """
        kpi = KPI.objects.get(id=id)

        # Update only the provided fields
        if name is not None:
            kpi.name = name
        if expression is not None:
            kpi.expression = expression
        if description is not None:
            kpi.description = description

        kpi.save()
        return UpdateKPI(kpi=kpi)

class DeleteKPI(graphene.Mutation):
    """
    Mutation to delete an existing KPI by its ID.

    Arguments:
        id (int): The ID of the KPI to delete.
    """
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        """
        Delete the KPI with the given ID.

        Args:
            id (int): The ID of the KPI to delete.
        """
        kpi = KPI.objects.get(id=id)
        kpi.delete()
        return DeleteKPI(success=True)

class CreateAssetKPI(graphene.Mutation):
    """
    Mutation to create a new Asset KPI.

    Arguments:
        asset_id (str): The ID of the asset.
        asset_value (str): The value associated with the asset.
        kpi_id (int): The ID of the KPI associated with the asset.
    """
    asset_kpi = graphene.Field(AssetKPIType)

    class Arguments:
        asset_id = graphene.String()
        asset_value = graphene.String()
        kpi_id = graphene.Int()

    def mutate(self, info, asset_id, asset_value, kpi_id):
        """
        Create and save a new Asset KPI.

        Args:
            asset_id (str): The ID of the asset.
            asset_value (str): The value associated with the asset.
            kpi_id (int): The ID of the KPI associated with the asset.
        """
        kpi = KPI.objects.get(id=kpi_id)
        asset_kpi = AssetKPI(asset_id=asset_id, asset_value=asset_value, kpi=kpi)
        asset_kpi.save()
        return CreateAssetKPI(asset_kpi=asset_kpi)

class UpdateAssetKPI(graphene.Mutation):
    """
    Mutation to update the asset value of an existing Asset KPI.

    Arguments:
        id (int): The ID of the Asset KPI to update.
        asset_value (str): The new value for the asset.
    """
    asset_kpi = graphene.Field(AssetKPIType)

    class Arguments:
        id = graphene.Int()
        asset_value = graphene.String()

    def mutate(self, info, id, asset_value):
        """
        Update the asset value for an existing Asset KPI.

        Args:
            id (int): The ID of the Asset KPI to update.
            asset_value (str): The new value for the asset.
        """
        asset_kpi = AssetKPI.objects.get(id=id)
        asset_kpi.asset_value = asset_value
        asset_kpi.save()
        return UpdateAssetKPI(asset_kpi=asset_kpi)

class DeleteAssetKPI(graphene.Mutation):
    """
    Mutation to delete an existing Asset KPI by its ID.

    Arguments:
        id (int): The ID of the Asset KPI to delete.
    """
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        """
        Delete the Asset KPI with the given ID.

        Args:
            id (int): The ID of the Asset KPI to delete.
        """
        asset_kpi = AssetKPI.objects.get(id=id)
        asset_kpi.delete()
        return DeleteAssetKPI(success=True)


class CreateSimulator(graphene.Mutation):
    """
    Mutation to create a new Simulator.

    Arguments:
        start_date (datetime): The start date of the simulator.
        interval (str): The interval for the simulator.
        kpi_id (int): The ID of the associated KPI.
    """
    simulator = graphene.Field(SimulatorType)

    class Arguments:
        start_date = graphene.DateTime()
        interval = graphene.String()
        kpi_id = graphene.Int()

    def mutate(self, info, start_date, interval, kpi_id):
        """
        Create and save a new Simulator.

        Args:
            start_date (datetime): The start date of the simulator.
            interval (str): The interval for the simulator.
            kpi_id (int): The ID of the associated KPI.
        """
        kpi = KPI.objects.get(id=kpi_id)
        simulator = Simulator(start_date=start_date, interval=interval, kpi_id=kpi)
        simulator.save()
        return CreateSimulator(simulator=simulator)

class UpdateSimulator(graphene.Mutation):
    """
    Mutation to update an existing Simulator.

    Arguments:
        id (int): The ID of the Simulator to update.
        start_date (datetime, optional): The new start date for the simulator.
        interval (str, optional): The new interval for the simulator.
        kpi_id (int, optional): The new KPI ID for the simulator.
    """
    simulator = graphene.Field(SimulatorType)

    class Arguments:
        id = graphene.Int()
        start_date = graphene.DateTime(required=False)
        interval = graphene.String(required=False)
        kpi_id = graphene.Int(required=False)

    def mutate(self, info, id, start_date=None, interval=None, kpi_id=None):
        """
        Update the fields of the existing Simulator.

        Args:
            id (int): The ID of the Simulator to update.
            start_date (datetime, optional): The new start date for the simulator.
            interval (str, optional): The new interval for the simulator.
            kpi_id (int, optional): The new KPI ID for the simulator.
        """
        simulator = Simulator.objects.get(id=id)

        # Update only the provided fields
        if start_date is not None:
            simulator.start_date = start_date
        if interval is not None:
            simulator.interval = interval
        if kpi_id is not None:
            simulator.kpi_id = KPI.objects.get(id=kpi_id)

        simulator.save()
        return UpdateSimulator(simulator=simulator)

class DeleteSimulator(graphene.Mutation):
    """
    Mutation to delete an existing Simulator by its ID.

    Arguments:
        id (int): The ID of the Simulator to delete.
    """
    success = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        """
        Delete the Simulator with the given ID.

        Args:
            id (int): The ID of the Simulator to delete.
        """
        simulator = Simulator.objects.get(id=id)
        simulator.delete()
        return DeleteSimulator(success=True)

class Mutation(graphene.ObjectType):
    """
    Root Mutation class for GraphQL API.

    This includes all mutations related to KPI, Asset KPI, Asset Attribute, and Simulator.
    """
    create_kpi = CreateKPI.Field()
    update_kpi = UpdateKPI.Field()
    delete_kpi = DeleteKPI.Field()

    create_asset_kpi = CreateAssetKPI.Field()
    update_asset_kpi = UpdateAssetKPI.Field()
    delete_asset_kpi = DeleteAssetKPI.Field()

    create_simulator = CreateSimulator.Field()
    update_simulator = UpdateSimulator.Field()
    delete_simulator = DeleteSimulator.Field()
