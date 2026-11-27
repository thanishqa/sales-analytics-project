"""
generate_data.py
Generates a synthetic retail sales dataset used by analyze.py.
"""
import numpy as np
import pandas as pd

np.random.seed(42)

N = 2000
regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Clothing", "Groceries", "Furniture", "Toys"]
products = {
    "Electronics": ["Headphones", "Smartphone", "Laptop", "Smartwatch"],
    "Clothing": ["T-Shirt", "Jeans", "Jacket", "Sneakers"],
    "Groceries": ["Rice 5kg", "Cooking Oil", "Snacks Pack", "Beverages"],
    "Furniture": ["Office Chair", "Study Table", "Bookshelf", "Sofa"],
    "Toys": ["Puzzle Set", "Remote Car", "Building Blocks", "Board Game"],
}

dates = pd.date_range("2025-01-01", "2025-12-31", freq="D")

rows = []
for i in range(N):
    date = np.random.choice(dates)
    region = np.random.choice(regions, p=[0.3, 0.25, 0.25, 0.2])
    category = np.random.choice(categories)
    product = np.random.choice(products[category])
    unit_price = {
        "Electronics": np.random.uniform(1000, 60000),
        "Clothing": np.random.uniform(300, 3000),
        "Groceries": np.random.uniform(50, 800),
        "Furniture": np.random.uniform(1500, 25000),
        "Toys": np.random.uniform(200, 2500),
    }[category]
    quantity = np.random.randint(1, 6)
    discount_pct = np.random.choice([0, 0, 0, 5, 10, 15, 20], p=[0.35,0.15,0.1,0.15,0.1,0.1,0.05])
    revenue = unit_price * quantity * (1 - discount_pct / 100)

    # occasionally introduce messy / missing data to make cleaning meaningful
    if np.random.rand() < 0.03:
        quantity = np.nan
    if np.random.rand() < 0.02:
        region = region.lower()  # inconsistent casing
    if np.random.rand() < 0.01:
        revenue = -abs(revenue)  # bad data: negative revenue

    rows.append({
        "OrderDate": pd.Timestamp(date),
        "Region": region,
        "Category": category,
        "Product": product,
        "UnitPrice": round(unit_price, 2),
        "Quantity": quantity,
        "DiscountPct": discount_pct,
        "Revenue": round(revenue, 2),
    })

df = pd.DataFrame(rows)
df.to_csv("data/sales_data.csv", index=False)
print(f"Generated {len(df)} rows -> data/sales_data.csv")
