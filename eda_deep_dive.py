
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "cleaned_cars.csv")

print("--- Record counts by brand and model ---")
print(
    df.groupby(["Brand", "Model"])
    .size()
    .sort_values(ascending=False)
    .head(15)
    .to_string()
)

print("\n--- Price summary by manufacturing year ---")
print(
    df.groupby("Year")["Price_PKR"]
    .agg(["count", "median", "mean"])
    .round(0)
    .tail(10)
    .to_string()
)

print("\n--- Mileage correlation within newer vs older cars ---")
df["Age_Group"] = df["Year"].apply(
    lambda year: "2020 or newer" if year >= 2020 else "Before 2020"
)

for group, subset in df.groupby("Age_Group"):
    print(f"\n{group}: {len(subset)} records")
    print(
        subset[["Mileage_KM", "Price_PKR"]]
        .corr()
        .loc["Mileage_KM", "Price_PKR"]
        .round(3)
    )

print("\n--- Price variability by brand and model ---")
summary = (
    df.groupby(["Brand", "Model"])["Price_PKR"]
    .agg(["count", "median", "min", "max"])
    .query("count >= 10")
    .sort_values("median", ascending=False)
)

print(summary.head(15).round(0).to_string())
