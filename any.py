import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-2.html"

header = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=header)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    all_book = []

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        all_book.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

    df = pd.DataFrame(all_book)

    print(df)

    df.to_csv("books.csv", index=False)

else:
    print("Page not found")