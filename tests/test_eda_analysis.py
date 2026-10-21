
import pandas as pd
import pytest

from car_price_prediction.eda_analysis import (
    get_brand_counts,
    get_price_summary,
    load_dataset,
)


def sample_data():
    return pd.DataFrame({
        "Brand": ["Toyota", "Honda", "Toyota"],
        "Model": ["Corolla", "Civic", "Corolla"],
        "Year": [2020, 2019, 2021],
        "Engine_CC": [1300, 1500, 1800],
        "Mileage_KM": [20000, 30000, 15000],
        "Fuel": ["Petrol", "Petrol", "Diesel"],
        "Transmission": ["Manual", "Automatic", "Automatic"],
        "Price_PKR": [2500000, 3000000, 3500000],
    })


def test_price_summary():
    result = get_price_summary(sample_data())

    assert result["count"] == 3
    assert result["mean"] == 3000000
    assert result["median"] == 3000000
    assert result["min"] == 2500000
    assert result["max"] == 3500000


def test_brand_counts():
    result = get_brand_counts(sample_data())

    assert result["Toyota"] == 2
    assert result["Honda"] == 1


def test_load_dataset_rejects_missing_columns(tmp_path):
    path = tmp_path / "invalid.csv"
    pd.DataFrame({"Brand": ["Toyota"]}).to_csv(path, index=False)

    with pytest.raises(ValueError, match="Missing required columns"):
        load_dataset(str(path))
