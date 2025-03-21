
# README

## the link of the end point:
http://127.0.0.1:8000/predict/predict/

## Data Preprocessing Instructions(any pkl will be found in pkl files)

(The endpoint performs these steps implicitly; you only need to send the response in the required format. You do not need to execute these steps when using the endpoint.)

### For Feature Scaling (`x_feature`):
To preprocess your features using a pre-fitted scaler:
```python
# Load the fitted scaler from the pickle file
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Use the loaded scaler to transform new data
X_test = scaler.transform(X_test)
```

### For Class Encoding (`class encoding`):
To preprocess your target variable using a pre-fitted encoder:
```python
# Load the fitted encoder from the pickle file
with open('class_encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

# Use the loaded encoder to transform target data
y_test = encoder.transform(y_test)
```

---
## Please the model expected the same order of the train cvs if you change the order , you will get error 


## Example Input and Expected Output

### Example Input:
```json
{
  "0": {
  "num_clients": 10,
  "sum_of_instances_in_clients": 13821,
  "max_of_instances_in_clients": 1383,
  "min_of_instances_in_clients": 1382,
  "stddev_of_instances_in_clients": 0.3,
  "average_dataset_missing_values_percent": 4.992465885,
  "min_dataset_missing_values_percent": 4.121475054,
  "max_dataset_missing_values_percent": 5.571635311,
  "stddev_dataset_missing_values_percent": 0.448969735,
  "average_target_missing_values_percent": 4.992465885,
  "min_target_missing_values_percent": 4.121475054,
  "max_target_missing_values_percent": 5.571635311,
  "stddev_target_missing_values_percent": 0.448969735,
  "no_of_features": 3,
  "no_of_numerical_features": 3,
  "no_of_categorical_features": 0,
  "sampling_rate": 0.166666667,
  "average_skewness_of_numerical_features": 0.072566663,
  "minimum_skewness_of_numerical_features": 1.13e-05,
  "maximum_skewness_of_numerical_features": 1.305305017,
  "stddev_skewness_of_numerical_features": 0.245613658,
  "average_kurtosis_of_numerical_features": 1.347356542,
  "minimum_kurtosis_of_numerical_features": 0.319057598,
  "maximum_kurtosis_of_numerical_features": 1.502076621,
  "stddev_kurtosis_of_numerical_features": 0.195271617,
  "avg_no_of_symbols_per_categorical_features": 0,
  "min_no_of_symbols_per_categorical_features": 0,
  "max_no_of_symbols_per_categorical_features": 0,
  "stddev_no_of_symbols_per_categorical_features": 0,
  "avg_no_of_stationary_features": 1,
  "min_no_of_stationary_features": 0,
  "max_no_of_stationary_features": 2,
  "stddev_no_of_stationary_features": 0.447213595,
  "avg_no_of_stationary_features_after_1st_order": 2.2,
  "min_no_of_stationary_features_after_1st_order": 1,
  "max_no_of_stationary_features_after_1st_order": 3,
  "stddev_no_of_stationary_features_after_1st_order": 0.6,
  "avg_no_of_stationary_features_after_2nd_order": 2.9,
  "min_no_of_stationary_features_after_2nd_order": 2,
  "max_no_of_stationary_features_after_2nd_order": 3,
  "stddev_no_of_stationary_features_after_2nd_order": 0.3,
  "avg_no_of_significant_lags_in_target": 0,
  "min_no_of_significant_lags_in_target": 0,
  "max_no_of_significant_lags_in_target": 0,
  "stddev_no_of_significant_lags_in_target": 0,
  "avg_no_of_insignificant_lags_in_target": 0,
  "max_no_of_insignificant_lags_in_target": 0,
  "min_no_of_insignificant_lags_in_target": 0,
  "stddev_no_of_insignificant_lags_in_target": 0,
  "avg_no_of_seasonality_components_in_target": 0,
  "max_no_of_seasonality_components_in_target": 2,
  "min_no_of_seasonality_components_in_target": 0,
  "stddev_no_of_seasonality_components_in_target": 0.009828662,
  "average_fractal_dimensionality_across_clients_of_target": 13,
  "maximum_period_of_seasonality_components_in_target_across_clients": 2,
  "minimum_period_of_seasonality_components_in_target_across_clients": 0.325082973,
  "entropy_of_target_stationarity": 0.673011667
},
  "1": {
  "num_clients": 10,
  "sum_of_instances_in_clients": 13821,
  "max_of_instances_in_clients": 1383,
  "min_of_instances_in_clients": 1382,
  "stddev_of_instances_in_clients": 0.3,
  "average_dataset_missing_values_percent": 4.992465885,
  "min_dataset_missing_values_percent": 4.121475054,
  "max_dataset_missing_values_percent": 5.571635311,
  "stddev_dataset_missing_values_percent": 0.448969735,
  "average_target_missing_values_percent": 4.992465885,
  "min_target_missing_values_percent": 4.121475054,
  "max_target_missing_values_percent": 5.571635311,
  "stddev_target_missing_values_percent": 0.448969735,
  "no_of_features": 3,
  "no_of_numerical_features": 3,
  "no_of_categorical_features": 0,
  "sampling_rate": 0.166666667,
  "average_skewness_of_numerical_features": 0.072566663,
  "minimum_skewness_of_numerical_features": 1.13e-05,
  "maximum_skewness_of_numerical_features": 1.305305017,
  "stddev_skewness_of_numerical_features": 0.245613658,
  "average_kurtosis_of_numerical_features": 1.347356542,
  "minimum_kurtosis_of_numerical_features": 0.319057598,
  "maximum_kurtosis_of_numerical_features": 1.502076621,
  "stddev_kurtosis_of_numerical_features": 0.195271617,
  "avg_no_of_symbols_per_categorical_features": 0,
  "min_no_of_symbols_per_categorical_features": 0,
  "max_no_of_symbols_per_categorical_features": 0,
  "stddev_no_of_symbols_per_categorical_features": 0,
  "avg_no_of_stationary_features": 1,
  "min_no_of_stationary_features": 0,
  "max_no_of_stationary_features": 2,
  "stddev_no_of_stationary_features": 0.447213595,
  "avg_no_of_stationary_features_after_1st_order": 2.2,
  "min_no_of_stationary_features_after_1st_order": 1,
  "max_no_of_stationary_features_after_1st_order": 3,
  "stddev_no_of_stationary_features_after_1st_order": 0.6,
  "avg_no_of_stationary_features_after_2nd_order": 2.9,
  "min_no_of_stationary_features_after_2nd_order": 2,
  "max_no_of_stationary_features_after_2nd_order": 3,
  "stddev_no_of_stationary_features_after_2nd_order": 0.3,
  "avg_no_of_significant_lags_in_target": 0,
  "min_no_of_significant_lags_in_target": 0,
  "max_no_of_significant_lags_in_target": 0,
  "stddev_no_of_significant_lags_in_target": 0,
  "avg_no_of_insignificant_lags_in_target": 0,
  "max_no_of_insignificant_lags_in_target": 0,
  "min_no_of_insignificant_lags_in_target": 0,
  "stddev_no_of_insignificant_lags_in_target": 0,
  "avg_no_of_seasonality_components_in_target": 0,
  "max_no_of_seasonality_components_in_target": 2,
  "min_no_of_seasonality_components_in_target": 0,
  "stddev_no_of_seasonality_components_in_target": 0.009828662,
  "average_fractal_dimensionality_across_clients_of_target": 13,
  "maximum_period_of_seasonality_components_in_target_across_clients": 2,
  "minimum_period_of_seasonality_components_in_target_across_clients": 0.325082973,
  "entropy_of_target_stationarity": 0.673011667
}
}
```

### Expected Output:
```json
{"0":{"ELASTICNETCV":0.0,"HUBERREGRESSOR":0.3133159268929504,"LASSO":0.0,"LinearSVR":0.14360313315926893,"QUANTILEREGRESSOR":0.02610966057441253,"XGBRegressor":0.5169712793733681},
"1":{"ELASTICNETCV":0.0,"HUBERREGRESSOR":0.3133159268929504,"LASSO":0.0,"LinearSVR":0.14360313315926893,"QUANTILEREGRESSOR":0.02610966057441253,"XGBRegressor":0.5169712793733681}}
```
