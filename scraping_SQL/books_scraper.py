import sqlite3
import requests
from bs4 import BeautifulSoup


#Request URL

def save_books(all_books):
    connection = sqlite3.connect("books.db")
    c = connection.cursor()
    c.execute('''CREATE TABLE books 
              (title TEXT,price REAL,rating INTEGER);''')
    c.executemany("INSERT INTO books VALUES (?,?,?)",all_books)
    connection.commit()
    connection.close()


def scrape_book(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article")
    all_books = []
    for book in books:
       book_data = (get_title(book),get_price(book),get_rating(book))
       all_books.append(book_data)
    save_books(all_books)

def get_title(book):
    return book.find("h3").find("a")["title"]

def get_price(book):
     price = book.select(".price_color")[0].get_text()
     return float(price.replace("Â","").replace("£",""))

def get_rating(book):
    ratings = {"Zero":0, "One":1,"Two":2,"Three":3,"Four":4,"Five":5}
    paragraph = book.select(".star-rating")[0]
    word = paragraph.get_attribute_list("class")[-1]
    return ratings[word]


scrape_book("https://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html")
#Initialize BS
#Extract Data we want
#Save Data to database