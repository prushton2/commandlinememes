from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests



def search(query):
    # query = "sponebob"

    response = requests.get(f"https://imgflip.com/search?q={query}")

    with open("response.html", "w") as f:
        f.write(response.text)

    soup = None

    with open("response.html") as fp:
        soup = BeautifulSoup(fp, features="lxml")

