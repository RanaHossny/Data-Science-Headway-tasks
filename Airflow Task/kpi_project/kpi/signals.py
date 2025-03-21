from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from .models import AssetKPI, KPI
from .serializers import KPISerializer
from .sw.my_software.Software_Ingestor.Data_Ingestor_Proxy import Ingestor_Proxy

@receiver(post_save, sender=AssetKPI)
def handle_asset_kpi_creation(sender, instance, created, **kwargs):
    """
    Signal handle_asset_kpi_creation:

    Handles the creation of an AssetKPI by generating a random value, linking it to a KPI, 
    preparing filtered data, and using an Ingestor_Proxy to send the data to the ingestion system. 
    The function ensures that all necessary processes are logged for auditing and tracking purposes.
    """
    if not created:
        return  

    try:
        kpi = KPI.objects.get(id=instance.kpi.id)
        kpi_data = KPISerializer(kpi).data

        filtered_data = {
            "value": instance.asset_value ,
            "attribute_id": str(instance.asset_id),
        }

        print(f"Filtered Data Prepared: {filtered_data}")

        processing_engine_args = ['Json', [kpi_data.get('expression')]]
        ingestor_args = ['Json', [filtered_data]]
        data_sink_args = ['Raw']

        my_data_ingestor = Ingestor_Proxy(ingestor_args, processing_engine_args, data_sink_args)
        my_data_ingestor.send_msg()

    except KPI.DoesNotExist:
        print(f"KPI with ID {instance.kpi.id} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

