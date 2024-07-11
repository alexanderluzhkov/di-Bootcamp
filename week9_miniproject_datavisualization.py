# -*- coding: utf-8 -*-
"""Week9/Miniproject/datavisualization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1luZn9nd276d3mG2jJQlj3dzU1sNBuB5-
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv'

penguins_df = pd.read_csv(url)

penguins_df.head()

# Display the data types of all columns
print("Data Types of All Columns:")
print(penguins_df.dtypes)

# Display the amount of missing values in each column
print("\nAmount of Missing Values in Each Column:")
print(penguins_df.isnull().sum())

print("\nTotal Number of Rows in the Dataset:")
print(len(penguins_df))

print("\nRows with Missing Values:")
rows_with_missing_values = penguins_df[penguins_df.isnull().any(axis=1)]
print(rows_with_missing_values)

# Drop all rows with missing 'Sex' values
penguins_df = penguins_df.dropna(subset=['sex'])

# Reset the index to maintain sequential order
penguins_df = penguins_df.reset_index(drop=True)

# Display the updated DataFrame
print("\nUpdated DataFrame after Deleting Rows with Missing 'Sex' Values:")
print(penguins_df)

# Display the total number of rows in the updated DataFrame
print("\nTotal Number of Rows in the Updated DataFrame:")
print(len(penguins_df))

# Summary statistics
summary_stats = penguins_df.describe(include='all')

# Unique values in each column
unique_values = penguins_df.nunique()

# Range of each numeric column
ranges = penguins_df.select_dtypes(include='number').agg(['min', 'max'])


# Display the results
print("Summary Statistics:")
print(summary_stats)
print("\nUnique Values in Each Column:")
print(unique_values)
print("\nRange of Each Numeric Column:")
print(ranges)

# Create a bar chart for the distribution of penguin species
species_counts = penguins_df['species'].value_counts()
species_counts.plot(kind='bar', color='skyblue')

# Add titles and labels
plt.title('Distribution of Penguin Species')
plt.xlabel('Species')
plt.ylabel('Count')

# Display the bar chart
plt.show()

# Create a scatter plot for flipper length vs body mass, color-coded by species
species_unique = penguins_df['species'].unique()
colors = {'Adelie':'blue', 'Gentoo':'green', 'Chinstrap':'red'}

plt.figure(figsize=(10, 6))

for species in species_unique:
    subset = penguins_df[penguins_df['species'] == species]
    plt.scatter(subset['flipper_length_mm'], subset['body_mass_g'],
                color=colors[species], label=species, alpha=0.6)

# Add titles and labels
plt.title('Flipper Length vs Body Mass by Species')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')
plt.legend(title='Species')

# Display the scatter plot
plt.show()

# Create a pie chart for the count of penguins on each island
island_counts = penguins_df['island'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(island_counts, labels=island_counts.index, autopct='%1.1f%%', startangle=140, colors=['skyblue', 'lightgreen', 'lightcoral'])

# Add title
plt.title('Penguin Count on Each Island')

# Display the pie chart
plt.show()

# Create a grouped bar chart for the distribution of sex within each penguin species
species_sex_counts = penguins_df.groupby(['species', 'sex']).size().unstack()

species_sex_counts.plot(kind='bar', figsize=(10, 6), color=['skyblue', 'lightgreen'])

# Add titles and labels
plt.title('Distribution of Sex Within Each Penguin Species')
plt.xlabel('Species')
plt.ylabel('Count')
plt.legend(title='Sex')

# Display the bar chart
plt.show()

# Select the numerical variables
numerical_vars = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

# Calculate the correlation matrix
correlation_matrix = penguins_df[numerical_vars].corr()

# Create a heatmap to visualize the correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')

# Add title
plt.title('Correlation Heatmap of Numerical Variables')

# Display the heatmap
plt.show()

# Set the figure size
plt.figure(figsize=(15, 10))

# Create a boxplot for flipper_length_mm segmented by species
plt.subplot(2, 2, 1)
sns.boxplot(x='species', y='flipper_length_mm', data=penguins_df)
plt.title('Flipper Length (mm) by Species')

# Create a boxplot for body_mass_g segmented by species
plt.subplot(2, 2, 2)
sns.boxplot(x='species', y='body_mass_g', data=penguins_df)
plt.title('Body Mass (g) by Species')

# Create a boxplot for bill_length_mm segmented by species
plt.subplot(2, 2, 3)
sns.boxplot(x='species', y='bill_length_mm', data=penguins_df)
plt.title('Bill Length (mm) by Species')

# Create a boxplot for bill_depth_mm segmented by species
plt.subplot(2, 2, 4)
sns.boxplot(x='species', y='bill_depth_mm', data=penguins_df)
plt.title('Bill Depth (mm) by Species')

# Adjust layout
plt.tight_layout()

# Display the boxplots
plt.show()

# Set the figure size
plt.figure(figsize=(15, 5))

# Create a histogram for bill length
plt.subplot(1, 3, 1)
sns.histplot(penguins_df['bill_length_mm'], bins=20, kde=True)
plt.title('Distribution of Bill Length (mm)')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Frequency')

# Create a histogram for bill depth
plt.subplot(1, 3, 2)
sns.histplot(penguins_df['bill_depth_mm'], bins=20, kde=True)
plt.title('Distribution of Bill Depth (mm)')
plt.xlabel('Bill Depth (mm)')
plt.ylabel('Frequency')

# Create a histogram for flipper length
plt.subplot(1, 3, 3)
sns.histplot(penguins_df['flipper_length_mm'], bins=20, kde=True)
plt.title('Distribution of Flipper Length (mm)')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Frequency')

# Drop the 'year' column
penguins_df = penguins_df.drop(columns=['year'])

# Create a pairplot to visualize pairwise relationships
pairplot = sns.pairplot(penguins_df, hue='species', diag_kind='kde')

# Add a title
pairplot.fig.suptitle('Pairwise Relationships in the Palmer Penguins Dataset', y=1.02)

# Display the pairplot
plt.show()

# Create a histogram for the count of species on each island
sns.histplot(data=penguins_df, x='island', hue='species', multiple='stack', shrink=0.8)

# Add titles and labels
plt.title('Count of Penguin Species on Each Island')
plt.xlabel('Island')
plt.ylabel('Count')

# Display the histogram
plt.show()

# Filter the dataset for Adelie penguins
adelie_df = penguins_df[penguins_df['species'] == 'Adelie']

# Set the figure size
plt.figure(figsize=(20, 10))

# Create a boxplot for flipper_length_mm segmented by island
plt.subplot(2, 2, 1)
sns.boxplot(x='island', y='flipper_length_mm', data=adelie_df)
plt.title('Flipper Length (mm) for Adelie Penguins by Island')
plt.xlabel('Island')
plt.ylabel('Flipper Length (mm)')

# Create a boxplot for body_mass_g segmented by island
plt.subplot(2, 2, 2)
sns.boxplot(x='island', y='body_mass_g', data=adelie_df)
plt.title('Body Mass (g) for Adelie Penguins by Island')
plt.xlabel('Island')
plt.ylabel('Body Mass (g)')

# Create a boxplot for bill_length_mm segmented by island
plt.subplot(2, 2, 3)
sns.boxplot(x='island', y='bill_length_mm', data=adelie_df)
plt.title('Bill Length (mm) for Adelie Penguins by Island')
plt.xlabel('Island')
plt.ylabel('Bill Length (mm)')

# Create a boxplot for bill_depth_mm segmented by island
plt.subplot(2, 2, 4)
sns.boxplot(x='island', y='bill_depth_mm', data=adelie_df)
plt.title('Bill Depth (mm) for Adelie Penguins by Island')
plt.xlabel('Island')
plt.ylabel('Bill Depth (mm)')

# Adjust layout
plt.tight_layout()

# Display the boxplots
plt.show()

# Filter out Gentoo penguins
penguins_no_gentoo = penguins_df[penguins_df['species'] != 'Gentoo']

# Select the numerical variables
numerical_vars_no_gentoo = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g']

# Calculate the correlation matrix without Gentoo penguins
correlation_matrix_no_gentoo = penguins_no_gentoo[numerical_vars_no_gentoo].corr()

# Create a heatmap to visualize the correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_no_gentoo, annot=True, cmap='coolwarm', fmt='.2f')

# Add title
plt.title('Correlation Heatmap of Numerical Variables (Without Gentoo Penguins)')

# Display the heatmap
plt.show()

# Conclusions: Three species of penguins live on three islands. The most numerous species, Adelie, is also the most mobile and inhabits all three islands. The other two species each reside on their own island. The second most populous and largest species, Gentoo, exhibits a very strong correlation between flipper length and body mass, while the other species do not show this relationship.