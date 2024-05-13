-- Importing necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

-- LOAD DATA:
data = pd.read_csv('amazon.csv') #Read the CSV File.

data.head() #Checking and have a look of the Head and Top 5 Row of Data.

-- DATA CLEANING:
data.isnull().sum() #Checking Null Value. 

#convert Dtype and removing the symbol from the data
numeric_columns = ['discounted_price', 'actual_price', 'discount_percentage', 'rating', 'rating_count']
for column in numeric_columns:
    data[column] = data[column].astype(str).str.replace(',', '').str.replace('₹', '').str.replace('%', '').str.replace('|', '')
    data[column] = data[column].apply(lambda x: float(x) if x.strip() else None)

# Droping null values
data = data.dropna()
data.isnull().sum()

-- DATA UNDERSTANDING:
# Describe the data and print Statistical view
data.describe()
data.describe(include=object)

-- DATA EXPLORATION:
## After cleaning the data checking the Head of the data 
data.head()

#info of the data
data.info()

#Checking the Shape of the data
data.shape

-- FINDING INSIGHTS AFTER CLEANING THE DATA
 ## How are product prices distributed, and are there notable outliers?
price_columns = ['discounted_price', 'actual_price']
data[price_columns] = data[price_columns].replace('[\₹,]', '', regex=True).astype(float)

# Calculate summary statistics
price_summary = data[price_columns].describe()

# Plot boxplot to visualize the distribution and identify outliers
plt.figure(figsize=(10, 6))
data[price_columns].boxplot()
plt.title('Distribution of Product Prices')
plt.ylabel('Price (INR)')
plt.xticks(range(1, len(price_columns) + 1), price_columns)
plt.show()

# Print summary statistics
print("Summary Statistics of Product Prices:")
print(price_summary)

## What is the average rating across different product categories ?
# Group the data by 'category' and calculate the average rating for each category
average_rating_by_category = data.groupby('category')['rating'].mean()

# Print or display the average ratings for each category
print("Average Rating Across Different Product Categories:")

print(average_rating_by_category)

average_rating_by_category = data.groupby('category')['rating'].mean().sort_values(ascending=False)

# Plotting
plt.figure(figsize=(10, 6))
average_rating_by_category.plot(kind='barh', color='skyblue')
plt.title('Average Rating Across Different Product Categories')
plt.xlabel('Product Category')
plt.ylabel('Average Rating')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Print average rating by category
print("Average Rating Across Different Product Categories:")
print(average_rating_by_category)
