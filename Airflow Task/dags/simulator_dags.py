import os
import random
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Set up Django environment
import django
import sys

sys.path.append('/mnt/d/Users/rana.hosny/Downloads/tasks/airflow task/sw part 2/kpi_project')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kpi_project.settings')
django.setup()

from kpi.models import Simulator, AssetKPI

def get_simulators():
    """
    Function to get all simulator instances using Django ORM.
    """
    return Simulator.objects.all()


def generate_random_value():
    """
    Function to generate a random value.
    """
    return random.randint(1, 100)


def interval_selection(interval):
    """
    Function interval_selection:Define a dictionary mapping interval types to their cron expressions
    
    """
    interval_map = {
        "daily": "0 0 * * *",    
        "hourly": "0 * * * *",   
        None: None               
    }
    
    return interval_map.get(interval, None) 


def generate_asset_link(kpi_id):
    """
    Function to create an AssetLink instance using Django ORM.
    """
    value = str(generate_random_value())
    AssetKPI.objects.create(kpi=kpi_id,asset_value=value)
    print(f"AssetKPI created for KPI {kpi_id} with value {value}")


def generate_dags():
    """
    Function to create DAGs dynamically for each simulator.
    """
    simulators = get_simulators()
    for simulator in simulators:
        sim_num=str(simulator.id)
        dag_id = f"Sim_{sim_num}_dag"
        start_date = simulator.start_date
        interval = simulator.interval
        schedule_interval = interval_selection(interval)
        with DAG(
            dag_id=dag_id,
            start_date=start_date,
            schedule=schedule_interval,
            catchup=False,
        ) as dag:
            PythonOperator(
                task_id='generate_asset_link_task',
                python_callable=generate_asset_link,
                op_args=[simulator.kpi_id],
            )


# Generate the DAGs
generate_dags()
