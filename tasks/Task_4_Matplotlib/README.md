# Task 4: Matplotlib — Air Quality Data Visualization

## 1. Project Overview

This task uses Python's Matplotlib library to visualize air quality data from the Indian city-level air quality dataset. The visualizations help identify differences in average Air Quality Index (AQI), observe Delhi's AQI over time, and understand the distribution of AQI measurements.

## 2. Objectives

- Create clear and informative charts using Matplotlib.
- Compare average AQI values across cities.
- Visualize Delhi's AQI over time.
- Examine the distribution of valid AQI observations.
- Export charts and summary data for reports and presentations.

## 3. Tools and Libraries

- Python
- Pandas — data loading and preparation
- Matplotlib — chart creation
- NumPy — available for numerical analysis, although not directly required by the current script
- pathlib — file path management

## 4. Dataset

**File:** `data/city_day.csv`

The dataset contains 29,531 rows and 16 columns. The script identified 24,850 records with valid AQI values.

Rows without AQI measurements were excluded from the visualizations.

## 5. Methodology

1. Load the dataset using Pandas.
2. Convert the Date column into a date format.
3. Exclude records with missing AQI values.
4. Calculate average AQI for each city.
5. Select the 10 cities with the highest average AQI.
6. Plot Delhi's valid AQI observations in chronological order.
7. Create a histogram showing the distribution of AQI observations.
8. Save the charts as high-resolution PNG images and export the city-average summary as a CSV file.

## 6. Visualizations

### Chart 1: Average AQI by City

A horizontal bar chart comparing the 10 cities with the highest average AQI in the dataset.

**Purpose:** To compare average recorded AQI levels across cities.

### Chart 2: Delhi AQI Over Time

A line chart displaying Delhi's valid AQI observations in date order.

**Purpose:** To observe changes and fluctuations in Delhi's recorded AQI.

### Chart 3: AQI Distribution

A histogram showing the distribution of valid AQI observations.

**Purpose:** To understand how AQI values are distributed across the dataset.

## 7. Output Files

The generated files are stored in `tasks/Task_4_Matplotlib/outputs/`.

- `average_aqi_by_city.png` — horizontal bar chart
- `delhi_aqi_over_time.png` — time-series line chart
- `aqi_distribution.png` — AQI histogram
- `average_aqi_by_city.csv` — city-average AQI summary

## 8. Key Findings

- The dataset contains 29,531 rows, of which 24,850 have valid AQI values.
- The city-average chart highlights cities with the highest mean recorded AQI.
- The Delhi time-series chart provides a view of AQI variation across recorded dates.
- The histogram reveals the distribution and spread of AQI observations.

Exact city rankings and numerical findings should be interpreted alongside the generated charts and the underlying dataset.

## 9. Limitations

- Missing AQI values are excluded, so the charts represent only available AQI observations.
- The dataset may contain unusually high AQI values that require validation.
- Recorded values and dates depend on the coverage and quality of the source dataset.
- These charts describe the available data and do not establish the causes of air pollution.

## 10. How to Run

From the root directory of the project, run:

```powershell
.\.venv\Scripts\python.exe tasks\Task_4_Matplotlib\task4_matplotlib.py
```

The script recreates the visualizations in the `outputs` folder.

## 11. Conclusion

This task demonstrates how Matplotlib can turn air quality measurements into visual insights. The charts support city-level comparisons, time-series exploration, and distribution analysis, making the results easier to interpret and communicate in an internship report or presentation.
