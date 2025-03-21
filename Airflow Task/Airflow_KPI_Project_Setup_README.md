# Airflow and KPI Project Setup

This README provides a step-by-step guide to set up your Airflow and KPI projects. Follow the instructions carefully to ensure proper configuration and operation.

## Prerequisites
- Install WSL (Windows Subsystem for Linux).
- Ensure you have Python 3 installed.
---

## Steps to Set Up

### 1. Mount Project Files
- Mount the files of your Airflow and KPI projects from their actual paths on Windows to WSL. For example:
  ```bash
  sudo mount --bind /mnt/c/path_to_kpi_project /path_in_wsl/kpi_project
  sudo mount --bind /mnt/c/path_to_airflow_project /path_in_wsl/airflow
  ```
- Navigate to the Airflow project directory in WSL and edit the `dags_folder` configuration in the Airflow settings to point to the mounted folder:
  ```bash
  nano ~/airflow/airflow.cfg
  ```
  Update the `dags_folder` entry to:
  ```
  dags_folder = /mnt/c/path_to_airflow/dags/path_in_wsl/airflow/dags
  ```

### 2. Create and Activate Airflow Environment
- In WSL, create a virtual environment for Airflow:
  ```bash
  python3 -m venv airflow-venv
  ```
- Activate the environment:
  ```bash
  source airflow-venv/bin/activate
  ```
- Install required Python packages:
  ```bash
  pip install apache-airflow django drf-yasg mysql-connector-python
  ```

### 3. Configure Airflow
- Initialize the Airflow database:
  ```bash
  airflow db init
  ```
- Create a user for the Airflow webserver:
  ```bash
  airflow users create     --username admin     --password admin     --firstname Admin     --lastname User     --role Admin     --email admin@example.com
  ```

### 4. Set Up the KPI Project
- Navigate to the KPI project directory.
- Run the following commands in the first terminal:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  python3 manage.py runserver 0.0.0.0:8000
  ```

### 5. Start Airflow Components
- In the second terminal, activate the environment and run the Airflow webserver:
  ```bash
  source airflow-venv/bin/activate
  airflow webserver --port 8080
  ```
- In the third terminal, activate the environment and start the Airflow scheduler:
  ```bash
  source airflow-venv/bin/activate
  airflow scheduler
  ```

### 6. Access Airflow and KPI Services
- Open Airflow in your browser at: [http://localhost:8080/home](http://localhost:8080/home)
- Verify that the DAGs are visible and operational.

---

## KPI Project API Endpoints

### 1. Simulators
- **POST** and **GET**: `http://localhost:8000/kpi/simulators/`
- Example payload for **POST**:
  ```json
  {
      "start_date": "2024-12-17T18:00:00Z",
      "interval": "hourly",
      "kpi_id": 1
  }
  ```

**Note**: Ensure you create a KPI first, as `kpi_id` is a foreign key in the Simulators table.

### 2. KPIs
- **POST** and **GET**: `http://localhost:8000/kpi/kpis/`
- Example payload for **POST**:
  ```json
  {
      "name": "KPI Name_3",
      "expression": "ATTR-1",
      "description": "Optional description"
  }
  ```

### 3. Link Asset
- **POST** and **GET**: `http://localhost:8000/kpi/link_asset/`
- Example payload for **POST**:
  ```json
  {
      "asset_id": "b5f8400f-cb29-48f0-bd3c-a2cc5350f44f",
      "kpi": 3,
      "timestamp": "2024-12-18T14:14:16.635834Z"
  }
  ```

**Note**: The `kpi` field is a foreign key in the Link Asset table.

---

## Additional Notes
- Always activate the virtual environment (`source airflow-venv/bin/activate`) in all terminals before running commands.
- Use separate terminals for running the Django server, Airflow webserver, and Airflow scheduler.
