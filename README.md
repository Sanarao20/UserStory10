# UserStory10
This project implements a Python-based Customer Order Analytics Engine designed to analyze customer purchasing behavior and classify customers into loyalty segments. The system processes customer master data and order transaction records to generate actionable analytics for business insights and marketing campaigns.

# Customer Order Analytics & Loyalty Classification Engine

## Overview
This project implements a **Python-based Customer Order Analytics Engine** designed to analyze customer purchasing behavior and classify customers into loyalty segments. The system processes customer data and order transactions to generate insights that can help businesses identify valuable customers and support marketing strategies.

The application reads customer and order datasets, validates and filters records based on defined business rules, calculates customer purchase metrics, and generates analytics reports.

## Features
- Load and process customer and order datasets
- Validate and filter order records
- Aggregate customer purchase metrics
- Classify customers into loyalty segments
- Determine customer activity status
- Generate analytics reports
- Implement logging for error handling
- Unit testing for core logic

## Input Data

### customers.csv
Contains customer master data.

Columns:
- `customer_id`
- `customer_name`
- `email`
- `status` (ACTIVE / INACTIVE)
- `signup_date`

### orders.csv
Contains order transaction data.

Columns:
- `order_id`
- `customer_id`
- `order_date`
- `order_amount`
- `order_status` (DELIVERED / CANCELLED / RETURNED)

## Processing Rules

### Order Filtering
- Only orders from **May 2024** are processed
- Invalid dates are ignored
- Negative order amounts are ignored
- Only **DELIVERED** orders count toward revenue

### Aggregation Metrics
For each customer the system calculates:
- `total_orders`
- `total_spent`
- `average_order_value`

Customers with no valid orders still appear in the final report.

## Loyalty Classification

Customers are classified based on total spending:

| Total Spent | Loyalty Segment |
|-------------|----------------|
| ≥ 10000 | PLATINUM |
| ≥ 5000 | GOLD |
| ≥ 1000 | SILVER |
| < 1000 | BRONZE |

## Customer Activity Status

| Condition | Status |
|----------|--------|
| ACTIVE customer with orders | ACTIVE_CUSTOMER |
| ACTIVE customer with zero orders | INACTIVE_CUSTOMER |
| INACTIVE customer | INACTIVE_CUSTOMER |

## Output Files

### customer_loyalty_report.csv
Contains customer analytics with the following fields:

- `customer_id`
- `customer_name`
- `total_orders`
- `total_spent`
- `average_order_value`
- `loyalty_segment`
- `customer_activity_status`

### analytics_summary.json
Contains overall metrics:

- total_customers
- active_customers
- inactive_customers
- platinum_customers
- gold_customers
- silver_customers
- bronze_customers
- total_revenue

## Project Structure

```
project/
│
├── data/
│   ├── customers.csv
│   └── orders.csv
│
├── src/
│   ├── loader.py
│   ├── order_processor.py
│   ├── loyalty_engine.py
│   ├── reporter.py
│   └── main.py
│
├── tests/
│   ├── test_order_processor.py
│   └── test_loyalty_engine.py
│
├── logs/
│   └── analytics.log
```

## Running the Application

Run the analytics engine using:

```bash
python src/main.py
```

## Running Unit Tests

Execute tests using:

```bash
python -m unittest discover tests
```


## Logging

The system logs processing information and errors in:

```
logs/analytics.log
```

Examples of logged events:
- Invalid order dates
- Negative order amounts
- Unknown customer IDs


## Technologies Used
- Python
- CSV and JSON processing
- Logging module
- unittest framework
