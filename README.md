# Amazon-Review-Data-EDA-Project

## Overview
This project focuses on Exploratory Data Analysis (EDA) of a dataset sourced from Amazon. The main objectives include importing necessary libraries, performing data cleaning, understanding the dataset, exploring it through various statistical measures, and visualizing key insights.

## Dataset
The dataset used in this project is sourced from Amazon.
This dataset is having the data of 1K+ Amazon Product's Ratings and Reviews as per their details listed on the official website of Amazon¶
Features
product_id - Product ID
product_name - Name of the Product
category - Category of the Product
discounted_price - Discounted Price of the Product
actual_price - Actual Price of the Product
discount_percentage - Percentage of Discount for the Product
rating - Rating of the Product
rating_count - Number of people who voted for the Amazon rating
about_product - Description about the Product
user_id - ID of the user who wrote review for the Product
user_name - Name of the user who wrote review for the Product
review_id - ID of the user review
review_title - Short review
review_content - Long review
img_link - Image Link of the Product
product_link - Official Website Link of the Product


## Contents
1. [Introduction](#introduction)
2. [Dataset Overview](#dataset-overview)
3. [Data Cleaning](#data-cleaning)
4. [Data Understanding](#data-understanding)
5. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6. [Data Exploration and Visualization](#data-exploration-and-visualization)
7. [Conclusion](#conclusion)

## Introduction
[Provide a brief introduction to the project, its objectives, and the dataset used.]

## Dataset Overview
[Describe the dataset briefly, including its size, features, and any relevant background information.]


## Importing Library:
We will use the following libraries¶
1. Pandas: Data manipulation and analysis
2. Numpy: Numerical operations and calculations
3. Matplotlib: Data visualization and plotting
4. Seaborn: Enhanced data visualization and statistical graphics¶

## Data Cleaning
Handling Missing Values: Identify and address missing values in the dataset through imputation or removal.

Data Type Conversion: Ensure consistency and appropriateness of data types for analysis.

Removing Special Characters: Eliminate unnecessary symbols or formatting characters that may hinder analysis.

Standardizing Values: Ensure uniform representation of data values, including units and formats.

Detecting and Handling Outliers: Identify and address outliers to prevent skewed analysis results.

Handling Duplicates: Detect and remove duplicate records to avoid bias in analysis.

Data Transformation: Transform data to meet analysis requirements, such as scaling or normalization.

## Data Cleaning
The dataset underwent a series of cleaning steps to ensure its quality and usability for analysis. Here's a summary of the data cleaning process:

1. **Handling Missing Values:**
   The `isnull().sum()` method was used to identify missing values in the dataset. After identifying the columns with missing values, those rows were either dropped or imputed with appropriate values to maintain data integrity.

2. **Data Type Conversion:**
   Certain numeric columns such as 'discounted_price', 'actual_price', 'discount_percentage', 'rating', and 'rating_count' contained special characters like currency symbols and percentage signs. These were removed using string manipulation techniques (`str.replace()`) and the columns were then converted to numeric data type using `astype(float)`.

3. **Handling Special Characters:**
   Special characters such as currency symbols ('₹') and percentage signs were removed from numeric columns to facilitate numerical computations.

4. **Removing Unnecessary Characters:**
   Characters such as commas (',') and vertical bars ('|') were removed from numeric columns to ensure consistency and enable proper data conversion.

5. **Removing Rows with Missing Values:**
   After cleaning, rows with any remaining missing values were dropped from the dataset using the `dropna()` method to ensure the completeness of the data for analysis.

Following these steps, the dataset was cleaned and prepared for further analysis. The cleaned dataset was then used for Exploratory Data Analysis (EDA) to gain insights and extract meaningful information.

The cleaned dataset was confirmed to have no missing values, ensuring the reliability of the subsequent analysis.


[Detail the steps taken to clean the data, including handling missing values, removing duplicates, and any other necessary preprocessing steps.]

## Data Understanding
The purpose of a sneak peek is to get a quick overview of the data and identify any potential problems or areas of interest.
[Discuss the initial exploration of the dataset, such as descriptive statistics, data types, and basic insights gained.]

## Exploratory Data Analysis (EDA)
[Provide a deeper analysis of the dataset, including correlation analysis, distribution of key features, and any patterns or trends discovered.]

## Data Exploration and Visualization
[Present visualizations of the dataset, including histograms, scatter plots, and other relevant plots to illustrate key insights.]

## Conclusion
[Summarize the findings of the EDA process, highlight any significant discoveries or insights, and discuss potential next steps or areas for further investigation.]

## Getting Started
[Include instructions on how to clone and run the project locally, as well as any prerequisites or dependencies.]

## Contributors
[List the contributors to the project, including their roles and contributions.]

## License
[Specify the license under which the project is distributed, if applicable.]

