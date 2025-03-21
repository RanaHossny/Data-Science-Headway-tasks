### Report: Model Evaluation and Selection

#### Data Splitting:
The dataset was first split into **training + validation** (80%) and **test** (20%) sets. Then, the **train-validation** set was further split into **training** (80%) and **validation** (20%) sets. 

- **Training Set:** 256 samples
- **Validation Set:** 64 samples
- **Test Set:** 80 samples

#### Exploratory Data Analysis (EDA):
Upon examining the training data, the following findings were observed:

- **Missing Values:** There are no missing values (NaNs) in any of the columns.
- **Duplicates:** There are no duplicated rows in the dataset.
  
##### Class Distribution:
The class distribution for the target variable (after encoding) was found to be unbalanced:

- **Encoded y_train:**  
    - Class 5: 179 samples  
    - Class 3: 270 samples

- **Encoded y_test:**  
    - Class 2: 209 samples  
    - Class 3: 280 samples 

- **Class distribution in training dataset:**
  -XGBRegressor         118
  -HUBERREGRESSOR        51
  -LinearSVR             42
  -LASSO                 30
  -QUANTILEREGRESSOR     12
  -ELASTICNETCV           3

- **Class distribution in testing dataset:**
  -XGBRegressor         32
  -LinearSVR            18
  -HUBERREGRESSOR       17
  -LASSO                 8
  -QUANTILEREGRESSOR     3
  -ELASTICNETCV          2

- **Class distribution in validation dataset:**
  -XGBRegressor         27
  -HUBERREGRESSOR       17
  -LinearSVR             9
  -LASSO                 8
  -QUANTILEREGRESSOR     2
  -ELASTICNETCV          1

 
## **preprossing steps:**
  -Label encoding for target('class colounm')
  -stander scaler for x features 

##### Resampling:
The training data was resampled using SMOTE to balance the class distribution:
- **Resampled Class Distribution:**
  - Class 0: 150 samples  
  - Class 1: 150 samples  
  - Class 2: 150 samples  
  - Class 3: 150 samples  
  - Class 4: 150 samples  
  - Class 5: 150 samples  

This balanced class distribution was achieved through over-sampling, ensuring each class has an equal number of instances for model training.

#### Model Training:
Various classifiers were trained and evaluated, both before and after calibration. Below are the results of these models:

##### Performance Metrics:

| Classifier          | Model Accuracy | Precision Score  | Recall Score   | F1 Score        | Macro-average ROC AUC |
|---------------------|-----------------|------------------|----------------|------------------|-----------------------|
| **clf_log**          | 0.5125          | 0.4264           | 0.3956         | 0.4026           | 0.7942                |
| **clf_dt**           | 0.4375          | 0.3012           | 0.2722         | 0.2785           | 0.6625                |
| **clf_mlp**          | 0.6000          | 0.5489           | 0.4504         | 0.4683           | 0.8221                |
| **clf_gradientBoosting** | 0.5625      | 0.4784           | 0.4151         | 0.4288           | 0.8161                |
| **clf_gradientBoosting (2nd)** | 0.5375 | 0.4719         | 0.4065         | 0.4200           | 0.7640                |
| **clf_lightgbm**     | 0.6000          | 0.5110           | 0.3653         | 0.3473           | 0.8229                |
| **clf_adaboost**     | 0.5125          | 0.4589           | 0.3185         | 0.3018           | 0.8230                |
| **clf_rf**           | 0.5125          | 0.4741           | 0.3312         | 0.3150           | 0.8468                |


##### Calibrated Classifiers:
The classifiers were further calibrated using two approaches: **Platt Scaling** and **Isotonic Regression**. Below are the results for the calibrated models:

| Classifier                          | Model Accuracy | Precision Score | Recall Score | F1 Score | Macro-average ROC AUC | Average Calibration Error (Brier Score) |
|-------------------------------------|----------------|-----------------|--------------|----------|-----------------------|-----------------------------------------|
| **cal_clf_plat_log**                | 0.4875         | 0.8306          | 0.2491       | 0.1952   | 0.7626                | 0.1141                                  |
| **cal_clf_iso_log**                 | 0.5500         | 0.5998          | 0.3259       | 0.2958   | 0.7857                | 0.1158                                  |
| **cal_clf_plat_dt**                 | 0.4750         | 0.6591          | 0.2439       | 0.1915   | 0.6536                | 0.1349                                  |
| **cal_clf_iso_dt**                  | 0.4750         | 0.4955          | 0.2439       | 0.1940   | 0.6555                | 0.1267                                  |
| **cal_clf_plat_mp**                 | 0.5375         | 0.7858          | 0.3398       | 0.2899   | 0.8031                | 0.1144                                  |
| **cal_clf_iso_mp**                  | 0.6250         | 0.7454          | 0.4404       | 0.4448   | 0.7946                | 0.1142                                  |
| **cal_clf_plat_gradientBoosting**   | 0.5250         | 0.4006          | 0.3097       | 0.2610   | 0.7755                | 0.1217                                  |
| **cal_clf_iso_gradientBoosting**    | 0.5500         | 0.4302          | 0.3404       | 0.2914   | 0.8374                | 0.0884                                  |
| **cal_clf_plat_gradientBoosting (2nd)** | 0.5375      | 0.4780          | 0.3282       | 0.2901   | 0.8090                | 0.1128                                  |
| **cal_clf_iso_gradientBoosting (2nd)** | 0.5625      | 0.4854          | 0.3491       | 0.3148   | 0.7651                | 0.0713                                  |
| **cal_clf_plat_lightgbm**           | 0.5875         | 0.6558          | 0.3566       | 0.3293   | 0.7714                | 0.1143                                  |
| **cal_clf_iso_lightgbm**            | 0.5750         | 0.5274          | 0.3554       | 0.3355   | 0.7149                | 0.0706                                  |
| **cal_clf_plat_adaBoost**           | 0.6000         | 0.6099          | 0.3960       | 0.3505   | 0.7906                | 0.1126                                  |
| **cal_clf_iso_adaBoost**            | 0.5875         | 0.5706          | 0.3943       | 0.3600   | 0.8055                | 0.1178                                  |
| **cal_clf_plat_rf**                 | 0.5250         | 0.4608          | 0.3294       | 0.2873   | 0.8540                | 0.0989                                  |
| **cal_clf_iso_rf**                  | 0.5375         | 0.4590          | 0.3346       | 0.2956   | 0.8028                | 0.0890                                  |

#### Model Selection:
Based on the calibration error and model accuracy, **Isotonic Regression with LightGBM (cal_clf_iso_lightgbm)** was selected as the final model. This model has:
- **Accuracy:** 0.575
- **Lowest Calibration Error (Brier Score):** 0.0706
- **Comparable Accuracy** to the highest accuracy model (**AdaBoost with Platt Scaling**, accuracy = 0.600).

The choice of **cal_clf_iso_lightgbm** was made because it offers a balanced trade-off between model accuracy and the lowest calibration error, which is essential for ensuring reliable predictions.
