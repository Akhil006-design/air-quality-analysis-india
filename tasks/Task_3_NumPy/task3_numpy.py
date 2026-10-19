
from pathlib import Path
import pandas as pd
import numpy as np

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "city_day.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 50)
print("TASK 3: NUMPY - AIR QUALITY STATISTICS")
print("=" * 50)

# 1. Load the dataset
df = pd.read_csv(DATA_FILE)

print("\n1. DATASET INFORMATION")
print("-" * 30)
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])

# 2. Select valid AQI values
aqi = pd.to_numeric(df["AQI"], errors="coerce").dropna().to_numpy()

if len(aqi) == 0:
    raise ValueError("No valid AQI values found in the dataset.")

# 3. Calculate statistics using NumPy
statistics = {
    "Statistic": [
        "Count",
        "Mean AQI",
        "Median AQI",
        "Standard Deviation",
        "Minimum AQI",
        "Maximum AQI",
        "25th Percentile",
        "50th Percentile",
        "75th Percentile"
    ],
    "Value": [
        len(aqi),
        np.mean(aqi),
        np.median(aqi),
        np.std(aqi),
        np.min(aqi),
        np.max(aqi),
        np.percentile(aqi, 25),
        np.percentile(aqi, 50),
        np.percentile(aqi, 75)
    ]
}

statistics_df = pd.DataFrame(statistics)

print("\n2. AQI STATISTICAL ANALYSIS")
print("-" * 30)
print(statistics_df.to_string(index=False))

# 4. Calculate statistics for each city
city_results = []

for city in sorted(df["City"].dropna().unique()):
    city_aqi = pd.to_numeric(
        df.loc[df["City"] == city, "AQI"],
        errors="coerce"
    ).dropna().to_numpy()

    if len(city_aqi) > 0:
        city_results.append({
            "City": city,
            "Valid_Records": len(city_aqi),
            "Mean_AQI": np.mean(city_aqi),
            "Median_AQI": np.median(city_aqi),
            "Std_Deviation": np.std(city_aqi),
            "Minimum_AQI": np.min(city_aqi),
            "Maximum_AQI": np.max(city_aqi)
        })

city_summary = pd.DataFrame(city_results)
city_summary = city_summary.sort_values(
    by="Mean_AQI", ascending=False
)

print("\n3. TOP 10 CITIES BY MEAN AQI")
print("-" * 30)
print(city_summary.head(10).round(2).to_string(index=False))

# 5. Save results
statistics_df.to_csv(
    OUTPUT_DIR / "aqi_statistics.csv", index=False
)

city_summary.to_csv(
    OUTPUT_DIR / "city_numpy_summary.csv", index=False
)

# 6. Save percentile summary
percentile_df = pd.DataFrame({
    "Percentile": ["25th", "50th", "75th", "90th", "95th"],
    "AQI_Value": [
        np.percentile(aqi, 25),
        np.percentile(aqi, 50),
        np.percentile(aqi, 75),
        np.percentile(aqi, 90),
        np.percentile(aqi, 95)
    ]
})

percentile_df.to_csv(
    OUTPUT_DIR / "aqi_percentiles.csv", index=False
)

print("\n4. OUTPUT FILES")
print("-" * 30)
print("aqi_statistics.csv")
print("city_numpy_summary.csv")
print("aqi_percentiles.csv")

print("\n" + "=" * 50)
print("TASK 3 NUMPY ANALYSIS COMPLETED SUCCESSFULLY!")
print("Output folder:", OUTPUT_DIR)
print("=" * 50)
