
import requests
from bs4 import BeautifulSoup
import pandas as pd

all_book = []

for i in range(1, 8):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"

    header = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=header)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_="price_color").text
            rating = book.p["class"][1]
            link = "https://books.toscrape.com/catalogue/" + book.h3.a["href"]

            all_book.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Category": "Books",
                "Link": link
            })

    else:
        print("Page not found")

df = pd.DataFrame(all_book)

print(df)

df.to_csv("qoutes.csv", index=False)