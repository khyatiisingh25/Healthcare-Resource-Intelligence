# Synthetic Data Generation

## Purpose

Generate realistic synthetic healthcare inventory and medicine consumption data for the internal hackathon prototype.

The generated data must be clearly labelled as synthetic/demo data.

## Facilities

Generate multiple healthcare facilities with different sizes:

- Small PHC
- Medium CHC
- Large Hospital

Each facility should have:

- facility_id
- facility_type
- city
- latitude
- longitude

## Medicines

Generate a set of medicines with different consumption patterns.

Each medicine should have:

- medicine_id
- medicine_name
- category
- unit
- base_consumption_rate
- shelf/stock characteristics

## Inventory Behaviour

Simulate different scenarios:

### 1. Stable Demand

Consumption remains relatively consistent.

### 2. Increasing Demand

Consumption gradually increases over time.

### 3. Decreasing Demand

Consumption gradually decreases.

### 4. Demand Spike

Consumption suddenly increases for a short period.

### 5. Low Stock

Current inventory approaches the safety-stock threshold.

### 6. Long Lead Time

Supplier delivery requires more days.

## Daily Records

Generate daily observations for each:

Facility × Medicine

combination.

Each observation should contain:

- date
- current_stock
- daily_consumption
- average_daily_consumption
- recent_consumption_trend
- minimum_stock
- safety_stock
- lead_time_days

## Target Generation

The synthetic generator will calculate:

`days_until_shortage`

based on simulated future consumption and stock behaviour.

This target is generated from the simulation logic and is used for supervised ML training.

## Dataset Size

The initial prototype should target approximately:

- 10–20 facilities
- 20–50 medicines
- 180–365 days of historical data

The final number of rows will depend on the selected combinations.

## Data Validation

After generation, validate:

- No negative stock
- No negative consumption
- Valid dates
- Valid facility IDs
- Valid medicine IDs
- Realistic consumption ranges
- No impossible lead times
- No duplicate observations

## Output

The generated dataset should be stored as CSV for the initial ML workflow.

Example:

`data/medicine_inventory.csv`

## Data Disclaimer

This dataset is entirely synthetic and does not represent real healthcare facility data.