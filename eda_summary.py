
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "cleaned_cars.csv")

print("--- Price Statistics (PKR) ---")
print(df["Price_PKR"].describe().round(2).to_string())

print("\n--- Records by Brand ---")
print(df["Brand"].value_counts().to_string())

print("\n--- Price by Brand ---")
print(
    df.groupby("Brand")["Price_PKR"]
    .agg(["count", "mean", "median"])
    .sort_values("median", ascending=False)
    .round(0)
    .to_string()
)

print("\n--- Price by Fuel Type ---")
print(
    df.groupby("Fuel")["Price_PKR"]
    .agg(["count", "mean", "median"])
    .sort_values("median", ascending=False)
    .round(0)
    .to_string()
)

print("\n--- Price by Transmission ---")
print(
    df.groupby("Transmission")["Price_PKR"]
    .agg(["count", "mean", "median"])
    .sort_values("median", ascending=False)
    .round(0)
    .to_string()
)

print("\n--- Numeric Correlations ---")
print(
    df[["Year", "Engine_CC", "Mileage_KM", "Price_PKR"]]
    .corr()
    .round(3)
    .to_string()
)
