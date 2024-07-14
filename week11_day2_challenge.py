# -*- coding: utf-8 -*-
"""Week11/day2/challenge.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z0KxPb4A0sVmrDsVT8ZR9il2aM5BTvxt

1. Data Preporation.
"""

import numpy as np
import pandas as pd


# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic temperature data
temperatures = np.random.uniform(low=-5, high=35, size=(10, 12))

# Round the temperatures to one decimal place
temperatures = np.round(temperatures, decimals=1)


# Create a list of city names
city_names = [f"City {i}" for i in range(1, 11)]

# Create a list of month names
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create the DataFrame
df = pd.DataFrame(data=temperatures, index=city_names, columns=month_names)

print(df)

"""2. Data Analysis"""

# Calculate annual average temperature for each city
annual_avg_temps = df.mean(axis=1)

# Add the annual average temperatures to the DataFrame
df['Annual Average'] = annual_avg_temps

# Identify the city with the highest average temperature
city_highest_temp = annual_avg_temps.idxmax()
highest_temp = annual_avg_temps.max()

# Identify the city with the lowest average temperature
city_lowest_temp = annual_avg_temps.idxmin()
lowest_temp = annual_avg_temps.min()

print("\nAnnual Average Temperatures:")
print(annual_avg_temps)
print(f"\nCity with highest average temperature: {city_highest_temp} ({highest_temp:.1f}°C)")
print(f"City with lowest average temperature: {city_lowest_temp} ({lowest_temp:.1f}°C)")

"""3. Data Visualization"""

import matplotlib.pyplot as plt
from statsmodels.nonparametric.smoothers_lowess import lowess

# Create a figure and axis for plotting
plt.figure(figsize=(12, 8))

# Plot temperature trends for each city
for city in df.index:
    # Get the temperature data for the city
    temp_data = df.loc[city]

    # Create x-axis values (0 to 11 for 12 months)
    x = np.arange(12)

    # Perform LOESS smoothing
    smoothed = lowess(temp_data, x, frac=0.6)

    # Plot the original data and the smoothed trend
    plt.scatter(x, temp_data, alpha=0.5, label=None)
    plt.plot(x, smoothed[:, 1], label=city)

# Customize the plot
plt.title('Temperature Trends for Cities (LOESS Smoothing)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(range(12), month_names)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()

"""Brief report: the part of the cities is located in the North hemisphere, the part is in the South hemisfere, the part in a very weird place."""