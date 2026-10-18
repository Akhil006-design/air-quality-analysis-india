
from pathlib import Path
import pandas as pd

# Set up project paths
project_folder = Path(__file__).resolve().parent.parent
input_file = project_folder / "data" / "city_day.csv"
output_folder = project_folder / "outputs"

output_folder.mkdir(parents=True, exist_ok=True)

# Load the original dataset
df = pd.read_csv(input_file)

print("Original rows:", len(df))

# Convert Date into datetime format
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove rows only if essential city/date information is invalid
df = df.dropna(subset=["City", "Date"]).copy()

# Check whether a city has multiple records for the same date
city_date_duplicates = df.duplicated(
    subset=["City", "Date"]
).sum()

print("Duplicate city-date combinations:", city_date_duplicates)

# Report negative values in numeric measurement columns
numeric_columns = df.select_dtypes(include="number").columns

print("\nNegative values by column:")
print((df[numeric_columns] < 0).sum().to_string())

# Preserve missing pollutant and AQI values.
# Do not replace missing measurements with zero.
# Do not remove city-date records automatically.

# Sort records for easier analysis
df = df.sort_values(["City", "Date"]).reset_index(drop=True)

# Save a separate cleaned copy
output_file = output_folder / "air_quality_cleaned.csv"
df.to_csv(output_file, index=False)

# Save a missing-value summary
missing_summary = pd.DataFrame({
    "Missing_Count": df.isna().sum(),
    "Missing_Percentage": (
        df.isna().mean() * 100
    ).round(2)
})

missing_file = output_folder / "missing_values_summary.csv"
missing_summary.to_csv(missing_file)

print("\nCleaned dataset rows:", len(df))
print("Cleaned dataset columns:", len(df.columns))
print("Missing values preserved for careful analysis.")
print("\nSaved cleaned dataset to:", output_file)
print("Saved missing-value report to:", missing_file)
print("\nDATA CLEANING STEP COMPLETED")
