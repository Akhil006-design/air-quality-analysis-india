
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Set project paths
PROJECT_DIR = Path(__file__).resolve().parents[2]
DATA_FILE = PROJECT_DIR / "data" / "city_day.csv"
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")


# 2. Load the dataset
df = pd.read_csv(DATA_FILE)

print("=" * 60)
print("TASK 6: EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nDataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five records:")
print(df.head())


# 3. Check data quality
print("\n--- DATA QUALITY ---")

missing_values = df.isnull().sum().sort_values(ascending=False)

missing_report = pd.DataFrame({
    "Missing_Count": missing_values,
    "Missing_Percentage": (
        missing_values / len(df) * 100
    ).round(2)
})

missing_report.to_csv(
    OUTPUT_DIR / "missing_values_report.csv"
)

print("\nMissing values:")
print(missing_report)

duplicate_count = int(df.duplicated().sum())

duplicate_report = pd.DataFrame({
    "Metric": ["Total Rows", "Duplicate Rows"],
    "Value": [len(df), duplicate_count]
})

duplicate_report.to_csv(
    OUTPUT_DIR / "duplicate_report.csv",
    index=False
)

print("\nDuplicate rows:", duplicate_count)


# 4. Prepare valid AQI records
if "AQI" not in df.columns:
    raise ValueError("The dataset does not contain an AQI column.")

aqi = pd.to_numeric(df["AQI"], errors="coerce")
valid_aqi = aqi.dropna()

if valid_aqi.empty:
    raise ValueError("No valid AQI values were found.")

aqi_stats = pd.DataFrame({
    "Metric": [
        "Valid AQI Count",
        "Mean AQI",
        "Median AQI",
        "Minimum AQI",
        "Maximum AQI",
        "Standard Deviation"
    ],
    "Value": [
        valid_aqi.count(),
        valid_aqi.mean(),
        valid_aqi.median(),
        valid_aqi.min(),
        valid_aqi.max(),
        valid_aqi.std()
    ]
})

aqi_stats.to_csv(
    OUTPUT_DIR / "overall_aqi_statistics.csv",
    index=False
)

print("\n--- OVERALL AQI STATISTICS ---")
print(aqi_stats.round(2))


# 5. Analyze AQI by city
if "City" in df.columns:
    city_data = pd.DataFrame({
        "City": df["City"],
        "AQI": aqi
    }).dropna(subset=["City", "AQI"])

    city_summary = (
        city_data.groupby("City")["AQI"]
        .agg(["count", "mean", "median", "min", "max"])
        .round(2)
        .sort_values("mean", ascending=False)
    )

    city_summary.to_csv(
        OUTPUT_DIR / "city_aqi_summary.csv"
    )

    print("\n--- TOP 10 CITIES BY MEAN AQI ---")
    print(city_summary.head(10))

    top_cities = city_summary.head(10).sort_values("mean")

    plt.figure(figsize=(10, 6))
    plt.barh(top_cities.index, top_cities["mean"])
    plt.title("Top 10 Cities by Average AQI")
    plt.xlabel("Average AQI")
    plt.ylabel("City")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "top_10_cities_average_aqi.png",
        dpi=300
    )
    plt.close()


# 6. Analyze monthly AQI trends
if "Date" in df.columns:
    date_values = pd.to_datetime(
        df["Date"], errors="coerce"
    )

    monthly_data = pd.DataFrame({
        "Date": date_values,
        "AQI": aqi
    }).dropna()

    monthly_data["Month"] = (
        monthly_data["Date"].dt.month
    )

    monthly_data["Month_Name"] = (
        monthly_data["Date"].dt.month_name()
    )

    monthly_summary = (
        monthly_data.groupby("Month")
        .agg(
            Mean_AQI=("AQI", "mean"),
            Median_AQI=("AQI", "median"),
            Record_Count=("AQI", "count")
        )
        .round(2)
    )

    monthly_summary["Month_Name"] = (
        monthly_summary.index.map(
            lambda month: pd.Timestamp(
                month=month, day=1, year=2000
            ).month_name()
        )
    )

    monthly_summary.to_csv(
        OUTPUT_DIR / "monthly_aqi_summary.csv"
    )

    print("\n--- MONTHLY AQI SUMMARY ---")
    print(monthly_summary)

    plt.figure(figsize=(10, 5))
    plt.plot(
        monthly_summary.index,
        monthly_summary["Mean_AQI"],
        marker="o"
    )
    plt.xticks(range(1, 13))
    plt.title("Average AQI by Month")
    plt.xlabel("Month Number")
    plt.ylabel("Average AQI")
    plt.tight_layout()
    plt.savefig(
        OUTPUT_DIR / "monthly_aqi_trend.png",
        dpi=300
    )
    plt.close()


# 7. Analyze pollutant relationships
pollutants = [
    "PM2.5", "PM10", "NO", "NO2", "NOx",
    "NH3", "CO", "SO2", "O3", "Benzene",
    "Toluene", "Xylene"
]

available_pollutants = [
    column for column in pollutants
    if column in df.columns
]

correlation_columns = available_pollutants.copy()

if "AQI" in df.columns:
    correlation_columns.append("AQI")

numeric_pollutants = df[correlation_columns].apply(
    pd.to_numeric, errors="coerce"
)

correlation_matrix = numeric_pollutants.corr()

correlation_matrix.to_csv(
    OUTPUT_DIR / "pollutant_correlation_matrix.csv"
)

print("\n--- POLLUTANT CORRELATION WITH AQI ---")

if "AQI" in correlation_matrix.columns:
    aqi_correlations = (
        correlation_matrix["AQI"]
        .drop("AQI")
        .dropna()
        .sort_values(ascending=False)
    )

    print(aqi_correlations.round(3))

    aqi_correlations.to_csv(
        OUTPUT_DIR / "pollutant_aqi_correlations.csv",
        header=["Correlation_with_AQI"]
    )

plt.figure(figsize=(12, 9))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    center=0
)
plt.title("Pollutant and AQI Correlation Heatmap")
plt.tight_layout()
plt.savefig(
    OUTPUT_DIR / "pollutant_correlation_heatmap.png",
    dpi=300
)
plt.close()


# 8. Identify unusually high AQI observations
q1 = valid_aqi.quantile(0.25)
q3 = valid_aqi.quantile(0.75)
iqr = q3 - q1

upper_limit = q3 + 1.5 * iqr

high_aqi = df.loc[
    aqi > upper_limit
].copy()

high_aqi.to_csv(
    OUTPUT_DIR / "unusually_high_aqi_records.csv",
    index=False
)

print("\n--- HIGH AQI OBSERVATIONS ---")
print("IQR upper limit:", round(upper_limit, 2))
print("Records above the limit:", len(high_aqi))


# 9. Save key findings
findings = [
    f"Total dataset records: {len(df)}",
    f"Valid AQI records: {valid_aqi.count()}",
    f"Duplicate records: {duplicate_count}",
    f"Mean AQI: {valid_aqi.mean():.2f}",
    f"Median AQI: {valid_aqi.median():.2f}",
    f"Minimum AQI: {valid_aqi.min():.2f}",
    f"Maximum AQI: {valid_aqi.max():.2f}",
    f"Missing values across all columns: {int(df.isnull().sum().sum())}",
    f"Records above the IQR upper limit: {len(high_aqi)}"
]

if "City" in df.columns and not city_summary.empty:
    highest_city = city_summary.index[0]
    findings.append(
        f"Highest mean AQI city: {highest_city} "
        f"({city_summary.iloc[0]['mean']:.2f})"
    )

if (
    "AQI" in correlation_matrix.columns
    and not aqi_correlations.empty
):
    strongest_pollutant = aqi_correlations.index[0]
    findings.append(
        f"Strongest positive AQI correlation among analyzed "
        f"pollutants: {strongest_pollutant} "
        f"({aqi_correlations.iloc[0]:.3f})"
    )

with open(
    OUTPUT_DIR / "key_findings.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write("TASK 6: KEY FINDINGS\n")
    file.write("=" * 40 + "\n")
    file.write("\n".join(findings))
    file.write("\n")

print("\n--- KEY FINDINGS ---")
for finding in findings:
    print("-", finding)

print("\nAll EDA outputs saved to:")
print(OUTPUT_DIR)

print("\nTASK 6 ANALYSIS COMPLETED SUCCESSFULLY!")
