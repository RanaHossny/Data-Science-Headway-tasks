from rest_framework import serializers
class PredictionFeatureSerializer(serializers.Serializer):
    num_clients = serializers.IntegerField()
    sum_of_instances_in_clients = serializers.IntegerField()
    max_of_instances_in_clients = serializers.IntegerField()
    min_of_instances_in_clients = serializers.IntegerField()
    stddev_of_instances_in_clients = serializers.FloatField()
    average_dataset_missing_values_percent = serializers.FloatField()
    min_dataset_missing_values_percent = serializers.FloatField()
    max_dataset_missing_values_percent = serializers.FloatField()
    stddev_dataset_missing_values_percent = serializers.FloatField()
    average_target_missing_values_percent = serializers.FloatField()
    min_target_missing_values_percent = serializers.FloatField()
    max_target_missing_values_percent = serializers.FloatField()
    stddev_target_missing_values_percent = serializers.FloatField()
    no_of_features = serializers.IntegerField()
    no_of_numerical_features = serializers.IntegerField()
    no_of_categorical_features = serializers.IntegerField()
    sampling_rate = serializers.FloatField()
    average_skewness_of_numerical_features = serializers.FloatField()
    minimum_skewness_of_numerical_features = serializers.FloatField()
    maximum_skewness_of_numerical_features = serializers.FloatField()
    stddev_skewness_of_numerical_features = serializers.FloatField()
    average_kurtosis_of_numerical_features = serializers.FloatField()
    minimum_kurtosis_of_numerical_features = serializers.FloatField()
    maximum_kurtosis_of_numerical_features = serializers.FloatField()
    stddev_kurtosis_of_numerical_features = serializers.FloatField()
    avg_no_of_symbols_per_categorical_features = serializers.FloatField()
    min_no_of_symbols_per_categorical_features = serializers.FloatField()
    max_no_of_symbols_per_categorical_features = serializers.FloatField()
    stddev_no_of_symbols_per_categorical_features = serializers.FloatField()
    avg_no_of_stationary_features = serializers.FloatField()
    min_no_of_stationary_features = serializers.FloatField()
    max_no_of_stationary_features = serializers.FloatField()
    stddev_no_of_stationary_features = serializers.FloatField()
    avg_no_of_stationary_features_after_1st_order = serializers.FloatField()
    min_no_of_stationary_features_after_1st_order = serializers.FloatField()
    max_no_of_stationary_features_after_1st_order = serializers.FloatField()
    stddev_no_of_stationary_features_after_1st_order = serializers.FloatField()
    avg_no_of_stationary_features_after_2nd_order = serializers.FloatField()
    min_no_of_stationary_features_after_2nd_order = serializers.FloatField()
    max_no_of_stationary_features_after_2nd_order = serializers.FloatField()
    stddev_no_of_stationary_features_after_2nd_order = serializers.FloatField()
    avg_no_of_significant_lags_in_target = serializers.FloatField()
    min_no_of_significant_lags_in_target = serializers.FloatField()
    max_no_of_significant_lags_in_target = serializers.FloatField()
    stddev_no_of_significant_lags_in_target = serializers.FloatField()
    avg_no_of_insignificant_lags_in_target = serializers.FloatField()
    max_no_of_insignificant_lags_in_target = serializers.FloatField()
    min_no_of_insignificant_lags_in_target = serializers.FloatField()
    stddev_no_of_insignificant_lags_in_target = serializers.FloatField()
    avg_no_of_seasonality_components_in_target = serializers.FloatField()
    max_no_of_seasonality_components_in_target = serializers.FloatField()
    min_no_of_seasonality_components_in_target = serializers.FloatField()
    stddev_no_of_seasonality_components_in_target = serializers.FloatField()
    average_fractal_dimensionality_across_clients_of_target = serializers.FloatField()
    maximum_period_of_seasonality_components_in_target_across_clients = serializers.FloatField()
    minimum_period_of_seasonality_components_in_target_across_clients = serializers.FloatField()
    entropy_of_target_stationarity = serializers.FloatField()

    class Meta:
        # Custom ordering for the fields
        fields = [
            'num_clients', 'sum_of_instances_in_clients', 'max_of_instances_in_clients', 
            'min_of_instances_in_clients', 'stddev_of_instances_in_clients', 
            'average_dataset_missing_values_percent', 'min_dataset_missing_values_percent', 
            'max_dataset_missing_values_percent', 'stddev_dataset_missing_values_percent', 
            'average_target_missing_values_percent', 'min_target_missing_values_percent', 
            'max_target_missing_values_percent', 'stddev_target_missing_values_percent', 
            'no_of_features', 'no_of_numerical_features', 'no_of_categorical_features', 
            'sampling_rate', 'average_skewness_of_numerical_features', 
            'minimum_skewness_of_numerical_features', 'maximum_skewness_of_numerical_features', 
            'stddev_skewness_of_numerical_features', 'average_kurtosis_of_numerical_features', 
            'minimum_kurtosis_of_numerical_features', 'maximum_kurtosis_of_numerical_features', 
            'stddev_kurtosis_of_numerical_features', 'avg_no_of_symbols_per_categorical_features', 
            'min_no_of_symbols_per_categorical_features', 
            'max_no_of_symbols_per_categorical_features', 
            'stddev_no_of_symbols_per_categorical_features', 'avg_no_of_stationary_features', 
            'min_no_of_stationary_features', 'max_no_of_stationary_features', 
            'stddev_no_of_stationary_features', 'avg_no_of_stationary_features_after_1st_order', 
            'min_no_of_stationary_features_after_1st_order', 
            'max_no_of_stationary_features_after_1st_order', 
            'stddev_no_of_stationary_features_after_1st_order', 
            'avg_no_of_stationary_features_after_2nd_order', 
            'min_no_of_stationary_features_after_2nd_order', 
            'max_no_of_stationary_features_after_2nd_order', 
            'stddev_no_of_stationary_features_after_2nd_order', 
            'avg_no_of_significant_lags_in_target', 'min_no_of_significant_lags_in_target', 
            'max_no_of_significant_lags_in_target', 'stddev_no_of_significant_lags_in_target', 
            'avg_no_of_insignificant_lags_in_target', 
            'max_no_of_insignificant_lags_in_target', 'min_no_of_insignificant_lags_in_target', 
            'stddev_no_of_insignificant_lags_in_target', 
            'avg_no_of_seasonality_components_in_target', 
            'max_no_of_seasonality_components_in_target', 
            'min_no_of_seasonality_components_in_target', 
            'stddev_no_of_seasonality_components_in_target', 
            'average_fractal_dimensionality_across_clients_of_target', 
            'maximum_period_of_seasonality_components_in_target_across_clients', 
            'minimum_period_of_seasonality_components_in_target_across_clients', 
            'entropy_of_target_stationarity'
        ]

class PredictionInputSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        if not isinstance(data, dict):
            raise serializers.ValidationError("Input must be a dictionary of instances.")

        validated_data = {}
        for key, value in data.items():
            try:
                feature_data = PredictionFeatureSerializer(data=value)
                feature_data.is_valid(raise_exception=True)
                validated_data[key] = feature_data.validated_data
            except serializers.ValidationError as e:
                raise serializers.ValidationError({key: e.detail})

        return validated_data
