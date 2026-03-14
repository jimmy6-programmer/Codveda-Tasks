import requests
import csv
from bs4 import BeautifulSoup

# URL for the website we want to scrape
url = "https://quotes.toscrape.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Access granted")

        # Convert html into a searchable object
        searchable_obj = BeautifulSoup(response.text, "html.parser")

        # Find all quote blocks on the webpage
        quotes = searchable_obj.find_all("div", class_="quote")

        # Create a list to store quotes data
        data = []

        # Loop through each quote block
        for quote in quotes:
            # Extract text
            text = quote.find("span", class_="text").get_text()
            # Extract author's name
            author = quote.find("small", class_="author").get_text()

            # Append data to our list
            data.append([text, author])

        with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Text", "Author"])
            writer.writerows(data)
    else:
        print("Access denied")
        print(response.status_code)
except requests.exceptions.RequestException as e:
    print("There was an error trying to scrap the website: ")
    print(e)                    

