# -*- coding: utf-8 -*-
"""Week9/day2/xp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SckhBYQPXskhC9B2cHodnf6jZczWDVQK
"""

!pip install kaggle

from google.colab import files
files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/

!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d shariful07/student-mental-health

!unzip student-mental-health.zip

import pandas as pd

df = pd.read_csv('Student Mental health.csv')

df.head()

# Exercise 1

import seaborn as sns
import matplotlib.pyplot as plt


plt.figure(figsize=(10, 6))
sns.histplot(df['What is your CGPA?'], kde=False, color='skyblue')

# Customize the histogram with a title
plt.title('Distribution of Students\' CGPA')
plt.xlabel('What is your CGPA?')
plt.ylabel('Frequency')

# Display the plot
plt.show()

# Check for unique values in the CGPA column
unique_cgpas = df['What is your CGPA?'].unique()
unique_cgpas

# Step 1: Strip whitespace from the values in the 'What is your CGPA?' column
df['What is your CGPA?'] = df['What is your CGPA?'].str.strip()

# Step 2: Check for unique values again to confirm the cleanup
unique_cgpas_cleaned = df['What is your CGPA?'].unique()
print(unique_cgpas_cleaned)

# Step 3: Create a histogram using the cleaned data
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.histplot(df['What is your CGPA?'], kde=False, color='skyblue')

# Customize the histogram with a title
plt.title('Distribution of Students\' CGPA')
plt.xlabel('CGPA')
plt.ylabel('Frequency')

# Display the plot
plt.show()

# Exercise 2

# Step 1: Clean and prepare the data
df['Choose your gender'] = df['Choose your gender'].str.strip()
df['Do you have Anxiety?'] = df['Do you have Anxiety?'].str.strip()

# Step 2: Calculate the proportion of students experiencing anxiety for each gender
anxiety_proportion = df[df['Do you have Anxiety?'] == 'Yes'].groupby('Choose your gender').size() / df.groupby('Choose your gender').size()

# Step 3: Convert the series to a DataFrame for easier plotting
anxiety_proportion_df = anxiety_proportion.reset_index(name='Proportion')
anxiety_proportion_df.columns = ['Gender', 'Proportion']

# Step 4: Create the bar plot
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.barplot(data=anxiety_proportion_df, x='Gender', y='Proportion', palette='viridis')

# Customize the plot with a title and labels
plt.title('Proportion of Students Experiencing Anxiety Across Different Genders')
plt.xlabel('Gender')
plt.ylabel('Proportion of Students with Anxiety')

# Display the plot
plt.show()

# Exercise 3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Convert the panic attack responses to numeric values (Yes=1, No=0)
df['Panic_attack_numeric'] = df['Do you have Panic attack?'].map({'Yes': 1, 'No': 0})

# Calculate the percentage of students with panic attacks for each age
panic_attack_percentage = df.groupby('Age')['Panic_attack_numeric'].mean() * 100

# Convert the result to a DataFrame for easier plotting
panic_attack_percentage_df = panic_attack_percentage.reset_index()
panic_attack_percentage_df.columns = ['Age', 'Panic_Attack_Percentage']

# Create the scatter plot with lines connecting the dots using Seaborn's lineplot
plt.figure(figsize=(10, 6))
sns.lineplot(data=panic_attack_percentage_df, x='Age', y='Panic_Attack_Percentage', marker='o', color='blue')

# Customize the plot with a title and labels
plt.title('Relationship Between Students\' Age and Occurrence of Panic Attacks')
plt.xlabel('Age')
plt.ylabel('Panic Attack Percentage')

# Display the plot
plt.show()

# Exercise 4

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv('Student Mental health.csv')

# Convert categorical columns to numeric values (Yes=1, No=0)
df['Do you have Depression?'] = df['Do you have Depression?'].map({'Yes': 1, 'No': 0})
df['Do you have Anxiety?'] = df['Do you have Anxiety?'].map({'Yes': 1, 'No': 0})
df['Do you have Panic attack?'] = df['Do you have Panic attack?'].map({'Yes': 1, 'No': 0})

# Convert CGPA ranges to midpoints for numerical representation
cgpa_mapping = {
    '3.00 - 3.49': 3.245,
    '3.50 - 4.00': 3.75,
    '2.50 - 2.99': 2.745,
    '2.00 - 2.49': 2.245,
    '0 - 1.99': 0.995
}
df['What is your CGPA?'] = df['What is your CGPA?'].map(cgpa_mapping)

# Select the subset of columns relevant to the exercise
columns_of_interest = ['Age', 'What is your CGPA?', 'Do you have Depression?', 'Do you have Anxiety?', 'Do you have Panic attack?']
subset_df = df[columns_of_interest]

# Rename columns for easier reference
subset_df.columns = ['Age', 'CGPA', 'Depression', 'Anxiety', 'Panic_Attack']

# Use Seaborn’s pairplot to visualize pairwise relationships and distributions
sns.pairplot(subset_df, hue='Anxiety', palette='viridis')

# Customize the plot with a title
plt.suptitle('Pairwise Relationships and Distributions of Selected Variables', y=1.02)

# Display the plot
plt.show()

# Exercise 5

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
file_path = '/content/Student Mental health.csv'
df = pd.read_csv(file_path)

# Step 2: Convert categorical variables to numeric values
df['Do you have Depression?'] = df['Do you have Depression?'].map({'Yes': 1, 'No': 0})
df['Do you have Anxiety?'] = df['Do you have Anxiety?'].map({'Yes': 1, 'No': 0})
df['Do you have Panic attack?'] = df['Do you have Panic attack?'].map({'Yes': 1, 'No': 0})

# Convert CGPA ranges to midpoints for numerical representation
cgpa_mapping = {
    '3.00 - 3.49': 3.245,
    '3.50 - 4.00': 3.75,
    '2.50 - 2.99': 2.745,
    '2.00 - 2.49': 2.245,
    '0 - 1.99': 0.995
}
df['What is your CGPA?'] = df['What is your CGPA?'].map(cgpa_mapping)

# Step 3: Select relevant columns
columns_of_interest = ['Age', 'What is your CGPA?', 'Do you have Depression?', 'Do you have Anxiety?', 'Do you have Panic attack?']
subset_df = df[columns_of_interest]

# Rename columns for easier reference
subset_df.columns = ['Age', 'CGPA', 'Depression', 'Anxiety', 'Panic_Attack']

# Step 4: Calculate the correlation matrix
correlation_matrix = subset_df.corr()

# Step 5: Create the heatmap using Seaborn
plt.figure(figsize=(10, 8))
heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)

# Customize the plot with a title
plt.title('Correlation Matrix of Age, CGPA, and Mental Health Indicators', size=16)

# Display the heatmap
plt.show()

# Exercise 6

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/content/Student Mental health.csv'
df = pd.read_csv(file_path)

# Convert categorical variables to numeric values
df['Do you have Depression?'] = df['Do you have Depression?'].map({'Yes': 1, 'No': 0})

# Convert CGPA ranges to specified integer values for numerical representation
cgpa_mapping = {
    '0 - 1.99': 1,
    '2.00 - 2.49': 2,
    '2.50 - 2.99': 3,
    '3.00 - 3.49': 4,
    '3.50 - 4.00': 5
}
df['What is your CGPA?'] = df['What is your CGPA?'].map(cgpa_mapping)

# Create a single plot for CGPA distribution by depression status with overlapping bars
plt.figure(figsize=(9, 6))
sns.histplot(data=df, x='What is your CGPA?', hue='Do you have Depression?',
             multiple='stack', bins=[1, 2, 3, 4, 5, 6], palette='viridis', kde=False)

# Customize x-axis labels to match the CGPA ranges and place them in the middle of each bar
plt.xticks(ticks=[1.5, 2.5, 3.5, 4.5, 5.5], labels=['0-1.99', '2.00-2.49', '2.50-2.99', '3.00-3.49', '3.50-4.00'])

# Add titles and labels
plt.title('Distribution of CGPA by Depression Status', size=16)
plt.xlabel('CGPA Range', size=14)
plt.ylabel('Count', size=14)
plt.legend(title='Depression Status', labels=['No', 'Yes'])

# Display the plot
plt.show()