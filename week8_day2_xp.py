# -*- coding: utf-8 -*-
"""Week8/day2/xp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10GJScALpd4SmOqkaLrngqelFKa7n_RW-
"""

# Exercise 1

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Read the CSV file into a DataFrame
df = pd.read_csv('train.csv')

# Check for duplicate rows across all columns
duplicate_rows = df.duplicated()

# If duplicates exist, remove them and store the result in a new DataFrame
if duplicate_rows.any():
    df_deduplicated = df.drop_duplicates()

    # Get the number of rows before and after removing duplicates
    num_rows_before = df.shape[0]
    num_rows_after = df_deduplicated.shape[0]

    # Print the number of duplicates dropped and the shape of the new DataFrame
    print(f"Number of duplicates dropped: {num_rows_before - num_rows_after}")
    print(f"Shape of the new DataFrame after removing duplicates: {df_deduplicated.shape}")
else:
    print("No duplicate rows found in the dataset.")

# Exercise 2

import pandas as pd
from sklearn.impute import SimpleImputer

# Calculate and print the percentage of missing values in each column
missing_percentage = (df.isnull().sum() / len(df)) * 100
print("Percentage of missing values in each column:")
print(missing_percentage.round(4).to_markdown(numalign="left", stralign="left"))

# Create a copy of the DataFrame
df_copy = df.copy()

# Age: Impute missing values with the mean
imputer = SimpleImputer(strategy='mean')
df_copy['Age'] = imputer.fit_transform(df_copy[['Age']])
df_age_imputed = df_copy.copy()

# Cabin: Fill missing values with 'Unknown'
df_cabin_filled = df.copy()
df_cabin_filled['Cabin'] = df_cabin_filled['Cabin'].fillna('Unknown')

# Embarked: Fill missing values with the most frequent category
most_frequent_embarked = df['Embarked'].mode()[0]
df_embarked_filled = df.copy()
df_embarked_filled['Embarked'] = df_embarked_filled['Embarked'].fillna(most_frequent_embarked)

# Dropping Rows: Drop rows with any missing values
df_dropped = df.copy()
df_dropped.dropna(inplace=True)

# Display the first 5 rows of each modified DataFrame
print("\nDataFrame with age imputed:")
print(df_age_imputed.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nDataFrame with cabin filled:")
print(df_cabin_filled.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nDataFrame with embarked filled:")
print(df_embarked_filled.head().to_markdown(index=False, numalign="left", stralign="left"))

print("\nDataFrame with rows dropped:")
print(df_dropped.head().to_markdown(index=False, numalign="left", stralign="left"))

# Exercise 3, 6

import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import re


# Create a new feature 'Family_Size'
df['Family_Size'] = df['SibSp'] + df['Parch'] + 1

# Extract titles from the 'Name' column
df['Title'] = df['Name'].apply(lambda x: re.search(' ([A-Za-z]+)\.', x).group(1))

# Map common titles to simplified versions and others to 'Other'
title_mapping = {'Mr': 'Mr', 'Miss': 'Miss', 'Mrs': 'Mrs', 'Master': 'Master', 'Dr': 'Other', 'Rev': 'Other', 'Col': 'Other', 'Major': 'Other', 'Mlle': 'Miss', 'Mme': 'Mrs', 'Ms': 'Miss', 'Capt': 'Other', 'Lady': 'Other', 'Sir': 'Other', 'Don': 'Other', 'Jonkheer': 'Other', 'Countess': 'Other'}
df['Title'] = df['Title'].map(title_mapping)

# Fill missing values in 'Embarked' with the most frequent category
most_frequent_embarked = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(most_frequent_embarked)

# One-hot encode 'Sex', 'Embarked', and 'Title'
encoder = OneHotEncoder(drop='first', sparse=False)
encoded_data = encoder.fit_transform(df[['Sex', 'Embarked', 'Title']])

# Get feature names, excluding dropped categories
feature_names = []
for i, categories in enumerate(encoder.categories_):
    feature_names.extend([f"{df[['Sex', 'Embarked', 'Title']].columns[i]}_{category}" for category in categories[1:]])

# Create DataFrame with correct feature names
encoded_df = pd.DataFrame(encoded_data, columns=feature_names)

# Standardize 'Age' and 'Fare'
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Concatenate the encoded and standardized features with the original dataframe
df_final = pd.concat([df, encoded_df], axis=1)
df_final.drop(['Sex', 'Embarked', 'Name', 'Title'], axis=1, inplace=True)

print(df_final.head().to_markdown(index=False, numalign="left", stralign="left"))

# Exercise 4

import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame
df = pd.read_csv('train.csv')

# Calculate Q1, Q3, and IQR for 'Age' and 'Fare'
Q1 = df[['Age', 'Fare']].quantile(0.25)
Q3 = df[['Age', 'Fare']].quantile(0.75)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Identify outliers in 'Age' and 'Fare'
outliers_age = (df['Age'] < lower_bound['Age']) | (df['Age'] > upper_bound['Age'])
outliers_fare = (df['Fare'] < lower_bound['Fare']) | (df['Fare'] > upper_bound['Fare'])

# Cap outliers to their respective bounds
df['Age_capped'] = np.where(
    outliers_age,
    np.where(df['Age'] < lower_bound['Age'], lower_bound['Age'], upper_bound['Age']),
    df['Age']
)

df['Fare_capped'] = np.where(
    outliers_fare,
    np.where(df['Fare'] < lower_bound['Fare'], lower_bound['Fare'], upper_bound['Fare']),
    df['Fare']
)

# Print descriptive statistics before and after capping
print("\nDescriptive statistics for 'Age' before capping:")
print(df['Age'].describe().round(4).to_markdown(numalign="left", stralign="left"))

print("\nDescriptive statistics for 'Age' after capping:")
print(df['Age_capped'].describe().round(4).to_markdown(numalign="left", stralign="left"))

print("\nDescriptive statistics for 'Fare' before capping:")
print(df['Fare'].describe().round(4).to_markdown(numalign="left", stralign="left"))

print("\nDescriptive statistics for 'Fare' after capping:")
print(df['Fare_capped'].describe().round(4).to_markdown(numalign="left", stralign="left"))

print("\nFirst 5 rows of the dataframe:")
print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

# Exercise 5

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv('train.csv')

# Standardize 'Age'
scaler = StandardScaler()
df['Age_std'] = scaler.fit_transform(df[['Age']].fillna(df['Age'].mean()))  # Impute missing 'Age' with mean before scaling

# Normalize 'Fare'
normalizer = MinMaxScaler()
df['Fare_norm'] = normalizer.fit_transform(df[['Fare']])

# Show the transformed data (first 5 rows)
print(df[['Age', 'Age_std', 'Fare', 'Fare_norm']].head().round(4).to_markdown(index=False,numalign="left", stralign="left"))

# Exercise 7

import pandas as pd

df = pd.read_csv('train.csv')

# Define age bins and labels
bins = [0, 18, 30, 50, 80]
labels = ['Child', 'Young Adult', 'Adult', 'Senior']

# Create a new column 'Age_Group' by applying pd.cut() to the 'Age' column
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)

# Apply one-hot encoding to the 'Age_Group' column
age_group_dummies = pd.get_dummies(df['Age_Group'], prefix='Age_Group')

# Concatenate the one-hot encoded age groups with the original DataFrame
df = pd.concat([df, age_group_dummies], axis=1)

# Drop the original 'Age' and 'Age_Group' columns
df.drop(['Age', 'Age_Group'], axis=1, inplace=True)

# Convert the one-hot encoded columns to integers
for col in ['Age_Group_Child', 'Age_Group_Young Adult', 'Age_Group_Adult', 'Age_Group_Senior']:
    df[col] = df[col].astype(int)

# Save the dataframe to a new csv file "train_age_one_hot_encoded_int.csv"
df.to_csv('train_age_one_hot_encoded_int.csv', index=False)


print(df.head().to_markdown(index=False, numalign="left", stralign="left"))