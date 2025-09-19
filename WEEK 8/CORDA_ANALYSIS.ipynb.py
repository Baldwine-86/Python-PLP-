# CORD-19 Data Explorer
# Frameworks_Assignment
# By completing this notebook, I demonstrate:
# 1. Loading and exploring the metadata.csv dataset
# 2. Cleaning and preparing the data
# 3. Performing basic analysis and visualizations
# 4. Creating a simple Streamlit app
# 5. Documenting and reflecting on challenges

# Part 1: Setup and Data Loading
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import re

# Load dataset
df = pd.read_csv("metadata.csv", low_memory=False)

# Basic exploration
print("Shape of dataset:", df.shape)
print(df.info())
df.head()


# Part 2: Data Cleaning

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Handle missing values in titles
df['title'] = df['title'].fillna("Unknown Title")

# Create new column: word count in title
df['title_word_count'] = df['title'].apply(lambda x: len(x.split()))

# Check cleaned data
df[['title', 'year', 'title_word_count']].head()


# Part 3: Data Analysis & Visualizations

# Publications by year
year_counts = df['year'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
plt.bar(year_counts.index, year_counts.values, color='skyblue')
plt.title("Publications Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.show()


# Top journals
top_journals = df['journal'].value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis")
plt.title("Top 10 Journals")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.show()


# Common words in titles
titles = " ".join(df['title']).lower()
words = re.findall(r'\b\w+\b', titles)
common_words = Counter(words).most_common(15)

words_, counts = zip(*common_words)
plt.figure(figsize=(8, 5))
plt.barh(words_, counts, color="orange")
plt.title("Most Common Words in Titles")
plt.gca().invert_yaxis()
plt.show()


# Distribution of papers by source_x (dataset source)
source_counts = df['source_x'].value_counts().head(10)

plt.figure(figsize=(8, 5))
sns.barplot(y=source_counts.index, x=source_counts.values, palette="mako")
plt.title("Distribution of Papers by Source")
plt.xlabel("Number of Papers")
plt.ylabel("Source")
plt.show()
