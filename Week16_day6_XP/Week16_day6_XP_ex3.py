import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv(r'C:\temp_files\Year 2009-2010.csv', encoding='ISO-8859-1')

# Convert 'InvoiceDate' to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Create 'TotalPrice' column
df['TotalPrice'] = df['Quantity'] * df['Price']

# Remove cancelled orders (those with 'C' in the invoice number)
df = df[~df['Invoice'].str.contains('C', na=False)]

# Aggregate sales data on a monthly basis
monthly_sales = df.groupby(df['InvoiceDate'].dt.to_period('M')).agg({
    'TotalPrice': 'sum',
    'Quantity': 'sum'
}).reset_index()

monthly_sales['InvoiceDate'] = monthly_sales['InvoiceDate'].dt.to_timestamp()

# Analyze monthly sales trends
plt.figure(figsize=(12, 6))
sns.lineplot(x='InvoiceDate', y='TotalPrice', data=monthly_sales)
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r'C:\temp_files\monthly_sales_trend.png')
plt.close()

# Simple Moving Average (SMA) for next quarter forecast
sma_period = 3  # Using last 3 months for SMA
monthly_sales['SMA'] = monthly_sales['TotalPrice'].rolling(window=sma_period).mean()

# Forecast next quarter (3 months)
last_date = monthly_sales['InvoiceDate'].max()
next_quarter = pd.date_range(start=last_date + pd.DateOffset(months=1), periods=3, freq='M')
forecast = pd.DataFrame({'InvoiceDate': next_quarter, 'Forecast': monthly_sales['SMA'].iloc[-1]})

# Plot actual sales and forecast
plt.figure(figsize=(12, 6))
sns.lineplot(x='InvoiceDate', y='TotalPrice', data=monthly_sales, label='Actual Sales')
sns.lineplot(x='InvoiceDate', y='SMA', data=monthly_sales, label='Simple Moving Average')
sns.lineplot(x='InvoiceDate', y='Forecast', data=forecast, label='Forecast')
plt.title('Monthly Sales Trend with SMA and Forecast')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\temp_files\sales_forecast.png')
plt.close()

# Print insights and forecast
print("Sales Analysis Insights:")
print(f"1. Total Revenue: ${monthly_sales['TotalPrice'].sum():,.2f}")
print(f"2. Average Monthly Revenue: ${monthly_sales['TotalPrice'].mean():,.2f}")
print(f"3. Highest Revenue Month: {monthly_sales.loc[monthly_sales['TotalPrice'].idxmax(), 'InvoiceDate'].strftime('%B %Y')}")
print(f"4. Lowest Revenue Month: {monthly_sales.loc[monthly_sales['TotalPrice'].idxmin(), 'InvoiceDate'].strftime('%B %Y')}")
print(f"5. Number of months in the dataset: {len(monthly_sales)}")

print("\nSales Forecast for Next Quarter:")
for date, forecast in zip(next_quarter, forecast['Forecast']):
    print(f"{date.strftime('%B %Y')}: ${forecast:,.2f}")

print("\nNote: This forecast is based on a Simple Moving Average of the last 3 months.")
print("Limitations of this method include:")
print("- It doesn't account for long-term trends or seasonality.")
print("- It's sensitive to recent changes and outliers.")
print("- It assumes that future sales will be similar to recent past sales.")
print("- Limited data points may affect the accuracy of the forecast.")

# Additional analysis: Top selling products
top_products = df.groupby('Description').agg({
    'Quantity': 'sum',
    'TotalPrice': 'sum'
}).sort_values('TotalPrice', ascending=False).head(10)

print("\nTop 10 Selling Products:")
print(top_products)

# Country-wise sales analysis
country_sales = df.groupby('Country').agg({
    'TotalPrice': 'sum'
}).sort_values('TotalPrice', ascending=False).head(10)

print("\nTop 10 Countries by Sales:")
print(country_sales)

# Month-over-month growth rate
monthly_sales['Growth_Rate'] = monthly_sales['TotalPrice'].pct_change() * 100

print("\nMonth-over-Month Growth Rates:")
print(monthly_sales[['InvoiceDate', 'TotalPrice', 'Growth_Rate']])