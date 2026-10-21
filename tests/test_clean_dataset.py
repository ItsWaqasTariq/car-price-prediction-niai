
import pandas as pd
import pytest

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from clean_dataset import clean_dataset


def sample_data():
    return pd.DataFrame({
        "Brand": ["Toyota", "Honda", "Toyota"],
        "Model": ["Corolla", "Civic", "Corolla"],
        "Year": [2020, 2019, 2020],
        "Engine_CC": [1300, 1500, 1300],
        "Mileage_KM": [20000, 30000, 20000],
        "Fuel": ["Petrol", "Petrol", "Petrol"],
        "Transmission": ["Manual", "Automatic", "Manual"],
        "Price_PKR": [2500000, 3000000, 2500000],
    })


def test_removes_exact_duplicates():
    result = clean_dataset(sample_data())
    assert len(result) == 2
    assert not result.duplicated().any()


def test_preserves_original_dataframe():
    original = sample_data()
    before = original.copy(deep=True)

    clean_dataset(original)

    pd.testing.assert_frame_equal(original, before)




def test_removes_invalid_price():
    data = sample_data()
    data.loc[0, "Price_PKR"] = 0

    result = clean_dataset(data)

    assert (result["Price_PKR"] > 0).all()
    assert len(result) == 2



def test_rejects_missing_required_columns():
    data = sample_data().drop(columns=["Price_PKR"])

    with pytest.raises(ValueError, match="Missing required columns"):
        clean_dataset(data)
