import random
import json
import requests
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


BASE_URL = "http://localhost:8000/kpi/"

url = "http://localhost:8000/kpi/link_asset/"  



def get_instances(type):
    """
    Function get_instances:Function to send GET request to instances from django models
    input parmaters:
    type: the model name 
    output parmaters:
    list of the wanted model instances
    """
    url = f"{BASE_URL}{type}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        print("instances retrieved successfully:")
        instances = response.json()  # Parse the JSON response
        print(json.dumps(instances, indent=2))
        return instances
    else:
        print(f"Failed to retrieve instances. Status code: {response.status_code}")
        return []

def generate_random_value():
    """
    Function generate_random_value:to generate a random value
    output parmeters:
    a randm integer value
    
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

def  generate_asset_link(id):
    """
    Function generate_asset_link:Used to create instance of asset_link model 
    
    """
    value =str(generate_random_value())
    data = {
        "kpi":id,
        "asset_value":f"{value}"
        }
    #Send the POST request
    response = requests.post(url, json=data)
    # Check the response
    if response.status_code == 200 or response.status_code == 201:
        print("Success:", response.json())
    else:
        print("Failed:", response.status_code, response.text)




def generate_dags():
    """
    Function generate_dags : used to create DAGS dynamically
    """
    global simulator
    simulators = get_instances('simulators')
    # Create the DAGs for each simulator
    for simulator_data in simulators:
        simulator=simulator_data
        dag_id = f"Sim_{simulator_data['kpi_id']}_dag"
        start_date = simulator_data['start_date']
        interval = simulator_data['interval']
        start_date = datetime.fromisoformat(start_date) 
        schedule_interval = interval_selection(interval)
        with DAG(dag_id=dag_id, start_date=start_date, schedule=schedule_interval,catchup=False) as dag:
            python_task = PythonOperator(
            task_id='my_task',
            python_callable=generate_asset_link,
            op_args=[simulator_data['kpi_id']]
            )


# Call this function to generate and save DAGs for all simulators
generate_dags()
