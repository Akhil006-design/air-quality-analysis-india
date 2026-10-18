
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "outputs" / "air_quality_cleaned.csv"
output_folder = project_folder / "outputs"

df = pd.read_csv(input_file, parse_dates=["Date"])

# Keep records with AQI measurements
aqi_df = df.dropna(subset=["AQI"]).copy()

# Add year to each record
aqi_df["Year"] = aqi_df["Date"].dt.year

# Calculate average AQI separately for each city and year
city_year = (
    aqi_df.groupby(["Year", "City"])
    .agg(
        Average_AQI=("AQI", "mean"),
        AQI_Records=("AQI", "count")
    )
    .reset_index()
)

city_year.to_csv(
    output_folder / "city_year_aqi.csv",
    index=False
)

# Give each represented city equal weight in the yearly average
yearly_aqi = (
    city_year.groupby("Year")
    .agg(
        Average_City_AQI=("Average_AQI", "mean"),
        Cities_Represented=("City", "nunique"),
        Total_AQI_Records=("AQI_Records", "sum")
    )
)

print("YEARLY AQI SUMMARY")
print(yearly_aqi.round(2).to_string())

yearly_aqi.to_csv(
    output_folder / "yearly_aqi_summary.csv"
)

# Plot the yearly comparison
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))
plt.plot(
    yearly_aqi.index,
    yearly_aqi["Average_City_AQI"],
    marker="o",
    linewidth=2
)

plt.title("Yearly Average AQI Across Represented Cities")
plt.xlabel("Year")
plt.ylabel("Mean of City-Level Average AQI")
plt.xticks(yearly_aqi.index)
plt.tight_layout()

plt.savefig(
    output_folder / "yearly_aqi_trend.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\nSaved yearly summary and chart in:", output_folder)
