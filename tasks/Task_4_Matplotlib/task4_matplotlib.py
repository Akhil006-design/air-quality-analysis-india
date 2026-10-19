
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parents[2]

# File locations
DATA_FILE = PROJECT_DIR / "data" / "city_day.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

# Create the output folder if needed
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load the air quality dataset
df = pd.read_csv(DATA_FILE)

# Convert Date column to date format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Keep only rows with valid AQI values
aqi_data = df.dropna(subset=["AQI"]).copy()

print("AIR QUALITY DATA VISUALIZATION")
print("-" * 40)
print("Total dataset rows:", len(df))
print("Valid AQI records:", len(aqi_data))


# CHART 1: Average AQI by city
city_aqi = (
    aqi_data.groupby("City")["AQI"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10, 6))
city_aqi.sort_values().plot(kind="barh")

plt.title("Top 10 Cities by Average AQI")
plt.xlabel("Average AQI")
plt.ylabel("City")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "average_aqi_by_city.png", dpi=300)
plt.close()

print("Chart 1 saved: average_aqi_by_city.png")


# CHART 2: Delhi AQI over time
delhi_data = aqi_data[
    aqi_data["City"].str.lower() == "delhi"
].dropna(subset=["Date"]).sort_values("Date")

plt.figure(figsize=(12, 6))
plt.plot(delhi_data["Date"], delhi_data["AQI"], linewidth=1)

plt.title("Delhi Air Quality Index Over Time")
plt.xlabel("Date")
plt.ylabel("AQI")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "delhi_aqi_over_time.png", dpi=300)
plt.close()

print("Chart 2 saved: delhi_aqi_over_time.png")


# CHART 3: Distribution of AQI values
plt.figure(figsize=(10, 6))
plt.hist(aqi_data["AQI"], bins=30, edgecolor="black")

plt.title("Distribution of Air Quality Index")
plt.xlabel("AQI")
plt.ylabel("Number of Records")
plt.tight_layout()

plt.savefig(OUTPUT_DIR / "aqi_distribution.png", dpi=300)
plt.close()

print("Chart 3 saved: aqi_distribution.png")


# Save a summary of the city averages
city_aqi.rename("Average_AQI").to_csv(
    OUTPUT_DIR / "average_aqi_by_city.csv"
)

print("-" * 40)
print("All three charts generated successfully!")
print("Output folder:", OUTPUT_DIR)
