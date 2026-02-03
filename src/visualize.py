import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../data/processed/clean_sales.csv")

output_dir = "../Visualizations"
os.makedirs(output_dir, exist_ok=True)

# 1. Sales by Branch
plt.figure()
df.groupby("Branch")["Price"].sum().plot(kind="bar")
plt.title("Total Sales by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Sales (£)")
plt.tight_layout()
plt.savefig(f"{output_dir}/sales_by_branch.png")
plt.show()

# 2. Profit by Branch
plt.figure()
df.groupby("Branch")["Profit"].sum().plot(kind="bar")
plt.title("Total Profit by Branch")
plt.xlabel("Branch")
plt.ylabel("Total Profit (£)")
plt.tight_layout()
plt.savefig(f"{output_dir}/profit_by_branch.png")
plt.show()

# 3. Payment Method Distribution
plt.figure()
df["Payment_Type"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(f"{output_dir}/payment_distribution.png")
plt.show()

# 4. Product Popularity
plt.figure()
df["Product"].value_counts().plot(kind="bar")
plt.title("Most Popular Products")
plt.xlabel("Product")
plt.ylabel("Number of Sales")
plt.tight_layout()
plt.savefig(f"{output_dir}/product_popularity.png")
plt.show()
