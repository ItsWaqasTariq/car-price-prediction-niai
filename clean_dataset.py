
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "pakistan_car_price_6500_clean.csv"
OUTPUT_PATH = BASE_DIR / "cleaned_cars.csv"

REQUIRED_COLUMNS = [
    "Brand",
    "Model",
    "Year",
    "Engine_CC",
    "Mileage_KM",
    "Fuel",
    "Transmission",
    "Price_PKR",
]


def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Validate and clean car records without modifying the input."""

    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    cleaned = df[REQUIRED_COLUMNS].copy()

    # Normalize whitespace in categorical columns.
    categorical_columns = [
        "Brand",
        "Model",
        "Fuel",
        "Transmission",
    ]

    for column in categorical_columns:
        cleaned[column] = cleaned[column].map(
            lambda value: value.strip() if isinstance(value, str) else value
        )

    # Convert numerical fields; invalid text becomes missing.
    numerical_columns = [
        "Year",
        "Engine_CC",
        "Mileage_KM",
        "Price_PKR",
    ]

    for column in numerical_columns:
        cleaned[column] = pd.to_numeric(
            cleaned[column], errors="coerce"
        )

    # Remove records missing any required field.
    cleaned = cleaned.dropna(subset=REQUIRED_COLUMNS)

    # Keep only whole-number years and prices.
    whole_number_columns = ["Year", "Price_PKR", "Mileage_KM"]
    for column in whole_number_columns:
        cleaned = cleaned[
            cleaned[column] % 1 == 0
        ]

    # Validate numerical values.
    valid_rows = (
        cleaned["Year"].between(1886, 2026)
        & cleaned["Engine_CC"].gt(0)
        & cleaned["Mileage_KM"].ge(0)
        & cleaned["Price_PKR"].gt(0)
    )

    cleaned = cleaned.loc[valid_rows].copy()

    # Remove exact duplicate records only.
    cleaned = cleaned.drop_duplicates()

    # Use consistent integer types for whole-number columns.
    for column in whole_number_columns:
        cleaned[column] = cleaned[column].astype("int64")

    return cleaned.reset_index(drop=True)


def main() -> None:
    original = pd.read_csv(INPUT_PATH)
    cleaned = clean_dataset(original)

    cleaned.to_csv(OUTPUT_PATH, index=False)

    print("--- Cleaning Report ---")
    print(f"Original rows: {len(original)}")
    print(f"Cleaned rows:  {len(cleaned)}")
    print(f"Rows removed:  {len(original) - len(cleaned)}")
    print(f"Missing values remaining: {cleaned.isna().sum().sum()}")
    print(f"Duplicate rows remaining: {cleaned.duplicated().sum()}")
    print(f"Output saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
