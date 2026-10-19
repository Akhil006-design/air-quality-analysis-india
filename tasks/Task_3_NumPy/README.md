
# Task 3: NumPy — Air Quality Statistical Analysis

## 1. Project Overview

This project uses NumPy to perform statistical analysis on air-quality data collected from cities across India.

## 2. Objectives

- Calculate mean and median AQI.
- Calculate standard deviation.
- Find minimum and maximum AQI values.
- Calculate AQI percentiles.
- Compare AQI statistics across cities.
- Export results into CSV files.

## 3. Dataset

- File: city_day.csv
- Records: 29,531
- Columns: 16
- Data includes city names, dates, pollutant measurements, AQI, and AQI categories.

## 4. Technologies Used

- Python
- NumPy
- Pandas
- CSV files
- Antigravity

## 5. Methodology

1. Loaded the dataset using Pandas.
2. Selected valid AQI values and converted them into a NumPy array.
3. Calculated mean, median, standard deviation, minimum, and maximum.
4. Calculated the 25th, 50th, and 75th percentiles.
5. Calculated statistical summaries for individual cities.
6. Exported the results into CSV files.

## 6. Results

- Total dataset records: 29,531
- Valid AQI observations: 24,850
- Mean AQI: 166.46
- Median AQI: 118.00
- Standard deviation: 140.69
- Minimum AQI: 13
- Maximum AQI: 2,049
- Ahmedabad average AQI: 452.12
- Delhi average AQI: 259.49

These are historical dataset statistics, not current air-quality readings.

## 7. Output Files

The outputs folder contains:

- aqi_statistics.csv
- city_numpy_summary.csv
- aqi_percentiles.csv

## 8. Key Learnings

- Working with NumPy arrays.
- Calculating descriptive statistics.
- Understanding percentiles and standard deviation.
- Comparing numerical data across cities.
- Exporting analytical results using Pandas.

## 9. Limitations

The dataset contains missing AQI values, which are excluded from the calculations. The unusually high maximum AQI value should be validated before drawing conclusions. Standard deviation is calculated using NumPy's population standard deviation by default.

## 10. How to Run

Run the following command from the project root:

.\.venv\Scripts\python.exe tasks\Task_3_NumPy\task3_numpy.py

Ensure that the dataset exists at data/city_day.csv and that NumPy and Pandas are installed.
