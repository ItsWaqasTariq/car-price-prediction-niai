
# Exploratory Data Analysis (EDA) Report

## 1. Dataset Overview

- **Dataset:** `cleaned_cars.csv`
- **Total records:** 6,473
- **Total columns:** 8
- **Target variable:** `Price_PKR`
- **Features:** Brand, Model, Year, Engine_CC, Mileage_KM, Fuel, Transmission

## 2. Price Statistics

| Statistic | Price (PKR) |
|---|---:|
| Mean | 5,098,877 |
| Median | 5,390,000 |
| Minimum | 33,351 |
| Maximum | 22,000,000 |

The dataset contains a broad range of car prices.

## 3. Brand Distribution

Suzuki has the most records (2,617), followed by Toyota (904). MG has the fewest records (554).

These counts describe the dataset, not real Pakistani market share.

## 4. Numerical Relationships

| Feature | Correlation with Price |
|---|---:|
| Engine capacity | 0.741 |
| Manufacturing year | 0.524 |
| Mileage | -0.007 |

Engine capacity and manufacturing year have positive linear associations with price in this dataset. The overall linear relationship between mileage and price is close to zero.

Correlation does not establish causation.

## 5. Fuel and Transmission

Petrol vehicles account for 5,754 records. CNG and LPG have only 24 and 16 records, respectively, so their average prices may be less reliable.

Automatic vehicles have a higher median price than manual vehicles in this dataset. Differences in brands, models and years may contribute to this result.

## 6. Outlier Investigation

Some older vehicles have unusually low prices. Several models also have repeated upper price values, potentially indicating synthetic-data caps or rounding.

No additional records were removed during EDA. These records need external validation before any exclusion decision.

## 7. Generated Charts

Charts are stored in `reports/figures/`.

- `cars_by_brand.png`
- `price_distribution.png`
- `price_vs_year.png`
- `price_vs_mileage.png`
- `average_price_by_fuel.png`

## 8. Limitations

The dataset is synthetic. Its patterns and future model evaluation scores cannot establish real-world accuracy for Pakistani car prices. Validation using suitable real-world listings is required.
