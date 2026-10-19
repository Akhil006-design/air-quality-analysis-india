
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Locate the project folders
PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_DIR / "data" / "city_day.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Set a clean chart style
sns.set_theme(style="whitegrid", palette="deep")

# Load dataset
df = pd.read_csv(DATA_FILE)

# Keep only rows with valid AQI values
aqi_data = df.dropna(subset=["AQI"]).copy()

print("TASK 5: SEABORN DATA VISUALIZATION")
print("-" * 40)
print("Total rows:", len(df))
print("Valid AQI records:", len(aqi_data))


# CHART 1: Correlation heatmap
pollutants = [
    "PM2.5", "PM10", "NO", "NO2", "NOx",
    "NH3", "CO", "SO2", "O3", "Benzene",
    "Toluene", "Xylene", "AQI"
]

# Select available numeric columns
available_columns = [
    column for column in pollutants if column in df.columns
]

correlation_data = df[available_columns].corr(numeric_only=True)

plt.figure(figsize=(12, 9))
sns.heatmap(
    correlation_data,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    center=0
)

plt.title("Correlation Between AQI and Pollutants")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "pollutant_correlation_heatmap.png", dpi=300)
plt.close()

print("Chart 1 saved: pollutant_correlation_heatmap.png")


# CHART 2: AQI distribution across selected cities
top_cities = (
    aqi_data.groupby("City")["AQI"]
    .mean()
    .nlargest(6)
    .index
)

city_data = aqi_data[aqi_data["City"].isin(top_cities)]

plt.figure(figsize=(12, 6))
sns.boxplot(data=city_data, x="City", y="AQI")

plt.title("AQI Distribution Across Six High-AQI Cities")
plt.xlabel("City")
plt.ylabel("Air Quality Index (AQI)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "aqi_boxplot_by_city.png", dpi=300)
plt.close()

print("Chart 2 saved: aqi_boxplot_by_city.png")


# CHART 3: PM2.5 compared with AQI
scatter_data = df[["PM2.5", "AQI"]].dropna()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=scatter_data,
    x="PM2.5",
    y="AQI",
    alpha=0.4,
    s=25
)

plt.title("PM2.5 Concentration vs Air Quality Index")
plt.xlabel("PM2.5 Concentration")
plt.ylabel("Air Quality Index (AQI)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "pm25_vs_aqi_scatterplot.png", dpi=300)
plt.close()

print("Chart 3 saved: pm25_vs_aqi_scatterplot.png")


# Save correlation values as a CSV file
correlation_data.to_csv(
    OUTPUT_DIR / "pollutant_correlation.csv"
)

print("-" * 40)
print("All three Seaborn charts generated successfully!")
print("Output folder:", OUTPUT_DIR)
