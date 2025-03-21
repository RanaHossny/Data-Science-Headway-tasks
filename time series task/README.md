
# Project Setup Instructions

## Prerequisites

### 1. Required Packages

Before running the project, you may need to install the following Python packages:

```bash
python=3.10
pip install pandas numpy statsmodels scikit-learn xgboost
```

### 2. Installing Django
If you don’t have Django installed, you can install it using the following command:

```bash
pip install django
```

## Project Structure

- The **`output_values`** file contains all the dataset IDs and the minimum required values to make predictions using the model.

## Running the Django Project

To start the Django server, follow these steps:

1. Navigate to the `prediction_api` folder, which contains the Django project.
2. Open a terminal in this directory.
3. Run the following command to start the server:

```bash
python manage.py runserver
```

Once the server is running, it will be available at `http://localhost:8000/`.

## Making Predictions

You can make predictions using Postman or any similar API testing tool.

### Steps:

1. Open Postman.
2. Create a new `POST` request.
3. Set the request URL to:

```
http://localhost:8000/api/predict/
```

4. In the **Body** section, choose `raw` and format the request as `JSON`.
5. Add the request body with values like this:

```json
{
  "dataset_id": 79,
  "values": [
    {
      "time": "2021-09-23T00:00:00",
      "value": 0.530501654
    },
    {
      "time": "2021-09-23T06:00:00",
      "value": 0.438768476
    },
    {
      "time": "2021-09-23T12:00:00",
      "value": -0.748895755
    },
    {
      "time": "2021-09-23T18:00:00",
      "value": 0.541129344
    },
    {
      "time": "2021-09-24T00:00:00",
      "value": -0.360695099
    }
  ]
}

```
can put null value too :
```json
{
  "dataset_id": 102,
  "values": [
    {"time": , "value": null},
    {"time": , "value": 50}
  ]
}
```

---

This README provides clear instructions for installing dependencies, running the Django project, and making predictions through an API request using Postman.
