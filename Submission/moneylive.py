import requests
from decorators import WaitingDecorator, FormattingStar, Confirm
from config import MONEYLIVE_KEY

@Confirm
@WaitingDecorator
@FormattingStar
def livenews():
    newspaper = input("Please choose your news source (BBC/TheTimes/Sun): ")

    url = f"https://money-live.p.rapidapi.com/news/{newspaper.lower()}"

    headers = {
        "X-RapidAPI-Key": MONEYLIVE_KEY,
        "X-RapidAPI-Host": "money-live.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    print()
    print(f"TOP COST OF LIVING NEWS from {newspaper}")
    print()

    for article in data:
        print(f"{article['title']}")
        print(f"For more information, {article['url']}")
        print()