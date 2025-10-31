import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# STEP 1: Create folder to save outputs
# -----------------------------
os.makedirs("visualization_output", exist_ok=True)

# -----------------------------
# STEP 2: Create Sample Dataset
# -----------------------------
np.random.seed(42)

dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq="D")
products = ["Laptop", "Mobile", "Tablet", "Headphones", "Camera"]
categories = ["Electronics", "Gadgets"]
regions = ["North", "South", "East", "West"]
salespeople = ["Ravi", "Keerthi", "Arun", "Divya", "Meena"]

data = {
    "Date": np.random.choice(dates, 500),
    "Product": np.random.choice(products, 500),
    "Category": np.random.choice(categories, 500),
    "Quantity": np.random.randint(1, 10, 500),
    "Price": np.random.randint(2000, 30000, 500),
    "Region": np.random.choice(regions, 500),
    "Salesperson": np.random.choice(salespeople, 500)
}

df = pd.DataFrame(data)
df.to_csv("visualization_output/sales_data.csv", index=False)
print(" Dataset 'sales_data.csv' created successfully!\n")

# -----------------------------
# STEP 3: Basic Calculations
# -----------------------------
df["Total_Sales"] = df["Quantity"] * df["Price"]

# -----------------------------
# STEP 4: Visualization
# -----------------------------
plt.style.use("seaborn-v0_8")

# 1️⃣ Sales by Product
plt.figure(figsize=(8, 5))
sns.barplot(x="Product", y="Total_Sales", data=df, estimator=sum, palette="viridis")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualization_output/sales_by_product.png")
plt.close()

# 2️⃣ Sales by Region
plt.figure(figsize=(8, 5))
sns.barplot(x="Region", y="Total_Sales", data=df, estimator=sum, palette="coolwarm")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualization_output/sales_by_region.png")
plt.close()

# 3️⃣ Quantity Sold Over Time (Line chart)
daily_sales = df.groupby("Date")["Total_Sales"].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.plot(daily_sales["Date"], daily_sales["Total_Sales"], color="purple")
plt.title("Daily Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualization_output/sales_over_time.png")
plt.close()

# 4️⃣ Top 5 Salespersons
top_sales = df.groupby("Salesperson")["Total_Sales"].sum().nlargest(5).reset_index()
plt.figure(figsize=(7, 5))
sns.barplot(x="Salesperson", y="Total_Sales", data=top_sales, palette="mako")
plt.title("Top 5 Salespersons by Total Sales")
plt.xlabel("Salesperson")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("visualization_output/top_salespersons.png")
plt.close()

# -----------------------------
# STEP 5: Completion Message
# -----------------------------
print(" All visualizations generated successfully!")
print("Check the 'visualization_output' folder for:")
print("- sales_data.csv (dataset)")
print("- sales_by_product.png")
print("- sales_by_region.png")
print("- sales_over_time.png")
print("- top_salespersons.png")
