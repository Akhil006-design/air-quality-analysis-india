
from pathlib import Path
import pandas as pd

# Locate the project folder and load the original dataset
project_folder = Path(__file__).resolve().parent.parent
file_path = project_folder / "data" / "city_day.csv"

df = pd.read_csv(file_path)

print("=" * 50)
print("AIR QUALITY DATASET: QUALITY CHECK")
print("=" * 50)

# 1. Dataset size
print("\n1. DATASET SIZE")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# 2. Number of cities
print("\n2. CITY INFORMATION")
print("Number of cities:", df["City"].nunique())
print("Cities:", sorted(df["City"].dropna().unique()))

# 3. Duplicate rows
print("\n3. DUPLICATE ROWS")
print("Duplicate rows:", df.duplicated().sum())

# 4. Missing values and percentages
print("\n4. MISSING DATA")
missing_count = df.isna().sum()
missing_percent = (missing_count / len(df)) * 100

missing_summary = pd.DataFrame({
    "Missing Count": missing_count,
    "Missing Percentage": missing_percent.round(2)
})

print(missing_summary.sort_values(
    "Missing Percentage", ascending=False
).to_string())

# 5. Column data types
print("\n5. COLUMN DATA TYPES")
print(df.dtypes.to_string())

# 6. Convert dates for date-based analysis
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

print("\n6. DATE CHECK")
print("Earliest date:", df["Date"].min())
print("Latest date:", df["Date"].max())
print("Invalid dates:", df["Date"].isna().sum())

print("\nDATA-QUALITY CHECK COMPLETED")
