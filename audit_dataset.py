
import pandas as pd

DATASET_PATH = "pakistan_car_price_6500_clean.csv"
df = pd.read_csv(DATASET_PATH)

print("\n--- 1. Unique Categorical Values ---")
for column in ["Brand", "Model", "Fuel", "Transmission"]:
    print(f"\n{column}:")
    print(sorted(df[column].dropna().unique().tolist()))

print("\n--- 2. Invalid Numerical Values ---")
checks = {
    "Year": df["Year"].lt(1886),
    "Engine_CC": df["Engine_CC"].le(0),
    "Mileage_KM": df["Mileage_KM"].lt(0),
    "Price_PKR": df["Price_PKR"].le(0),
}

for column, invalid_mask in checks.items():
    print(f"{column}: {invalid_mask.sum()} invalid rows")

print("\n--- 3. Year Range ---")
print(df["Year"].value_counts().sort_index().to_string())

print("\n--- 4. Highest Mileage Records ---")
print(
    df.nlargest(10, "Mileage_KM")[
        ["Brand", "Model", "Year", "Mileage_KM", "Price_PKR"]
    ].to_string(index=False)
)

print("\n--- 5. Lowest Price Records ---")
print(
    df.nsmallest(10, "Price_PKR")[
        ["Brand", "Model", "Year", "Engine_CC", "Price_PKR"]
    ].to_string(index=False)
)

print("\n--- 6. Duplicate Examples ---")
print(
    df[df.duplicated(keep=False)]
    .sort_values(["Brand", "Model", "Year"])
    .head(10)
    .to_string(index=False)
)
