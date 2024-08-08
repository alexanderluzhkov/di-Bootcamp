from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import time

# Set up the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get("https://www.inmotionhosting.com/shared-hosting")

# Wait for the page to load completely
time.sleep(5)

# Extract the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

# Prepare a list to store the extracted data
hosting_plans = []

# Find the plan cards containing plan details
plan_cards = soup.select('div.imh-rostrum-card')

# Extract plan names and prices
for card in plan_cards:
    plan_name = card.select_one('h3.imh-rostrum-card-title').text.strip()
    price = card.select_one('span.rostrum-price').text.strip()
    
    hosting_plans.append({
        'Plan Name': plan_name,
        'Price': price,
        'Features': []
    })

# Find the table containing plan features
table = soup.select_one('div.imh-spec-table-container table')

# Find all rows in the table body
rows = table.select('tbody tr')

# Extract features for each plan
for row in rows:
    feature_name = row.select_one('td:first-child').text.strip()
    feature_values = row.select('td:not(:first-child)')
    
    for i, value in enumerate(feature_values):
        if i < len(hosting_plans):
            hosting_plans[i]['Features'].append(f"{feature_name}: {value.text.strip()}")

# Save the data to a CSV file
csv_filename = 'inmotionhosting_plans_complete.csv'

with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Plan Name', 'Price', 'Features']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for plan in hosting_plans:
        writer.writerow({
            'Plan Name': plan['Plan Name'],
            'Price': plan['Price'],
            'Features': ', '.join(plan['Features'])
        })

print(f"Data saved to {csv_filename}")

# Close the browser
driver.quit()
