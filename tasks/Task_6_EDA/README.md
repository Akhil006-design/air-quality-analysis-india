\# Task 6: Exploratory Data Analysis (EDA)



\## Project

\*\*Air Quality Analysis — India\*\*



\## Objective

To explore air-quality data, assess data quality, identify city-wise and monthly AQI patterns, and examine relationships between AQI and pollutant measurements.



\## Dataset

\- \*\*File:\*\* `data/city\_day.csv`

\- \*\*Total records:\*\* 29,531

\- \*\*Columns:\*\* 16

\- \*\*Valid AQI observations:\*\* 24,850



\## Tools and Libraries

\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn



\## Analysis Performed

1\. Inspected dataset structure and column names.

2\. Measured missing values and their percentages.

3\. Checked for exact duplicate rows.

4\. Calculated overall AQI statistics.

5\. Compared average AQI across cities.

6\. Analyzed monthly AQI patterns.

7\. Calculated pollutant-to-AQI correlations.

8\. Flagged unusually high AQI observations using the IQR method.



\## Key Findings

\- The dataset contains 29,531 records, including 24,850 valid AQI observations.

\- The mean AQI is 166.46 and the median AQI is 118.

\- No exact duplicate rows were detected.

\- Xylene has the highest missing-data percentage at 61.32%.

\- Ahmedabad has the highest mean AQI among the cities in this dataset, at 452.12.

\- November has the highest monthly mean AQI at 241.68; July has the lowest at 111.85.

\- PM10 has the strongest positive correlation with AQI among the analyzed pollutants, at 0.803.

\- The maximum recorded AQI is 2049 and requires validation before interpretation.

\- The IQR method flagged 1,358 observations above its upper threshold. These observations were retained for investigation rather than automatically removed.



\## Output Files

All generated files are saved in the `outputs/` folder.



\- `missing\_values\_report.csv`

\- `duplicate\_report.csv`

\- `overall\_aqi\_statistics.csv`

\- `city\_aqi\_summary.csv`

\- `monthly\_aqi\_summary.csv`

\- `pollutant\_correlation\_matrix.csv`

\- `pollutant\_aqi\_correlations.csv`

\- `unusually\_high\_aqi\_records.csv`

\- `top\_10\_cities\_average\_aqi.png`

\- `monthly\_aqi\_trend.png`

\- `pollutant\_correlation\_heatmap.png`

\- `key\_findings.txt`



\## How to Run



From the project root directory, execute:



```powershell

.\\.venv\\Scripts\\python.exe .\\tasks\\Task\_6\_EDA\\task6\_eda.py

```



\## Limitations

\- Several columns contain missing observations.

\- Correlations show associations, not causation.

\- Monthly averages may be influenced by differences in cities, years, and available observations.

\- Extreme AQI observations should be validated before being excluded or interpreted.



\## Conclusion

This exploratory analysis identifies important patterns in the available air-quality records and highlights data-quality issues that should be considered in further analysis. The findings provide a foundation for the project's final report and recommendations.

