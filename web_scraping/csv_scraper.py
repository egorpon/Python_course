from bs4 import BeautifulSoup
import requests
from time import sleep
from csv import DictWriter

BASE_URL = "https://quotes.toscrape.com/"

def scrape_quotes():
    all_quotes = []
    url = "/page/1"
    while url:
        response = requests.get(f"{BASE_URL}{url}")
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all("div", class_="quote")
        for quote in quotes:
            q = quote.find("span",class_= "text").get_text()
            author = quote.find("small",class_="author").get_text()
            a = quote.find("a")["href"]
            all_quotes.append({
                    "text" : q,
                    "author":author,
                    "href":a})

        next_btn = soup.find(class_="next")
        url = next_btn.find("a")["href"] if next_btn else None
        sleep(1)
    return all_quotes



def write_quotes(quotes):
    with open("quotes.csv", "w", encoding="utf-8-sig",newline="") as file:
        headers = ["text","author","href"]
        csv_writer = DictWriter(file,fieldnames=headers)
        csv_writer.writeheader()
        for quote in quotes:
            csv_writer.writerow(quote)

quotes = scrape_quotes()
write_quotes(quotes)
#write quotes to CSV file