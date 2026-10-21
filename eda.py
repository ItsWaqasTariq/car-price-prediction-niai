
from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Save charts without opening GUI windows.

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
DATASET_PATH = BASE_DIR / "cleaned_cars.csv"
OUTPUT_DIR = BASE_DIR / "reports" / "figures"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(DATASET_PATH)

print("--- Dataset Overview ---")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Average price: PKR {df['Price_PKR'].mean():,.0f}")
print(f"Median price: PKR {df['Price_PKR'].median():,.0f}")

# 1. Number of records per brand
brand_counts = df["Brand"].value_counts().sort_values()

plt.figure(figsize=(9, 5))
brand_counts.plot(kind="barh")
plt.title("Number of Cars by Brand")
plt.xlabel("Number of Records")
plt.ylabel("Brand")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "cars_by_brand.png", dpi=150)
plt.close()

# 2. Distribution of car prices
plt.figure(figsize=(9, 5))
plt.hist(df["Price_PKR"], bins=40, edgecolor="black")
plt.title("Car Price Distribution")
plt.xlabel("Price (PKR)")
plt.ylabel("Number of Cars")
plt.ticklabel_format(axis="x", style="plain")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "price_distribution.png", dpi=150)
plt.close()

# 3. Price versus manufacturing year
plt.figure(figsize=(9, 5))
plt.scatter(
    df["Year"],
    df["Price_PKR"],
    alpha=0.35,
    s=15,
)
plt.title("Car Price vs Manufacturing Year")
plt.xlabel("Manufacturing Year")
plt.ylabel("Price (PKR)")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "price_vs_year.png", dpi=150)
plt.close()

# 4. Price versus mileage
plt.figure(figsize=(9, 5))
plt.scatter(
    df["Mileage_KM"],
    df["Price_PKR"],
    alpha=0.35,
    s=15,
)
plt.title("Car Price vs Mileage")
plt.xlabel("Mileage (KM)")
plt.ylabel("Price (PKR)")
plt.ticklabel_format(axis="y", style="plain")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "price_vs_mileage.png", dpi=150)
plt.close()

# 5. Average price by fuel type
fuel_prices = (
    df.groupby("Fuel")["Price_PKR"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(8, 5))
fuel_prices.plot(kind="bar")
plt.title("Average Car Price by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average Price (PKR)")
plt.ticklabel_format(axis="y", style="plain")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "average_price_by_fuel.png", dpi=150)
plt.close()

print("\n--- Charts Saved ---")
for path in sorted(OUTPUT_DIR.glob("*.png")):
    print(path.relative_to(BASE_DIR))
