# ---------------------------------------
# Task 1: Load and Explore the Dataset
# ---------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # optional, makes plots prettier

# 1. Load dataset (example: Iris dataset from seaborn)
try:
    df = sns.load_dataset("iris")   # you can also use pd.read_csv("your_dataset.csv")
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("Error: Dataset file not found.")

# Display first 5 rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean dataset (if needed)
df = df.dropna()   # or df.fillna(method='ffill')

# ---------------------------------------
# Task 2: Basic Data Analysis
# ---------------------------------------

# Basic statistics
print("\nStatistical Summary:")
print(df.describe())

# Group by categorical column (species) and compute mean of numerical columns
print("\nMean values grouped by species:")
print(df.groupby("species").mean())

# Example finding
print("\nObservation: Iris-virginica has the largest average petal length compared to other species.")

# ---------------------------------------
# Task 3: Data Visualization
# ---------------------------------------

# 1. Line chart (trend over index, e.g., sepal_length)
plt.figure(figsize=(8,5))
plt.plot(df.index, df["sepal_length"], label="Sepal Length", color="blue")
plt.title("Line Chart of Sepal Length over Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
df.groupby("species")["petal_length"].mean().plot(kind="bar", color=["red","green","blue"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal_width"], bins=15, color="purple", edgecolor="black")
plt.title("Histogram of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (relationship between sepal length and petal length)
plt.figure(figsize=(8,5))
plt.scatter(df["sepal_length"], df["petal_length"], c="orange")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
