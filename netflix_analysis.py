import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("netflix_titles.csv")

# Basic info
print("Dataset Shape:", df.shape)

# Data Cleaning
df = df.dropna(subset=['country', 'listed_in'])

# Movies vs TV Shows
print("\nContent Type Count:")
print(df['type'].value_counts())

# Top 5 Countries
print("\nTop 5 Countries:")
print(df['country'].value_counts().head())

# Top 5 Genres
print("\nTop 5 Genres:")
print(df['listed_in'].value_counts().head())

# Visualization
df['type'].value_counts().plot(kind='bar')
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()