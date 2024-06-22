# -*- coding: utf-8 -*-
"""Miniproject/DailyChallenge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XhqdumFHq9g-ZU2o5JO3HpBB2TE0Pxe7
"""

!pip install kaggle

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json


!kaggle datasets download -d ruchi798/data-science-job-salaries

!unzip data-science-job-salaries.zip

# Load the dataset into a DataFrame
df = pd.read_csv('ds_salaries.csv')

# Display the first 10 rows
print("First 10 rows of the dataset:")
print(df.head(10))

# Display data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Check for missing values in specific columns
print("\nMissing data check:")
missing_data = df[['experience_level', 'salary', 'salary_in_usd']].isnull().sum()
print(missing_data)

# Check for duplicates based on all columns
print("\nNumber of duplicate rows:")
duplicates = df.duplicated().sum()
print(duplicates)

# Group-wise analysis for experience_level
print("\nGroup-wise analysis of experience_level:")
grouped_df = df.groupby('experience_level')['salary_in_usd'].agg(['mean', 'median']).reset_index()
print(grouped_df)

# Create a bar chart for average salaries
# Define experience level order
exp_order = {'EN': 'Entry', 'MI': 'Mid', 'SE': 'Senior', 'EX': 'Executive'}
grouped_df['experience_level'] = pd.Categorical(grouped_df['experience_level'], categories=exp_order.keys(), ordered=True)
grouped_df = grouped_df.sort_values('experience_level')

# Plotting
plt.figure(figsize=(10, 6))
bars = plt.bar(grouped_df['experience_level'], grouped_df['mean'], color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])

# Add labels and title
plt.xlabel('Experience Level')
plt.ylabel('Average Salary in USD')
plt.title('Average Salary by Experience Level')

# Adding annotations
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2), ha='center', va='bottom')

# Customize x-axis labels
plt.xticks(ticks=grouped_df['experience_level'], labels=[exp_order[exp] for exp in grouped_df['experience_level']])

# Show the plot
plt.show()