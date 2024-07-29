# -*- coding: utf-8 -*-
"""Week12/day6/xp.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IhDA8hkggYs7IS_jn3OJyUE9Rc-axeAV

Exercise 1
"""

!pip install beautifulsoup4

from bs4 import BeautifulSoup

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sports World</title>
    <style>
        body { font-family: Arial, sans-serif; }
        header, nav, section, article, footer { margin: 20px; padding: 15px; }
        nav { background-color: #333; }
        nav a { color: white; padding: 14px 20px; text-decoration: none; display: inline-block; }
        nav a:hover { background-color: #ddd; color: black; }
        .video { text-align: center; margin: 20px 0; }
    </style>
</head>
<body>

    <header>
        <h1>Welcome to Sports World</h1>
        <p>Your one-stop destination for the latest sports news and videos.</p>
    </header>

    <nav>
        <a href="#football">Football</a>
        <a href="#basketball">Basketball</a>
        <a href="#tennis">Tennis</a>
    </nav>

    <section id="football">
        <h2>Football</h2>
        <article>
            <h3>Latest Football News</h3>
            <p>Read about the latest football matches and player news.</p>
            <div class="video">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/football-video-id" frameborder="0" allowfullscreen>
                </iframe>
            </div>
        </article>
    </section>

    <section id="basketball">
        <h2>Basketball</h2>
        <article>
            <h3>NBA Highlights</h3>
            <p>Watch highlights from the latest NBA games.</p>
            <div class="video">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/basketball-video-id" frameborder="0" allowfullscreen>
                </iframe>
            </div>
        </article>
    </section>

    <section id="tennis">
        <h2>Tennis</h2>
        <article>
            <h3>Grand Slam Updates</h3>
            <p>Get the latest updates from the world of Grand Slam tennis.</p>
            <div class="video">
                <iframe width="560" height="315" src="https://www.youtube.com/embed/tennis-video-id" frameborder="0" allowfullscreen></iframe>
            </div>
        </article>
    </section>

    <footer>
        <form action="mailto:contact@sportsworld.com" method="post" enctype="text/plain">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="email">Email:</label><br>
            <input type="email" id="email" name="email"><br>
            <label for="message">Message:</label><br>
            <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
            <input type="submit" value="Send">
        </form>
    </footer>

</body>
</html>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Extract the Title
print(soup.title.string)

# Extract all paragraphs
paragraphs = soup.find_all('p')
print("Paragraphs:")
for p in paragraphs:
    print(p.text)

print("\n")

# Retrieve all links
links = soup.find_all('a')
print("Links:")
for link in links:
    print(link.get('href'))

"""Exercise 2"""

from urllib.request import urlopen

def get_robots_txt(url):
    """
    Fetch and return the content of robots.txt for the given URL.
    """
    robots_url = f"{url}/robots.txt"
    try:
        with urlopen(robots_url) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        return f"An error occurred: {e}"

# URL for English Wikipedia
wikipedia_url = "https://en.wikipedia.org"

# Fetch and display the robots.txt content
robots_content = get_robots_txt(wikipedia_url)
print(f"robots.txt content for {wikipedia_url}:\n")
print(robots_content)

"""Exercise 3"""

import requests
from bs4 import BeautifulSoup

def extract_headers(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all header tags
        headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

        # Display the headers
        for header in headers:
            print(f"{header.name}: {header.text.strip()}")

    except requests.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# URL for Wikipedia's main page
url = "https://en.wikipedia.org/wiki/Main_Page"

# Extract and display headers
print(f"Headers from {url}:\n")
extract_headers(url)

"""Exercise 4"""

import requests
from bs4 import BeautifulSoup

def check_title(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the title tag
        title_tag = soup.find('title')

        if title_tag:
            print(f"The page contains a title: {title_tag.string.strip()}")
        else:
            print("The page does not contain a title.")

    except requests.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# URL
url = "https://www.linkedin.com/"

# Check for title
check_title(url)

"""Exercise 5"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_cisa_alerts_count():
    url = "https://www.cisa.gov/news-events/cybersecurity-advisories"
    current_year = datetime.now().year

    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all teaser rows
        teaser_rows = soup.find_all("div", class_="c-teaser__row")

        count = 0
        for row in teaser_rows:
            date_elem = row.find("div", class_="c-teaser__date")
            meta_elem = row.find("div", class_="c-teaser__meta")

            if date_elem and meta_elem:
                date = date_elem.text.strip()
                meta = meta_elem.text.strip()

                if "ALERT" in meta.upper() and str(current_year) in date:
                    count += 1

        print(f"Number of ALERT items issued by CISA in {current_year}: {count}")

    except requests.RequestException as e:
        print(f"An error occurred while fetching the webpage: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
get_cisa_alerts_count()