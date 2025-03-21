
# KPI Project README

## Overview

This project implements a KPI management system using Django and REST framework, allowing users to manage KPIs and link assets to them.

## Setting Up the Project

1. **install those**:
```bash
pip install drf-yasg
pip install mysql-connector-python
```
2. **Database Migrations**: Before running the server, apply the database migrations to set up the necessary tables:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Run the Server**: Navigate to your project directory and execute:

   ```bash
   python manage.py runserver
   ```

4. **Run Tests**: To run the tests, use:

   ```bash
   python manage.py test
   ```

## API Documentation

The API is documented using Swagger, which can be accessed at:

- [Swagger Documentation](http://localhost:8000/swagger/)

### API Endpoints

1. **KPI List and Create**
   - **Method**: `GET`, `POST`, `DELETE`
   - **Endpoint**: `/kpi/kpis/`
   - **Description**: Retrieve all KPIs, create a new KPI, or delete an existing KPI.
   example:.
   
   
     {
        "name": "KPI Name_6",
        "expression": "ATTR+1-ATTR",
        "description": "Optional description"
    }

2. **Link Asset to KPI**
   - **Method**: `POST`
   - **Endpoint**: `/kpi/link_asset/`
   - **Description**: Link an asset to a KPI. The `asset_id` must exist in the DataFrame loaded from `example.txt`.

{
   "asset_id":"2",
   "kpi":5
}
## Available Assets

The assets information is stored in the `example.txt` file located in the `kpi` directory. 

# To run the project with an example like the part 1
 uncomment the following lines in the code(the values should be the same type if the 
equation.txt contain regex expression , so all assets should be string and when the equation is math expression 
all assets should be integer when doing this action ):

```python
# equation_path=os.path.join(os.getcwd(), "kpi\Equation.txt")
# processing_engine_args=['Text',equation_path,False]
# ingertor_args=[data_path,"Text"]
# data_sink_args=['Mysql','localhost','assets_db','root','Rana@1234']
# my_data_ingestor=Ingestor_Proxy(ingertor_args,processing_engine_args,data_sink_args)
# my_data_ingestor.send_msg()
```
### Video 

A video .
