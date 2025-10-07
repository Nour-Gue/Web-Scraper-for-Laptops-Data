import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

all_data = []

for page in range(1, 21):
    url = f"https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops?page={page}"
    response = requests.get(url)
    if response.status_code != 200:
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.find_all("div", class_="thumbnail")

    for p in products:
        name_element = p.find("a", class_="title")
        name = name_element.text.strip() if name_element else "N/A"

        price_element = p.find("h4", class_="price")
        price = price_element.text.strip() if price_element else "N/A"

        description_element = p.find("p", class_="description")
        description = description_element.text.strip() if description_element else "N/A"

        reviews_element = p.find("p", class_="pull-right")
        reviews = reviews_element.text.strip() if reviews_element else "N/A"

        rating_elements = p.find_all("span", class_="glyphicon-star")
        rating = len(rating_elements) if rating_elements else 0

        all_data.append({
            "Name": name,
            "Price": price,
            "Rating": rating,
            "Reviews": reviews,
            "Description": description
        })

    time.sleep(0.5)

df = pd.DataFrame(all_data)
df.to_csv("laptops_data.csv", index=False, encoding="utf-8-sig")
print(f"Extracted {len(df)} rows and saved to laptops_data.csv successfully!")
