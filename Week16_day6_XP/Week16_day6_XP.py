import pandas as pd
import numpy as np
from datetime import datetime

# Load the dataset with the correct encoding
df = pd.read_csv(r'C:\temp_files\Year 2009-2010.csv', encoding='ISO-8859-1')

# Convert 'InvoiceDate' to datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Calculate total price for each transaction
df['TotalPrice'] = df['Quantity'] * df['Price']

# Remove cancelled orders (those with 'C' in the invoice number)
df = df[~df['Invoice'].str.contains('C', na=False)]

# Calculate RFM scores
current_date = df['InvoiceDate'].max() + pd.Timedelta(days=1)

rfm = df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (current_date - x.max()).days,
    'Invoice': 'count',
    'TotalPrice': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Calculate quartiles for RFM scores
r_labels = range(4, 0, -1)
f_labels = range(1, 5)
m_labels = range(1, 5)

r_quartiles = pd.qcut(rfm['Recency'], q=4, labels=r_labels)
f_quartiles = pd.qcut(rfm['Frequency'], q=4, labels=f_labels)
m_quartiles = pd.qcut(rfm['Monetary'], q=4, labels=m_labels)

rfm['R'] = r_quartiles
rfm['F'] = f_quartiles
rfm['M'] = m_quartiles

# Calculate RFM Score
rfm['RFM_Score'] = rfm['R'].astype(str) + rfm['F'].astype(str) + rfm['M'].astype(str)

# Define customer segments
def segment_customers(row):
    if row['RFM_Score'] in ['444', '434', '443', '433']:
        return 'High-Value'
    elif row['RFM_Score'] in ['441', '442', '432', '423', '424']:
        return 'Loyal'
    elif row['RFM_Score'] in ['411', '412', '421']:
        return 'New'
    elif row['RFM_Score'] in ['311', '422', '423', '332']:
        return 'Potential Churners'
    else:
        return 'Lost'

rfm['Customer_Segment'] = rfm.apply(segment_customers, axis=1)

# Display results
print(rfm.head())
print("\nCustomer Segment Distribution:")
print(rfm['Customer_Segment'].value_counts(normalize=True))

# Save results to CSV
rfm.to_csv(r'C:\temp_files\RFM_Analysis_Results.csv', encoding='utf-8')
print("\nResults saved to 'RFM_Analysis_Results.csv' in the same directory.")