import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# connect to database
conn = sqlite3.connect("sales.db")

kpi_queries = """
SELECT
    COUNT(DISTINCT OrderID) AS Total_Orders,
    SUM(Quantity * Price) AS Total_Revenue,
    ROUND(AVG(Quantity * Price), 2) AS Avg_Order_Value
FROM sales;
"""
kpis = pd.read_sql(kpi_queries, conn)

# revenue by product
product_query = """
SELECT Product, SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 5;
"""
product_df = pd.read_sql(product_query, conn)

# revenue by city
city_query = """
SELECT City, SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY City;
"""
city_df = pd.read_sql(city_query, conn)

# monthly revenue
month_query = """
SELECT strftime('%Y-%m', OrderDate) AS Month,
       SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month;
"""
month_df = pd.read_sql(month_query, conn)


plt.figure(figsize=(12, 8))

# KPI text
plt.subplot(2, 2, 2)
plt.axis("off")
plt.text(0.1, 0.8, f"Total Revenue: ${kpis['Total_Revenue'][0]}", fontsize=12)
plt.text(0.1, 0.6, f"Total Orders: {kpis['Total_Orders'][0]}", fontsize=12)
plt.text(0.1, 0.4, f"Avg Order Value: ${kpis['Avg_Order_Value'][0]}", fontsize=12)
plt.title("Sales KPIs")

# product revenue bar chart
plt.subplot(2, 2, 1)
plt.bar(product_df["Product"], product_df["Revenue"])
plt.title("Top Products by Revenue")
plt.xticks(rotation=45)

# city revenue
plt.subplot(2, 2, 3)
plt.bar(city_df["City"], city_df["Revenue"])
plt.title("Revenue by City")

# monthly trend
plt.subplot(2, 2, 4)
plt.plot(month_df["Month"], month_df["Revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

conn.close()
