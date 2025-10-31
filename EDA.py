# SALES DATA ANALYSIS PROJECT

import pandas as pd
import random

# ---- STEP 1: Generate Sample Sales Dataset ----
data = {
    "OrderID": list(range(1, 31)),
    "Date": pd.date_range(start="2024-01-01", periods=30),
    "CustomerID": [f"C{str(i).zfill(3)}" for i in range(1, 31)],
    "Product": random.choices(["Laptop", "Mobile", "Tablet", "Headphones", "Charger"], k=30),
    "Category": random.choices(["Electronics", "Accessories"], k=30),
    "Quantity": random.choices(range(1, 6), k=30),
    "Price": random.choices(range(5000, 60000, 5000), k=30),
    "Region": random.choices(["North", "South", "East", "West"], k=30),
    "SalesPerson": random.choices(["Keerthi", "Rajesh", "Divya", "Anand"], k=30)
}

df = pd.DataFrame(data)

# ---- STEP 2: Save Dataset in Same Folder ----
df.to_csv("sales_raw.csv", index=False)
print("Dataset created & saved successfully as 'sales_raw.csv'!\n")

# ---- STEP 3: Load Dataset (to verify) ----
df = pd.read_csv("sales_raw.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\n Dataset Shape (Rows, Columns):", df.shape)

print("\n Dataset Info:")
print(df.info())

print("\n Summary Statistics:")
print(df.describe())

print("\n Missing Values:")
print(df.isnull().sum())

# ---- STEP 4: Simple Insights ----
total_sales = (df["Quantity"] * df["Price"]).sum()
top_region = df["Region"].value_counts().idxmax()
top_salesperson = df["SalesPerson"].value_counts().idxmax()

print("\n Total Estimated Sales Amount:", total_sales)
print(" Region with Most Orders:", top_region)
print(" Top Salesperson:", top_salesperson)

print("\n Sales Data Analysis Completed Successfully!")
