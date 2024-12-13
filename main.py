import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

def realtime(coin):

    coin = "bitcoin"
    response = requests.get("https://www.google.com/search?q=" + coin + 'price')
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    # find the current price
    price = soup.find('div', attrs={
        'class': 'BNeawe iBp4i AP7Wnd'
    }).text
    return price


coin= "bitcoin"
result = realtime(coin)
print(result)
