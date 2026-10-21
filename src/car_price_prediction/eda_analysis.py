
import pandas as pd

REQUIRED_COLUMNS = {
    "Brand",
    "Model",
    "Year",
    "Engine_CC",
    "Mileage_KM",
    "Fuel",
    "Transmission",
    "Price_PKR",
}


def load_dataset(path: str) -> pd.DataFrame:
    """Load the cleaned car dataset and validate its columns."""
    df = pd.read_csv(path)

    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    return df


def get_price_summary(df: pd.DataFrame) -> dict:
    """Return basic price statistics."""
    if "Price_PKR" not in df.columns:
        raise ValueError("Missing required column: Price_PKR")

    prices = df["Price_PKR"]

    return {
        "count": int(prices.count()),
        "mean": float(prices.mean()),
        "median": float(prices.median()),
        "min": float(prices.min()),
        "max": float(prices.max()),
    }


def get_brand_counts(df: pd.DataFrame) -> pd.Series:
    """Count records for each brand."""
    if "Brand" not in df.columns:
        raise ValueError("Missing required column: Brand")

    return df["Brand"].value_counts()
