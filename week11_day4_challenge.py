# -*- coding: utf-8 -*-
"""Week11/day4/challenge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13WlSusVNWAHUWxGgODTtYM8hGKpxAZkE
"""

import zipfile
import os

def unzip_file(zip_path, extract_path):
    # Check if the zip file exists
    if not os.path.exists(zip_path):
        print(f"Error: The file {zip_path} does not exist.")
        return

    # Create the extraction directory if it doesn't exist
    if not os.path.exists(extract_path):
        os.makedirs(extract_path)

    # Open the zip file
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all contents to the specified directory
        zip_ref.extractall(extract_path)

    print(f"Successfully extracted contents to {extract_path}")

# Run
zip_file_path = "/content/global_power_plant_database_v_1_3.zip"
extraction_path = "/content/power_plant_database"

unzip_file(zip_file_path, extraction_path)

!pip install pandas numpy scipy

import pandas as pd
import numpy as np
from scipy import stats

def process_power_plant_data(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Basic information and summaries (as before)
    print("Dataset Information:")
    print(df.info())

    print("\nFirst few rows of the dataset:")
    print(df.head())

    print("\nBasic statistics of numerical columns:")
    print(df.describe())

    print("\nCount of power plants by primary fuel type:")
    print(df['primary_fuel'].value_counts())

    # Statistical analysis of power output by fuel type
    print("\nStatistical analysis of power output (capacity_mw) by fuel type:")
    fuel_types = df['primary_fuel'].unique()

    for fuel in fuel_types:
        fuel_data = df[df['primary_fuel'] == fuel]['capacity_mw']
        print(f"\n{fuel}:")
        print(f"  Count: {len(fuel_data)}")
        print(f"  Mean: {np.mean(fuel_data):.2f} MW")
        print(f"  Median: {np.median(fuel_data):.2f} MW")
        print(f"  Std Dev: {np.std(fuel_data):.2f} MW")
        print(f"  Min: {np.min(fuel_data):.2f} MW")
        print(f"  Max: {np.max(fuel_data):.2f} MW")


# Run
file_path = "/content/power_plant_database/global_power_plant_database.csv"
process_power_plant_data(file_path)

def process_power_plant_data(file_path):
    df = pd.read_csv(file_path)


    # Hypothesis testing
    print("\nHypothesis testing - comparing mean power output between fuel types:")
    print("Using 30% difference as the threshold for practical significance")

    fuel_types = df['primary_fuel'].unique()
    fuel_means = {fuel: df[df['primary_fuel'] == fuel]['capacity_mw'].mean() for fuel in fuel_types}

    for fuel1 in fuel_types:
        for fuel2 in fuel_types:
            if fuel1 < fuel2:  # This ensures we don't repeat comparisons
                mean1 = fuel_means[fuel1]
                mean2 = fuel_means[fuel2]

                # Calculate percent difference
                percent_diff = abs(mean1 - mean2) / ((mean1 + mean2) / 2) * 100

                # Perform t-test
                data1 = df[df['primary_fuel'] == fuel1]['capacity_mw']
                data2 = df[df['primary_fuel'] == fuel2]['capacity_mw']
                t_stat, p_value = stats.ttest_ind(data1, data2, equal_var=False)

                print(f"\nComparing {fuel1} vs {fuel2}:")
                print(f"  Mean {fuel1}: {mean1:.2f} MW")
                print(f"  Mean {fuel2}: {mean2:.2f} MW")
                print(f"  Percent difference: {percent_diff:.2f}%")
                print(f"  t-statistic: {t_stat:.4f}")
                print(f"  p-value: {p_value:.4f}")

                if p_value < 0.05 and percent_diff >= 30:
                    print("  The difference is both statistically and practically significant.")
                elif p_value < 0.05:
                    print("  The difference is statistically significant but not practically significant.")
                elif percent_diff >= 30:
                    print("  The difference is practically significant but not statistically significant.")
                else:
                    print("  The difference is neither statistically nor practically significant.")

# Run
file_path = "/content/power_plant_database/global_power_plant_database.csv"
process_power_plant_data(file_path)

import pandas as pd

def list_fuel_types(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path, low_memory=False)

    # Get unique fuel types
    fuel_types = df['primary_fuel'].unique()

    # Sort the fuel types alphabetically
    fuel_types.sort()

    print("List of fuel types in the dataset:")
    for fuel in fuel_types:
        print(f"- {fuel}")

    print(f"\nTotal number of unique fuel types: {len(fuel_types)}")

# Run
file_path = "/content/power_plant_database/global_power_plant_database.csv"
list_fuel_types(file_path)

import pandas as pd
import numpy as np
import re

def clean_and_process_data(input_file, output_file):

    df = pd.read_csv(input_file, low_memory=False)

    def extract_year(value):
        if pd.isna(value):
            return np.nan

        value_str = str(value)

        # Try to extract a 4-digit year between 1900 and 2029
        match = re.search(r'\b(19\d{2}|20[0-2]\d)\b', value_str)
        if match:
            return int(match.group(1))

        # If no 4-digit year, try to extract the integer part
        try:
            year = int(float(value_str))
            if 1900 <= year <= 2023:
                return year
        except ValueError:
            pass

        return np.nan

    # Clean commissioning_year
    df['commissioning_year'] = df['commissioning_year'].apply(extract_year)

    # Delete rows with no data in commissioning_year
    df = df.dropna(subset=['commissioning_year'])

    # Create last_working_year column
    generation_columns = ['generation_gwh_2019', 'generation_gwh_2018', 'generation_gwh_2017',
                          'generation_gwh_2016', 'generation_gwh_2015', 'generation_gwh_2014',
                          'generation_gwh_2013']

    def get_last_working_year(row):
        for year, col in zip(range(2019, 2012, -1), generation_columns):
            if pd.notna(row[col]):
                return year
        return row['year_of_capacity_data'] if pd.notna(row['year_of_capacity_data']) else np.nan

    df['last_working_year'] = df.apply(get_last_working_year, axis=1)

    # Delete rows with no data in last_working_year
    df = df.dropna(subset=['last_working_year'])

    # Save the result
    df.to_csv(output_file, index=False)

    print(f"Data processing complete. Results saved to {output_file}")
    print(f"Original row count: {len(pd.read_csv(input_file))}")
    print(f"Processed row count: {len(df)}")

# Run
input_file = "/content/power_plant_database/global_power_plant_database.csv"
output_file = "/content/power_plant_database/cleaned_power_plant_database.csv"
clean_and_process_data(input_file, output_file)

import pandas as pd
import matplotlib.pyplot as plt

def analyze_fuel_mix_evolution(input_file):

    df = pd.read_csv(input_file)

    # Define fuel types of interest
    fuel_types = ['Coal', 'Gas', 'Geothermal', 'Hydro', 'Nuclear', 'Oil', 'Solar', 'Wind', 'Other']

    # Group other fuel types
    df['fuel_type'] = df['primary_fuel'].apply(lambda x: x if x in fuel_types[:-1] else 'Other')

    # Create a year range
    year_range = range(int(df['commissioning_year'].min()), int(df['last_working_year'].max()) + 1)

    # Initialize a dictionary to store capacity data
    capacity_data = {fuel: [0] * len(year_range) for fuel in fuel_types}

    # Calculate capacity for each fuel type for each year
    for _, row in df.iterrows():
        start_year = int(row['commissioning_year'])
        end_year = int(row['last_working_year'])
        capacity = row['capacity_mw']
        fuel = row['fuel_type']

        for year in range(start_year, end_year + 1):
            if year in year_range:
                index = year - year_range[0]
                capacity_data[fuel][index] += capacity

    # Convert to DataFrame
    capacity_df = pd.DataFrame(capacity_data, index=year_range)

    # Calculate percentage
    percentage_df = capacity_df.div(capacity_df.sum(axis=1), axis=0) * 100

    # Plot the evolution
    plt.figure(figsize=(15, 8))
    percentage_df.plot(kind='area', stacked=True)
    plt.title('Evolution of Fuel Type Mix in Power Generation')
    plt.xlabel('Year')
    plt.ylabel('Percentage of Total Capacity')
    plt.legend(title='Fuel Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('fuel_mix_evolution.png')
    plt.close()

    print("Fuel mix evolution plot has been saved as 'fuel_mix_evolution.png'")

    # Print summary for specific years
    summary_years = [1950, 1970, 1990, 2010, 2020]
    for year in summary_years:
        if year in percentage_df.index:
            print(f"\nFuel mix in {year}:")
            for fuel in fuel_types:
                percentage = percentage_df.loc[year, fuel]
                if percentage > 1:  # Only print if more than 1%
                    print(f"  {fuel}: {percentage:.2f}%")

# Run
input_file = "/content/power_plant_database/cleaned_power_plant_database.csv"
analyze_fuel_mix_evolution(input_file)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_power_plant_relationships(input_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Define fuel types of interest
    fuel_types = ['Coal', 'Gas', 'Geothermal', 'Hydro', 'Nuclear', 'Oil', 'Solar', 'Wind', 'Other']

    # Group other fuel types
    df['fuel_type'] = df['primary_fuel'].apply(lambda x: x if x in fuel_types[:-1] else 'Other')

    # Select top 10 countries by total capacity
    top_countries = df.groupby('country')['capacity_mw'].sum().nlargest(10).index

    # Filter data for top countries and select relevant columns
    data = df[df['country'].isin(top_countries)][['country', 'fuel_type', 'capacity_mw']]

    # Create a pivot table: countries vs fuel types, values are total capacity
    pivot = pd.pivot_table(data, values='capacity_mw', index='country', columns='fuel_type', aggfunc='sum', fill_value=0)

    # Convert to numpy array for matrix operations
    capacity_matrix = pivot.values

    # 1. Matrix multiplication: Fuel type correlation matrix
    fuel_correlation = np.corrcoef(capacity_matrix.T)

    # Plot fuel type correlation heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(fuel_correlation, annot=True, cmap='coolwarm', xticklabels=fuel_types, yticklabels=fuel_types)
    plt.title('Fuel Type Correlation Matrix')
    plt.tight_layout()
    plt.savefig('fuel_correlation_matrix.png')
    plt.close()

    print("Fuel type correlation matrix has been saved as 'fuel_correlation_matrix.png'")

    # 2. Matrix normalization: Percentage of each fuel type per country
    row_sums = capacity_matrix.sum(axis=1, keepdims=True)
    percentage_matrix = capacity_matrix / row_sums * 100

    # Plot percentage stacked bar chart
    plt.figure(figsize=(15, 8))
    bottom = np.zeros(len(top_countries))

    for i, fuel_type in enumerate(fuel_types):
        plt.bar(top_countries, percentage_matrix[:, i], bottom=bottom, label=fuel_type)
        bottom += percentage_matrix[:, i]

    plt.title('Fuel Type Distribution in Top 10 Countries')
    plt.xlabel('Country')
    plt.ylabel('Percentage of Total Capacity')
    plt.legend(title='Fuel Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('fuel_distribution_top_countries.png')
    plt.close()

    print("Fuel type distribution chart has been saved as 'fuel_distribution_top_countries.png'")

    # 3. Matrix operations: Calculating total and average capacity per fuel type
    total_capacity = capacity_matrix.sum(axis=0)
    avg_capacity = capacity_matrix.mean(axis=0)

    # Print summary statistics
    print("\nSummary Statistics for Top 10 Countries:")
    for i, fuel in enumerate(fuel_types):
        print(f"{fuel}:")
        print(f"  Total Capacity: {total_capacity[i]:.2f} MW")
        print(f"  Average Capacity: {avg_capacity[i]:.2f} MW")

    # 4. Additional insights: Dominant fuel type per country
    dominant_fuel = pivot.idxmax(axis=1)
    print("\nDominant Fuel Type per Country:")
    for country, fuel in dominant_fuel.items():
        percentage = pivot.loc[country, fuel] / pivot.loc[country].sum() * 100
        print(f"{country}: {fuel} ({percentage:.2f}%)")

    # 5. Fuel diversity index (using Shannon entropy)
    def shannon_diversity(row):
        p = row / row.sum()
        return -np.sum(p * np.log(p) * (p > 0))

    diversity_index = pivot.apply(shannon_diversity, axis=1)
    print("\nFuel Diversity Index (Shannon Entropy):")
    for country, index in diversity_index.sort_values(ascending=False).items():
        print(f"{country}: {index:.2f}")

# Run
input_file = "/content/power_plant_database/cleaned_power_plant_database.csv"
analyze_power_plant_relationships(input_file)