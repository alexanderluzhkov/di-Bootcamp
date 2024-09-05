import pandas as pd
import hashlib
import random

# Load the RFM Analysis Results
df = pd.read_csv(r'C:\temp_files\RFM_Analysis_Results.csv', index_col=0)

# Function to hash Customer ID
def hash_customer_id(customer_id):
    return hashlib.sha256(str(customer_id).encode()).hexdigest()[:16]

# Function to anonymize country
def anonymize_country(country):
    return f"Country_{hash(country) % 1000:03d}"

# Identify columns containing personal information
personal_info_columns = ['Customer ID', 'Country']

# Check if 'Country' column exists in the dataframe
if 'Country' not in df.columns:
    print("Note: 'Country' column not found in the dataset. Proceeding with Customer ID anonymization only.")
    personal_info_columns.remove('Country')

# Anonymize data
if 'Customer ID' in personal_info_columns:
    df['Anonymized_Customer_ID'] = df.index.map(hash_customer_id)
    df = df.reset_index(drop=True)

if 'Country' in personal_info_columns:
    df['Anonymized_Country'] = df['Country'].map(anonymize_country)

# Remove original personal information columns
for col in personal_info_columns:
    if col in df.columns:
        df = df.drop(col, axis=1)

# Rename anonymized columns
if 'Anonymized_Customer_ID' in df.columns:
    df = df.rename(columns={'Anonymized_Customer_ID': 'Customer ID'})
if 'Anonymized_Country' in df.columns:
    df = df.rename(columns={'Anonymized_Country': 'Country'})

# Save the anonymized dataset
anonymized_file_path = r'C:\temp_files\Anonymized_RFM_Analysis_Results.csv'
df.to_csv(anonymized_file_path, index=False)

print(f"Anonymized data has been saved to: {anonymized_file_path}")
print("\nFirst few rows of the anonymized dataset:")
print(df.head())

print("\nColumns in the anonymized dataset:")
print(df.columns.tolist())