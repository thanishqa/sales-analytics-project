"""
analyze.py
Sales & Customer Analytics Dashboard (script version)

Pipeline:
1. Load raw sales data
2. Clean & preprocess (handle missing values, fix inconsistent casing, drop bad rows)
3. Compute KPIs (total revenue, AOV, growth, top categories/regions)
4. Generate visualizations (matplotlib / seaborn)
5. Write an insights report (Markdown)
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_theme(style="whitegrid")
os.makedirs("charts", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ---------- 1. Load ----------
df = pd.read_csv("data/sales_data.csv", parse_dates=["OrderDate"])
raw_count = len(df)

# ---------- 2. Clean ----------
df["Region"] = df["Region"].str.strip().str.title()
df["Quantity"] = df["Quantity"].fillna(df["Quantity"].median())
df = df[df["Revenue"] > 0].copy()  # drop corrupted negative-revenue rows
cleaned_count = len(df)
df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

# ---------- 3. KPIs ----------
total_revenue = df["Revenue"].sum()
total_orders = len(df)
avg_order_value = df["Revenue"].mean()

monthly_revenue = df.groupby("Month")["Revenue"].sum().sort_index()
mom_growth = monthly_revenue.pct_change().iloc[-1] * 100

revenue_by_category = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
revenue_by_region = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)

# ---------- 4. Visualizations ----------
# Monthly revenue trend
plt.figure(figsize=(9, 4.5))
monthly_revenue.plot(marker="o", color="#2563eb")
plt.title("Monthly Revenue Trend (2025)")
plt.ylabel("Revenue (INR)")
plt.xlabel("Month")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_revenue_trend.png", dpi=150)
plt.close()

# Revenue by category
plt.figure(figsize=(7, 4.5))
sns.barplot(x=revenue_by_category.values, y=revenue_by_category.index, palette="Blues_d")
plt.title("Revenue by Product Category")
plt.xlabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("charts/revenue_by_category.png", dpi=150)
plt.close()

# Revenue by region (pie)
plt.figure(figsize=(6, 6))
plt.pie(revenue_by_region.values, labels=revenue_by_region.index, autopct="%1.1f%%", startangle=90)
plt.title("Revenue Share by Region")
plt.tight_layout()
plt.savefig("charts/revenue_by_region.png", dpi=150)
plt.close()

# Top 5 products
plt.figure(figsize=(7, 4.5))
sns.barplot(x=top_products.values, y=top_products.index, palette="Oranges_d")
plt.title("Top 5 Products by Revenue")
plt.xlabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("charts/top_products.png", dpi=150)
plt.close()

# ---------- 5. Insights report ----------
report = f"""# Sales & Customer Analytics - Insights Report

## Data Overview
- Raw records loaded: {raw_count}
- Records after cleaning (missing values imputed, invalid rows removed): {cleaned_count}

## Key Metrics
- **Total Revenue:** INR {total_revenue:,.2f}
- **Total Orders:** {total_orders}
- **Average Order Value (AOV):** INR {avg_order_value:,.2f}
- **Latest Month-over-Month Growth:** {mom_growth:.1f}%

## Top Category
**{revenue_by_category.index[0]}** generated the highest revenue at INR {revenue_by_category.iloc[0]:,.2f}.

## Top Region
**{revenue_by_region.index[0]}** leads with INR {revenue_by_region.iloc[0]:,.2f} in revenue
({(revenue_by_region.iloc[0] / total_revenue * 100):.1f}% of total).

## Top 5 Products
{top_products.to_string()}

## Charts Generated
- charts/monthly_revenue_trend.png
- charts/revenue_by_category.png
- charts/revenue_by_region.png
- charts/top_products.png
"""

with open("outputs/insights_report.md", "w") as f:
    f.write(report)

print("Analysis complete.")
print(report)
