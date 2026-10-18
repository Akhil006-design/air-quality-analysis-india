
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "outputs" / "air_quality_cleaned.csv"
output_folder = project_folder / "outputs"

df = pd.read_csv(input_file)

pollutants = [
    "PM2.5", "PM10", "NO2", "CO", "SO2", "O3", "AQI"
]

# Keep only the selected measurements
data = df[pollutants].copy()

# Calculate correlations using available pairs
correlation = data.corr(method="pearson", min_periods=30)

print("POLLUTANT AND AQI CORRELATIONS")
print("=" * 40)
print(correlation.round(2).to_string())

# Save correlation values
correlation.to_csv(
    output_folder / "pollutant_aqi_correlations.csv"
)

# Save the number of paired observations for each comparison
paired_counts = data.notna().astype(int).T @ data.notna().astype(int)
paired_counts.to_csv(
    output_folder / "pollutant_correlation_sample_counts.csv"
)

# Plot correlation heatmap
sns.set_theme(style="white")
plt.figure(figsize=(10, 8))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    vmin=-1,
    vmax=1,
    center=0,
    cmap="coolwarm",
    square=True
)

plt.title("Correlation Between Pollutants and AQI")
plt.tight_layout()

plt.savefig(
    output_folder / "pollutant_aqi_correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Report the pollutant most strongly correlated with AQI
aqi_correlations = correlation["AQI"].drop("AQI").dropna()

if not aqi_correlations.empty:
    strongest = aqi_correlations.abs().idxmax()
    print(
        "\nStrongest absolute correlation with AQI:",
        strongest,
        "=",
        round(aqi_correlations[strongest], 3)
    )

print("\nSaved correlation table, sample counts and heatmap.")
