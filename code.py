import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
import json

# Initialize a web driver 
driver = webdriver.Chrome()


scraped_data = []

# Load the CSV file
csv_file_path = '/content/Amazon Scraping - Sheet1.csv' # Update with your CSV file path
with open(csv_file_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        country_code = row.get('Country Code', '') # Handle missing values gracefully
        asin = row.get('ASIN', '')
        url = f"https://www.amazon.{country_code}/dp/{asin}"

        try:
            
            driver.get(url)

            # Check for Error 404
            if "404 - Not Found" in driver.title:
                print(f"{url} not available")
                continue

            
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            
            product_title = soup.find('span', {'id': 'productTitle'})
            product_image = soup.find('img', {'id': 'landingImage'})
            product_price = soup.find('span', {'id': 'priceblock_ourprice'})
            product_details = soup.find('div', {'id': 'productDescription'})

            
            if not (product_title and product_image and product_price and product_details):
                print(f"Data missing for {url}. Skipping.")
                continue

            
            product_title = product_title.text.strip()
            product_image_url = product_image.get('src', '')
            product_price = product_price.text.strip()
            product_details = product_details.text.strip()

            
            product_data = {
                "Product Title": product_title,
                "Product Image URL": product_image_url,
                "Price of the Product": product_price,
                "Product Details": product_details
            }
            scraped_data.append(product_data)

            
            print(f"Product Title: {product_title}")
            print(f"Product Image URL: {product_image_url}")
            print(f"Price of the Product: {product_price}")
            print(f"Product Details: {product_details}")

        except NoSuchElementException:
            print(f"{url} not available")

# Save the scraped data as a JSON file
json_file_path = 'scraped_data.json' # Update with your desired JSON file path
with open(json_file_path, 'w') as json_file:
    json.dump(scraped_data, json_file, indent=4)


driver.quit()
