import requests
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

url = "https://icanhazdadjoke.com/search"

print(colored(figlet_format("Dad Joke 3000"), color="magenta"))
msg = input("Let me tell you a joke! Give me a topic: ")

res = requests.get(
    url, headers={"Accept": "application/json"}, params={"term": msg}
).json()


def rand_joke(data):
    random_joke = choice(data["results"])
    return f" {random_joke['joke']}"


if res["total_jokes"] > 1:
    print(f"I've got {res['total_jokes']} jokes about {msg}. Here's one:")
    print(f" {choice(res['results'])['joke']}")

elif res["total_jokes"] == 1:
    print(f"I've got one jokes about {msg}. Here's one:")
    print(f" {choice(res['results'])['joke']}")
else:
    print(f"Sorry, I don't have any jokes about {msg}! Please try again.")
