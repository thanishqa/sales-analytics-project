# Sales & Customer Analytics Dashboard

A Python data analytics project that cleans, analyzes, and visualizes retail sales data to surface
revenue trends, top categories/regions, and top-selling products.

## Tech Stack
Python, Pandas, NumPy, Matplotlib, Seaborn

## What it does
1. **generate_data.py** – creates a synthetic (but realistic) retail sales dataset of 2,000 orders
   across regions, categories, and products, deliberately including messy data (missing values,
   inconsistent casing, a few invalid rows) to simulate real-world data.
2. **analyze.py** – the core pipeline:
   - Cleans the data (imputes missing quantities, standardizes region names, removes invalid rows)
   - Computes KPIs: total revenue, total orders, average order value, month-over-month growth
   - Generates 4 charts (monthly trend, revenue by category, revenue share by region, top products)
   - Writes `outputs/insights_report.md` summarizing the findings

## How to run
```bash
pip install -r requirements.txt
python generate_data.py   # creates data/sales_data.csv
python analyze.py         # creates charts/ and outputs/insights_report.md
```

## Project Structure
```
sales-analytics-project/
├── generate_data.py
├── analyze.py
├── requirements.txt
├── data/
│   └── sales_data.csv
├── charts/
│   ├── monthly_revenue_trend.png
│   ├── revenue_by_category.png
│   ├── revenue_by_region.png
│   └── top_products.png
└── outputs/
    └── insights_report.md
```

## Resume bullet points used for this project
- Performed data cleaning and exploratory data analysis (EDA) on a 2,000-record retail sales dataset
  using Pandas and NumPy, handling missing values and inconsistent entries.
- Built visual dashboards (trend, category, regional, and product-level charts) using Matplotlib and
  Seaborn to identify revenue drivers.
- Generated an automated insights report summarizing KPIs such as revenue growth, top categories,
  and top-performing regions.
