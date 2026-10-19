
from pathlib import Path
import pandas as pd

# Project paths
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_ROOT / "data" / "city_day.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

print("=" * 50)
print("TASK 2: PANDAS - AIR QUALITY DATA ANALYSIS")
print("=" * 50)

# 1. Load the dataset
df = pd.read_csv(DATA_FILE)

print("\n1. DATASET INFORMATION")
print("-" * 30)
print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("\nFirst five records:")
print(df.head())

# 2. Inspect column names and data types
print("\n2. COLUMN NAMES")
print("-" * 30)
print(df.columns.tolist())

print("\n3. DATA TYPES")
print("-" * 30)
print(df.dtypes)

# 3. Check missing values
print("\n4. MISSING VALUES")
print("-" * 30)
missing_values = df.isnull().sum()
print(missing_values)

missing_summary = missing_values.reset_index()
missing_summary.columns = ["Column", "Missing_Values"]
missing_summary.to_csv(
    OUTPUT_DIR / "missing_values_summary.csv",
    index=False
)

# 4. Clean data for AQI analysis
df["AQI"] = pd.to_numeric(df["AQI"], errors="coerce")
df["City"] = df["City"].astype("string").str.strip()

valid_aqi = df.dropna(subset=["City", "AQI"]).copy()
valid_aqi = valid_aqi[valid_aqi["City"] != ""]

# 5. Calculate average AQI for each city
city_summary = (
    valid_aqi.groupby("City", as_index=False)
    .agg(
        Average_AQI=("AQI", "mean"),
        Records=("AQI", "count")
    )
    .sort_values("Average_AQI", ascending=False)
)

city_summary["Average_AQI"] = city_summary["Average_AQI"].round(2)

city_summary.to_csv(
    OUTPUT_DIR / "city_summary.csv",
    index=False
)

print("\n5. TOP 10 CITIES BY AVERAGE AQI")
print("-" * 30)
print(city_summary.head(10).to_string(index=False))

# 6. Filter records for Delhi
delhi_data = valid_aqi[valid_aqi["City"].str.casefold() == "delhi"]

print("\n6. DELHI AQI ANALYSIS")
print("-" * 30)

if not delhi_data.empty:
    print("Delhi records:", len(delhi_data))
    print("Average AQI:", round(delhi_data["AQI"].mean(), 2))
    print("Minimum AQI:", round(delhi_data["AQI"].min(), 2))
    print("Maximum AQI:", round(delhi_data["AQI"].max(), 2))

    delhi_data.to_csv(
        OUTPUT_DIR / "delhi_aqi_records.csv",
        index=False
    )
else:
    print("No valid AQI records found for Delhi.")

# 7. Summarize AQI categories
if "AQI_Bucket" in valid_aqi.columns:
    category_summary = (
        valid_aqi["AQI_Bucket"]
        .fillna("Unknown")
        .value_counts()
        .rename_axis("AQI_Category")
        .reset_index(name="Record_Count")
    )

    category_summary.to_csv(
        OUTPUT_DIR / "aqi_category_summary.csv",
        index=False
    )

    print("\n7. AQI CATEGORY SUMMARY")
    print("-" * 30)
    print(category_summary.to_string(index=False))

print("\n" + "=" * 50)
print("TASK 2 ANALYSIS COMPLETED")
print("Output folder:", OUTPUT_DIR)
print("=" * 50)
