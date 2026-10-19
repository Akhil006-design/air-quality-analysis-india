# Week 4 — Machine Learning: Linear Regression

## Project Overview
This project implements a simple Linear Regression model to explore the relationship between PM2.5 concentration and the Air Quality Index (AQI) using India's city-level air-quality dataset.

## Objective
- Understand the basic workflow of supervised machine learning.
- Prepare input features and a target variable.
- Split the dataset into training and testing sets.
- Train a Linear Regression model using Scikit-learn.
- Evaluate predictions using standard regression metrics.

## Dataset
- **File:** `data/city_day.csv`
- **Input feature:** PM2.5
- **Target variable:** AQI
- **Usable records:** 24,172 after removing rows with missing PM2.5 or AQI values.

## Methodology
1. Loaded the dataset using Pandas.
2. Selected the PM2.5 and AQI columns.
3. Removed records with missing values in these columns.
4. Split the data into 80% training and 20% testing sets using `train_test_split`.
5. Trained a `LinearRegression` model.
6. Evaluated predictions using MAE, MSE, and R-squared.

## Results

| Metric | Result |
|---|---:|
| Total usable records | 24,172 |
| Training records | 19,337 |
| Testing records | 4,835 |
| Mean Absolute Error (MAE) | 48.21 |
| Mean Squared Error (MSE) | 9,283.45 |
| R-squared (R²) | 0.485 |
| Model coefficient | 1.47 |
| Model intercept | 68.461 |

## Interpretation
The model achieved an R² score of 0.485 on the test set, meaning it explains approximately 48.5% of the variation in the observed AQI values. The MAE of 48.21 indicates an average absolute prediction error of about 48 AQI points.

These results provide a baseline for predicting AQI from PM2.5 alone. The model does not capture all factors that influence air quality, and its predictions should not be treated as official AQI measurements.

## Limitations
- Only PM2.5 is used as an input feature.
- The model assumes a linear relationship between PM2.5 and AQI.
- Missing values in the selected columns are excluded.
- The model has not been validated for future dates or unseen cities.
- Correlation does not establish causation.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Linear Regression
- Train/test split
- Regression evaluation metrics

## How to Run
Run the following command from the repository's root directory:

```powershell
.\.venv\Scripts\python.exe tasks\Week_4_Machine_Learning\linear_regression.py
```

## Conclusion
This exercise demonstrates a basic machine-learning workflow, from data preparation and train/test splitting to model training and evaluation. Future improvements could include testing additional pollutant features and comparing different regression models.
