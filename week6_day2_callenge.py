import sqlite3
import requests
import random

# Step 1: Set Up the Database
conn = sqlite3.connect('countries.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Country (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    capital TEXT,
    flag TEXT,
    subregion TEXT,
    population INTEGER
)
''')
conn.commit()

# Step 2: Fetch Data from the REST Countries API
response = requests.get('https://restcountries.com/v3.1/all')
countries = response.json()
selected_countries = random.sample(countries, 10)

# Step 3: Insert Data into the Database
for country in selected_countries:
    name = country.get('name', {}).get('common', 'N/A')
    capital = country.get('capital', ['N/A'])[0] if 'capital' in country else 'N/A'
    flag = country.get('flags', {}).get('png', 'N/A')
    subregion = country.get('subregion', 'N/A')
    population = country.get('population', 0)
    
    cursor.execute('''
    INSERT INTO Country (name, capital, flag, subregion, population)
    VALUES (?, ?, ?, ?, ?)
    ''', (name, capital, flag, subregion, population))


conn.commit()
conn.close()
