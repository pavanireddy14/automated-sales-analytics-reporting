
# DATA CLEANING & PREPROCESSING

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# 1️ Load Dataset
df = pd.read_csv("C:/projects/data analysis project 1/dataset/SampleSuperstore.csv")

print("Dataset Loaded Successfully!")
print("Initial Shape:", df.shape)
print("\nColumns:\n", df.columns)

# 2️ Check Missing Values
print("\nMissing Values:\n", df.isna().sum())

# 3️ Remove Duplicates
df = df.drop_duplicates()
print("\nShape After Removing Duplicates:", df.shape)

# 4️ Convert Data Types (if needed)
# Ensure numeric columns are correct
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')

# 5️ Handle Missing Values (if any appear after conversion)
df = df.fillna(0)

# 6️ Create New Feature: Profit Margin
df['Profit Margin'] = np.where(
    df['Sales'] != 0,
    df['Profit'] / df['Sales'],
    0
)

print("\nNew Column Added: Profit Margin")

# 7️ Create Category Summary
category_summary = df.groupby('Category')[['Sales', 'Profit']].sum().round(2)

# 8️ Create Region Summary
region_summary = df.groupby('Region')[['Sales', 'Profit']].sum().round(2)

# 9️ Create Sub-Category Summary
subcategory_summary = df.groupby('Sub-Category')[['Sales', 'Profit']].sum().round(2)

#  Save Cleaned Dataset
df.to_csv("cleaned_superstore.csv", index=False)
category_summary.to_csv("category_summary.csv")
region_summary.to_csv("region_summary.csv")
subcategory_summary.to_csv("subcategory_summary.csv")

print("\nCleaned files saved successfully!")

# 1️1 Print Key Summaries
print("\nCategory Summary:\n", category_summary)
print("\nRegion Summary:\n", region_summary)
print("\nSub-Category Summary:\n", subcategory_summary)

print("\nData Cleaning Completed Successfully!")

# Category Profit Chart
plt.figure(figsize=(6,4))
category_summary['Profit'].plot(kind='bar')
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("category_profit.png")
plt.close()

# Region Profit Chart
plt.figure(figsize=(6,4))
region_summary['Profit'].plot(kind='bar')
plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("region_profit.png")
plt.close()

print("Charts saved successfully!")