# README - Amazon Product Scraper

## Introduction
This Python script is designed to scrape product information from Amazon product pages based on ASIN (Amazon Standard Identification Number) values provided in a CSV file. It utilizes Selenium for web automation, BeautifulSoup for HTML parsing, and saves the scraped data as a JSON file.

## Prerequisites
Before running the script, ensure you have the following installed:

1. [Python](https://www.python.org/downloads/) (Python 3.x recommended)
2. [Selenium](https://selenium-python.readthedocs.io/installation.html)
3. [ChromeDriver](https://sites.google.com/chromium.org/driver/) (WebDriver for Chrome) - Ensure the driver version matches your installed Chrome browser version.
4. [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)

## Usage
1. Place the CSV file containing ASIN values in the same directory as the script.
2. Modify the `/content/Amazon Scraping - Sheet1.csv` variable in the script to specify the CSV file's name, e.g., `'your_csv_file.csv'`.
3. Ensure you've configured the `json_file_path` variable to specify the desired JSON file path where the scraped data will be saved.
4. Run the script using the Python interpreter.

## Important Notes
- This script assumes that the CSV file contains a column named 'Country Code' for generating Amazon product URLs and a column named 'ASIN' for the unique product identifier.
- It checks for 404 errors and skips unavailable products.
- The scraped data includes product title, image URL, price, and product details.
- You can customize the data extraction and output format as needed.
- Ensure that you have a stable internet connection while running the script.

## Dependencies
- Python 3.x
- Selenium
- ChromeDriver
- BeautifulSoup

## Author
Garv Popli
For any queries contact at garvpopli09@gmail.com

