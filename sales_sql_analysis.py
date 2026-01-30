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

conn.close()