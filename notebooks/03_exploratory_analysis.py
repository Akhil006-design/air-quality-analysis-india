
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Project paths
project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "outputs" / "air_quality_cleaned.csv"
output_folder = project_folder / "outputs"
output_folder.mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(input_file, parse_dates=["Date"])

# Chart appearance
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# Use only records with an available AQI
aqi_df = df.dropna(subset=["AQI"]).copy()

print("EXPLORATORY DATA ANALYSIS")
print("=" * 45)
print("Total records:", len(df))
print("Records with AQI:", len(aqi_df))
print("Cities with AQI data:", aqi_df["City"].nunique())

# --------------------------------------------------
# 1. Average AQI by city
# --------------------------------------------------
city_aqi = (
    aqi_df.groupby("City")
    .agg(
        Average_AQI=("AQI", "mean"),
        Available_AQI_Records=("AQI", "count")
    )
    .sort_values("Average_AQI", ascending=False)
)

city_aqi.to_csv(output_folder / "average_aqi_by_city.csv")

print("\nTOP 10 CITIES BY AVERAGE RECORDED AQI")
print(city_aqi.head(10).round(2).to_string())

plt.figure(figsize=(12, 7))
sns.barplot(
    data=city_aqi.head(10).reset_index(),
    x="Average_AQI",
    y="City"
)
plt.title("Top 10 Cities by Average Recorded AQI")
plt.xlabel("Average AQI (available records only)")
plt.ylabel("City")
plt.tight_layout()
plt.savefig(
    output_folder / "top_10_cities_average_aqi.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# --------------------------------------------------
# 2. Monthly average AQI over time
# --------------------------------------------------
monthly_aqi = (
    aqi_df.set_index("Date")["AQI"]
    .resample("MS")
    .agg(["mean", "count"])
    .rename(columns={
        "mean": "Average_AQI",
        "count": "Available_Records"
    })
)

monthly_aqi.to_csv(output_folder / "monthly_average_aqi.csv")

print("\nMONTHLY AQI SUMMARY")
print(monthly_aqi.head(12).round(2).to_string())

plt.figure(figsize=(14, 6))
plt.plot(
    monthly_aqi.index,
    monthly_aqi["Average_AQI"],
    marker="o",
    markersize=3,
    linewidth=1.5
)
plt.title("Monthly Average AQI Across Available City Records")
plt.xlabel("Month")
plt.ylabel("Average AQI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(
    output_folder / "monthly_aqi_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# --------------------------------------------------
# 3. AQI category distribution
# --------------------------------------------------
bucket_counts = (
    aqi_df["AQI_Bucket"]
    .dropna()
    .value_counts()
    .rename_axis("AQI_Category")
    .reset_index(name="Record_Count")
)

bucket_counts.to_csv(
    output_folder / "aqi_category_distribution.csv",
    index=False
)

print("\nAQI CATEGORY DISTRIBUTION")
print(bucket_counts.to_string(index=False))

plt.figure(figsize=(10, 6))
sns.barplot(
    data=bucket_counts,
    x="AQI_Category",
    y="Record_Count"
)
plt.title("Distribution of Recorded AQI Categories")
plt.xlabel("AQI Category")
plt.ylabel("Number of Records")
plt.xticks(rotation=30, ha="right")
plt.tight_layout()
plt.savefig(
    output_folder / "aqi_category_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\nEDA COMPLETED")
print("Charts and summary CSV files saved in:", output_folder)
