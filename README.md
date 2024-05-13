# Amazon Review Data Analysis and Performed EDA

## Overview
This project focuses on Exploratory Data Analysis (EDA) of a dataset sourced from Amazon. The main objectives include importing necessary libraries, performing data cleaning, understanding the dataset, exploring it through various statistical measures, and visualizing key insights.

## Dataset
The dataset used in this project is sourced from Amazon.

This dataset is having the data of 1K+ Amazon Product's Ratings and Reviews as per their details listed on the official website of Amazon¶

**Column Descriptors**
* product_id - Product ID
* product_name - Name of the Product
* category - Category of the Product
* discounted_price - Discounted Price of the Product
* actual_price - Actual Price of the Product
* discount_percentage - Percentage of Discount for the Product
* rating - Rating of the Product
* rating_count - Number of people who voted for the Amazon rating
* about_product - Description about the Product
* user_id - ID of the user who wrote review for the Product
* user_name - Name of the user who wrote review for the Product
* review_id - ID of the user review
* review_title - Short review
* review_content - Long review
* img_link - Image Link of the Product
* product_link - Official Website Link of the Product


## Contents
1. [Introduction](#introduction)
2. [Importing Python Modules](#importing-python-modules)
3. [Dataset Overview](#dataset-overview)
4. [Data Cleaning](#data-cleaning)
5. [Data Understanding](#data-understanding)
6. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
7. [Data Exploration and Visualization](#data-exploration-and-visualization)
8. [Conclusion](#conclusion)

## Introduction

- Welcome to our Amazon Product Dataset Exploratory Data Analysis (EDA) project.
- In this project, we delve into a comprehensive analysis of Amazon product data, aiming to uncover valuable insights and trends.
- Through rigorous data cleaning, exploration, and visualization techniques, we aim to provide a deeper understanding of the dataset and its underlying characteristics.
- Join us on this journey as we explore the fascinating world of Amazon products through data.


[Provide a brief introduction to the project, its objectives, and the dataset used.]

## Dataset Overview

* Shape of the data is 1462 Columns & 24 Rows.
* The dataset encompasses attributes associated with Amazon products and user reviews.
* Columns include product ID, name, category, and pricing details (discounted and actual).
* Additional columns feature the discount percentage, average rating, and rating count.
* User-related attributes consist of user ID and name.
* Review details include review ID, title, and content.
* Links to product images and pages complement the dataset.
* These attributes collectively offer profound insights into product characteristics, user feedback, and pricing dynamics, facilitating comprehensive analysis and interpretation.

## Importing Python Modules:
We will use the following libraries¶
1. Pandas: Data manipulation and analysis
2. Numpy: Numerical operations and calculations
3. Matplotlib: Data visualization and plotting
4. Seaborn: Enhanced data visualization and statistical graphics¶

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

*Following these steps, the dataset was cleaned and prepared for further analysis.*

*The cleaned dataset was confirmed to have no missing values, ensuring the reliability of the subsequent analysis.*


## Data Understanding

Before diving into exploratory analysis, it's essential to understand the structure and characteristics of the dataset. 

The following steps were taken:

1. **Descriptive Statistics:**
   Summary statistics such as count, mean, standard deviation, min, max, and quartiles were computed for numeric columns using the `describe()` method. This provided an overview of the distribution and central tendencies of the numerical features.

2. **Descriptive Statistics for Categorical Columns:**
   Summary statistics for categorical columns, including count, unique, top, and frequency, were obtained using the `describe(include=object)` method. This helped understand the frequency and distribution of categorical values.

3. **Dataset Information:**
   The `info()` method was used to obtain:
   * Concise summary of the dataset, including the data types of each column. 
   * The presence of missing values. 
   * Identification of any potential data type inconsistencies or missing values.

*By understanding the dataset's structure and characteristics, we gained insights into its key features and prepared for the subsequent exploratory data analysis (EDA) phase.*


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


