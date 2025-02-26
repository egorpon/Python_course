from bs4 import BeautifulSoup
import requests
from random import choice

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
        # sleep(2)
    return all_quotes


def starts_game(quotes):
    attempts = 4
    # while True:
    print("Here's a quote:")
    quote = choice(quotes)
    print(quote.get("text"))
    print(quote["author"])
    msg = ""
    while msg.lower() != quote.get("author").lower() and attempts>0:
            msg = input(f"Who said this? Guesses remaining: {attempts}. ")
            if msg.lower() == quote["author"].lower():
                print("YOU GOT IT RIGHT!")
                break
            attempts-=1
            if attempts == 3:
                res = requests.get(f"{BASE_URL}{quote["href"]}")
                soup = BeautifulSoup(res.text, "html.parser")
                born_date = soup.find("span", class_="author-born-date").get_text()
                born_location = soup.find("span", class_="author-born-location").get_text()
                print(f"Here's a hint: Author was born on {born_date} {born_location}")
            elif attempts == 2:
                print(f"Here's a hint: The author's First name starts with {quote["author"][0]}")
            elif attempts == 1:
                last_name = quote["author"].split(" ")[1][0]
                print(f"The author's Last name starts with {last_name}")     
            else:
                print(f"Sorry, you've run out of guesses. The answer was {quote["author"]}")             

    again = ""
    while again not in ("y","yes","n","no"):
        again = input("Would you like to play again (y/n)?")
    if again.lower() in ("y","yes"):
        print("OK YOU PLAY AGAIN!")
        return starts_game(quotes)
    else:
        print("OK, GOODBYE!")

quotes = scrape_quotes()
starts_game(quotes)