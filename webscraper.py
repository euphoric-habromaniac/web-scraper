import requests
from bs4 import BeautifulSoup
import time
import random
import csv

def fetch_html(url, retries=3):
    headers = {'User-Agent': 'Your User-Agent String'}
    for _ in range(retries):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            return response.text
        except requests.exceptions.RequestException as e:
            print("Failed to fetch HTML:", e)
            time.sleep(random.uniform(2, 5))  # Add delay before retrying
    print("Max retries exceeded. Failed to fetch HTML.")
    return None

def parse_html(html, selector):
    soup = BeautifulSoup(html, 'html.parser')
    # Your parsing logic here
    # Example:
    titles = soup.select(selector)
    return [title.text.strip() for title in titles]

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title'])
        for item in data:
            writer.writerow([item])

def scrape(url, selector, num_pages=5):
    all_titles = []
    for page in range(1, num_pages+1):
        page_url = f"{url}?page={page}"
        html = fetch_html(page_url)
        if html:
            titles = parse_html(html, selector)
            all_titles.extend(titles)
            print(f"Scraped page {page}")
            time.sleep(random.uniform(1, 3))  # Add some delay between requests
        else:
            print(f"Failed to scrape page {page}")

    return all_titles

if __name__ == "__main__":
    url = 'https://example.com'
    selector = 'h2.title'  # Example CSS selector
    scraped_data = scrape(url, selector)
    save_to_csv(scraped_data, 'scraped_data.csv')
    print("Scraping complete!")
