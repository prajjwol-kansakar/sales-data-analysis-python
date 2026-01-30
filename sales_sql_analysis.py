import sqlite3
import pandas as pd

df = pd.read_csv("sales_data.csv")

conn = sqlite3.connect("sales.db")

df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded into SQLite database.")



query = """
SELECT 
    Product,
    SUM(Quantity * Price) AS Total_Revenue
FROM sales
GROUP BY Product
ORDER BY Total_Revenue DESC;
"""


result = pd.read_sql(query, conn)
print(result)


query_city = """
SELECT 
    City,
    SUM(Quantity * Price) AS Total_Revenue
FROM sales
GROUP BY City
ORDER BY Total_Revenue DESC;
"""


city_sql = pd.read_sql(query_city, conn)
print(city_sql)

query_all = """
SELECT * from sales
ORDER BY OrderDate DESC;
"""

all_data = pd.read_sql(query_all, conn)
print(all_data.head())



monthly_query = """
SELECT 
    strftime('%Y-%m', OrderDate) AS Month,
    SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Month
ORDER BY Month;
"""

monthly_sql = pd.read_sql(monthly_query, conn)
print(monthly_sql)


# Who are our high-value customers?
query = """
SELECT
    OrderID,
    City,
    SUM(Quantity * Price) AS Order_Value
FROM sales
GROUP BY OrderID, City
ORDER BY Order_Value DESC;
"""

order_value = pd.read_sql(query, conn)
print(order_value)

# Which orders are above average value?

query = """
SELECT *
FROM (
    SELECT
        OrderID,
        SUM(Quantity * Price) AS Order_Value
    FROM sales
    GROUP BY OrderID
)
WHERE Order_Value >
    (SELECT AVG(Quantity * Price) FROM sales);
"""

high_value_orders = pd.read_sql(query, conn)
print(high_value_orders)


# Classify orders into Low / Medium / High value

query = """
SELECT
    OrderID,
    SUM(Quantity * Price) AS Revenue,
    CASE
        WHEN SUM(Quantity * Price) >= 1000 THEN 'High Value'
        WHEN SUM(Quantity * Price) BETWEEN 500 AND 999 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS Order_Category
FROM sales
GROUP BY OrderID;
"""

order_segments = pd.read_sql(query, conn)
print(order_segments)

# What are the top 3 products by revenue?

query = """
SELECT
    Product,
    SUM(Quantity * Price) AS Revenue
FROM sales
GROUP BY Product
ORDER BY Revenue DESC
LIMIT 3;
"""

top_products_sql = pd.read_sql(query, conn)
print(top_products_sql)

# KPI Dashboard Query

query = """
SELECT
    COUNT(DISTINCT OrderID) AS Total_Orders,
    SUM(Quantity) AS Total_Quantity,
    SUM(Quantity * Price) AS Total_Revenue,
    ROUND(AVG(Quantity * Price), 2) AS Avg_Order_Value
FROM sales;
"""

kpi_sql = pd.read_sql(query, conn)
print(kpi_sql)


conn.close()