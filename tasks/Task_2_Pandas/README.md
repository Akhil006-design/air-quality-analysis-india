# Task 2: Pandas — Air Quality Data Analysis

## 1. Project Overview
This project uses the Pandas Python library to analyze air-quality data collected from cities across India. It demonstrates how to load, inspect, filter, summarize, and export data using a real-world dataset.

## 2. Objective
- Load a CSV dataset using Pandas.
- Inspect dataset dimensions, column names, and data types.
- Identify missing values.
- Filter air-quality records for Delhi.
- Calculate average AQI for each city.
- Summarize AQI categories.
- Export analysis results into CSV files.

## 3. Dataset
**File:** `city_day.csv`

**Source:** [Air Quality Data in India — Kaggle](https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india)

The dataset contains 29,531 rows and 16 columns, including city, date, pollutant measurements, AQI, and AQI category.

## 4. Tools and Technologies
- Python
- Pandas
- CSV data files
- Visual Studio Code / Antigravity

## 5. Methodology
1. Loaded the dataset using `pd.read_csv()`.
2. Inspected the first five records, dimensions, columns, and data types.
3. Counted missing values in each column using `isnull().sum()`.
4. Converted AQI values to numeric format and standardized city names by removing surrounding whitespace.
5. Excluded records with missing city or AQI values from city-level AQI analysis.
6. Grouped records by city and calculated average AQI and valid record counts.
7. Filtered valid AQI records for Delhi.
8. Counted records in each AQI category.
9. Exported the results into CSV files.

## 6. Results
- Total records: 29,531
- Total columns: 16
- Ahmedabad average AQI: 452.12
- Delhi average AQI: 259.49
- Delhi minimum AQI: 29.00
- Delhi maximum AQI: 716.00
- Most frequent AQI category: Moderate, with 8,829 records
- Column with the most missing values: Xylene, with 18,109 missing values

These results are based on available records in the dataset. They do not represent current air-quality conditions.

## 7. Output Files
The program creates the following files inside the `outputs` directory:

- `city_summary.csv` — average AQI and valid record count by city.
- `missing_values_summary.csv` — missing-value count by column.
- `delhi_aqi_records.csv` — valid AQI records for Delhi.
- `aqi_category_summary.csv` — record count by AQI category.

## 8. Key Learnings
- Loading and inspecting datasets with Pandas.
- Understanding rows, columns, and data types.
- Identifying missing values.
- Filtering data using conditions.
- Grouping data and calculating aggregate statistics.
- Exporting analysis results to CSV files.

## 9. Limitations
The dataset contains missing values. City averages are calculated using available valid AQI observations, so the number of observations varies by city. The program reports missing values but does not impute missing pollutant measurements.

## 10. How to Run
Run the following command from the main project directory:

```powershell
.\.venv\Scripts\python.exe tasks\Task_2_Pandas\task2_pandas.py
```

The source dataset must be available at `data/city_day.csv`, and Pandas must be installed in the Python environment.
