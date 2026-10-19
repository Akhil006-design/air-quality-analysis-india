# Task 5: Seaborn — Advanced Data Visualization

## 1. Project Overview

This task uses Python's Seaborn library to explore air-quality measurements from an Indian city-level dataset. Statistical visualizations help examine relationships between pollutants, compare AQI distributions across cities, and explore the relationship between PM2.5 and AQI.

## 2. Objectives

- Create statistical visualizations using Seaborn.
- Explore correlations between AQI and pollutant measurements.
- Compare AQI distributions across selected cities.
- Examine the relationship between PM2.5 and AQI.
- Export charts and correlation values for reporting.

## 3. Tools and Libraries

- Python
- Pandas — data loading and preparation
- Seaborn — statistical visualizations
- Matplotlib — chart rendering
- pathlib — file path management

## 4. Dataset

**File:** `data/city_day.csv`

The dataset contains 29,531 rows and 16 columns. The script identified 24,850 records with valid AQI values.

Records with missing values in the variables required for each chart are excluded from that chart.

## 5. Methodology

1. Load the dataset using Pandas.
2. Remove rows with missing AQI for AQI-based analyses.
3. Calculate correlations between available numerical pollutant columns and AQI.
4. Create a heatmap to visualize the correlation matrix.
5. Select six cities with the highest mean AQI and compare their AQI distributions using a boxplot.
6. Create a scatterplot to examine PM2.5 measurements against AQI.
7. Save the charts as PNG files and export the correlation matrix as a CSV file.

## 6. Visualizations

### Chart 1: Pollutant Correlation Heatmap

Displays pairwise correlations between available pollutant measurements and AQI.

**Purpose:** To identify positive and negative statistical relationships between numerical variables.

### Chart 2: AQI Boxplot by City

Compares AQI distributions for the six cities with the highest mean recorded AQI.

**Purpose:** To examine medians, variation, and potential outliers.

### Chart 3: PM2.5 vs AQI Scatterplot

Displays paired PM2.5 and AQI measurements.

**Purpose:** To explore whether higher PM2.5 measurements tend to occur alongside higher AQI values.

## 7. Output Files

The outputs are saved in `tasks/Task_5_Seaborn/outputs/`.

- `pollutant_correlation_heatmap.png` — correlation heatmap
- `aqi_boxplot_by_city.png` — AQI distribution by city
- `pm25_vs_aqi_scatterplot.png` — PM2.5 versus AQI scatterplot
- `pollutant_correlation.csv` — numerical correlation matrix

## 8. Key Findings

- The dataset provides 24,850 valid AQI records.
- The heatmap can help identify variables that are statistically associated with AQI.
- The boxplot reveals differences in AQI medians, spread, and potential outliers across selected cities.
- The scatterplot helps assess the relationship between PM2.5 and AQI.

Specific correlation strengths and city comparisons should be reported only after inspecting the generated outputs.

## 9. Limitations

- Correlation does not establish causation.
- Missing pollutant measurements can reduce the number of observations used in individual comparisons.
- Extreme measurements may affect correlations and visual scaling.
- The selected cities are based on mean AQI in this dataset, which may not represent every period or all Indian cities.
- Results depend on the accuracy and coverage of the source dataset.

## 10. How to Run

From the project root directory, execute:

```powershell
.\.venv\Scripts\python.exe tasks\Task_5_Seaborn\task5_seaborn.py
```

The script recreates the charts and correlation CSV in the outputs folder.

## 11. Conclusion

This task demonstrates how Seaborn supports statistical exploration of air-quality data. The heatmap, boxplot, and scatterplot offer complementary views of pollutant relationships and AQI variation, helping communicate findings in an internship report or presentation.
