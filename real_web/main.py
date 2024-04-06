from bs4 import BeautifulSoup
import requests

# request library
html_text = requests.get('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html').text

soup = BeautifulSoup(html_text,'lxml')

book_listings = soup.find_all("article", class_="product_pod")

for book in book_listings:
    book_title = (book.h3).a.text
    print(book_title)