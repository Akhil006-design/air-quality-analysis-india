
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "outputs" / "air_quality_cleaned.csv"
output_folder = project_folder / "outputs"

df = pd.read_csv(input_file, parse_dates=["Date"])
df = df.dropna(subset=["AQI"]).copy()

# Compare complete calendar years only
df = df[df["Date"].dt.year.between(2015, 2019)].copy()
df["Year"] = df["Date"].dt.year

# Calculate each city's average AQI for each year
city_year = (
    df.groupby(["City", "Year"])
    .agg(
        Average_AQI=("AQI", "mean"),
        AQI_Records=("AQI", "count")
    )
    .reset_index()
)

# Create a table: cities as rows, years as columns
aqi_pivot = city_year.pivot(
    index="City",
    columns="Year",
    values="Average_AQI"
)

# Keep only cities with AQI averages in every year
years = list(range(2015, 2020))
common_cities = aqi_pivot.dropna(subset=years)

print("FAIR CITY COMPARISON: 2015-2019")
print("=" * 45)
print("Cities represented in all five years:", len(common_cities))
print("Cities:", common_cities.index.tolist())

if common_cities.empty:
    print("\nNo cities have complete yearly AQI coverage.")
    print("We need to use a different comparison method.")
else:
    # Equal weight for every city in every year
    fair_yearly_aqi = common_cities[years].mean()

    print("\nAVERAGE AQI FOR THE SAME CITIES")
    print(fair_yearly_aqi.round(2).to_string())

    fair_yearly_aqi.to_csv(
        output_folder / "fair_yearly_aqi_2015_2019.csv",
        header=["Average_AQI"]
    )

    # Save city-by-city comparison
    common_cities.to_csv(
        output_folder / "common_cities_aqi_2015_2019.csv"
    )

    # Plot the fair comparison
    sns.set_theme(style="whitegrid")

    plt.figure(figsize=(10, 6))
    plt.plot(
        years,
        fair_yearly_aqi.values,
        marker="o",
        linewidth=2
    )
    plt.title("Yearly AQI: Same Cities, 2015-2019")
    plt.xlabel("Year")
    plt.ylabel("Mean City-Level Average AQI")
    plt.xticks(years)
    plt.tight_layout()

    plt.savefig(
        output_folder / "fair_yearly_aqi_2015_2019.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    print("\nSaved fair comparison table and chart.")

print("\nCOMPARISON COMPLETED")
