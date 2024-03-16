# Web Scraping Tool

This Python script is a basic web scraping tool designed to extract data from web pages using BeautifulSoup and requests libraries. It allows you to specify a URL and a CSS selector to scrape specific data elements from multiple pages. The scraped data is then saved to a CSV file for further analysis or processing.

## Features

- **Fetching HTML content**: Sends HTTP requests to retrieve HTML content from web pages.
- **Parsing HTML**: Parses the HTML content using BeautifulSoup library to extract desired data elements.
- **Customizable data extraction**: Allows users to specify a CSS selector to target specific elements for extraction.
- **Error handling and retries**: Implements retries to handle transient network errors when fetching HTML content.
- **Randomized delays**: Adds randomized delays between requests to simulate human-like behavior and reduce the likelihood of being detected as a bot.
- **Data export**: Saves the extracted data to a CSV file for easy storage and analysis.

## Usage

1. Clone this repository or download the `web_scraping_tool.py` file.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Open the `web_scraping_tool.py` file and modify the `url`, `selector`, and `num_pages` variables according to your requirements.
4. Run the script using `python web_scraping_tool.py`.
5. Once the scraping process is complete, the extracted data will be saved to a CSV file named `scraped_data.csv`.

## Requirements

- Python 3.x
- BeautifulSoup4 library
- Requests library

## Example

```python
# Example usage
url = 'https://example.com'
selector = 'h2.title'  # Example CSS selector
num_pages = 5

scraped_data = scrape(url, selector, num_pages)
save_to_csv(scraped_data, 'scraped_data.csv')
print("Scraping complete!")
```

## License 
This project is licensed under the MIT License - see the LICENSE file for details.
