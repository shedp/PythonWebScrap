from bs4 import BeautifulSoup
import requests
import time

print('What is you maximum price?')
max_price = input('£')
print(f'Filtering for books under £{max_price}')

# request library
def find_books():
    html_text = requests.get('https://books.toscrape.com/catalogue/category/books/mystery_3/index.html').text
    soup = BeautifulSoup(html_text,'lxml')
    book_listings = soup.find_all("article", class_="product_pod")

    for book in book_listings:
        book_titles = (book.h3).a.text
        book_prices = book.find("p",class_="price_color").text[1:]

    # print books under £20
        if float(book_prices[1:]) < float(max_price):
            print(f'''
            Book title: {book_titles}.
            Book price: {book_prices}
        ''')    

if __name__ == '__main__':
    while True:
        find_books()
        time_wait = 10
        time.sleep(6*time_wait)
        # run every 10 mins