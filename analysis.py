import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

# # create revenue column
df["Revenue"] = df["Quantity"] * df["Price"]

# KPIs
total_orders = df["OrderID"].nunique()
total_quantity = df["Quantity"].sum()
average_order_value = df["Revenue"].mean()

print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Average Order Value:", round(average_order_value, 2))


# top products by quantity sold
top_quantity = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print(top_quantity)

# category-wise revenue
category_revenue = df.groupby("Category")["Revenue"].sum()

print(category_revenue)

# revenue by product
product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

product_revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)

plt.show()

"""
BUSINESS INSIGHTS:
1. Laptop is the highest revenue-generating product.
2. February 2024 recorded the highest monthly revenue.
3. Chicago is the top-performing city.
4. Electronics category contributes most of the revenue.
5. Accessories sell in higher quantity but generate less revenue.
"""

# # print(df.head())
# # print(df.info())



# # total_revenue = df["Revenue"].sum()
# # print("Total Revenue:", total_revenue)

# # revenue by product
# # product_revenue = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)

# # print(product_revenue)

# # convert OrderDate to datetime
# df["OrderDate"] = pd.to_datetime(df["OrderDate"])

# # # create month column
# df["Month"] = df["OrderDate"].dt.to_period("M")

# # # monthly revenue
# monthly_revenue = df.groupby("Month")["Revenue"].sum()

# # print(monthly_revenue)

# city_revenue = df.groupby("City")["Revenue"].sum().sort_values(ascending=False)

# # print(city_revenue)

# city_revenue.plot(kind="bar")

# plt.title("Revenue by City")
# plt.xlabel("City")
# plt.ylabel("Revenue")

# plt.show()

# # plot monthly revenue trend
# monthly_revenue.plot()

# plt.title("Monthly Revenue Trend")
# plt.xlabel("Month")
# plt.ylabel("Revenue")

# plt.show()