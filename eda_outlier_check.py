
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
df = pd.read_csv(BASE_DIR / "cleaned_cars.csv")

models_to_check = [
    ("Toyota", "Fortuner"),
    ("Honda", "Civic"),
    ("Toyota", "Corolla"),
    ("Honda", "City"),
    ("Suzuki", "Wagon R"),
]

for brand, model in models_to_check:
    subset = df[
        (df["Brand"] == brand) &
        (df["Model"] == model)
    ]

    print(f"\n--- {brand} {model}: Lowest 5 prices ---")
    print(
        subset.nsmallest(5, "Price_PKR")[
            ["Brand", "Model", "Year", "Engine_CC",
             "Mileage_KM", "Fuel", "Transmission", "Price_PKR"]
        ].to_string(index=False)
    )

    print(f"\n--- {brand} {model}: Highest 5 prices ---")
    print(
        subset.nlargest(5, "Price_PKR")[
            ["Brand", "Model", "Year", "Engine_CC",
             "Mileage_KM", "Fuel", "Transmission", "Price_PKR"]
        ].to_string(index=False)
    )
