# Web Scraper for Laptops Data

This Python project scrapes laptop data from a test e-commerce website using **BeautifulSoup**. The script collects the following details for each product:

- Name
- Price
- Rating
- Number of Reviews
- Description

## Features

- Scrapes multiple pages (default: 20 pages)
- Handles missing data gracefully
- Saves the scraped data into a CSV file (`laptops_data.csv`)
- Lightweight and easy to modify for other categories or websites

## Requirements

- Python 3.7+
- Libraries:
  - requests
  - beautifulsoup4
  - pandas

Install dependencies with:

```bash
pip install requests beautifulsoup4 pandas
