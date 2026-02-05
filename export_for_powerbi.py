import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

# export tables
pd.read_sql("SELECT * FROM sales", conn).to_csv("sales_powerbi.csv", index=False)

conn.close()
print("Data exported for Power BI")
