
import pandas as pd

DATASET_PATH = "pakistan_car_price_6500_clean.csv"

df = pd.read_csv(DATASET_PATH)

print("\n--- 1. Dataset Shape ---")
print(df.shape)

print("\n--- 2. Column Names ---")
print(df.columns.tolist())

print("\n--- 3. First Five Rows ---")
print(df.head().to_string())

print("\n--- 4. Dataset Information ---")
df.info()

print("\n--- 5. Missing Values ---")
print(df.isnull().sum().to_string())

print("\n--- 6. Duplicate Rows ---")
print(df.duplicated().sum())

print("\n--- 7. Numerical Statistics ---")
print(df.describe().to_string())
