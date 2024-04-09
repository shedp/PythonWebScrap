from bs4 import BeautifulSoup
import requests

# request library
html_text = requests.get('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html').text

soup = BeautifulSoup(html_text,'lxml')

book_listings = soup.find_all("article", class_="product_pod")


for book in book_listings:
    book_titles = (book.h3).a.text
    book_prices = book.find("p",class_="price_color").text[1:]

# print books under £20
    if float(book_prices[1:]) < 20:
        print(f'''
        Book title: {book_titles}.
        Book price: {book_prices}
    ''')
