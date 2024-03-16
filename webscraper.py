import requests
from bs4 import BeautifulSoup
import time
import random
import csv

def fetch_html(url):
    headers = {'User-Agent': 'Your User-Agent String'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch HTML:", response.status_code)
        return None

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    # Your parsing logic here
    # Example:
    titles = soup.find_all('h2', class_='title')
    return [title.text.strip() for title in titles]

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        for item in data:
            writer.writerow([item])

def scrape(url, num_pages=5):
    all_titles = []
    for page in range(1, num_pages+1):
        page_url = f"{url}?page={page}"
        html = fetch_html(page_url)
        if html:
            titles = parse_html(html)
            all_titles.extend(titles)
            print(f"Scraped page {page}")
            time.sleep(random.uniform(1, 3))  # Add some delay between requests
        else:
            print(f"Failed to scrape page {page}")

    return all_titles

if __name__ == "__main__":
    url = 'https://example.com'
    scraped_data = scrape(url)
    save_to_csv(scraped_data, 'scraped_data.csv')
    print("Scraping complete!")
