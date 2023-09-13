from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import json

import requests



class SearchResult:
    def __init__(self, name, url):
        self.name = name
        self.url = url


def search(query):
    response = requests.get(f"https://imgflip.com/search?q={query}")

    with open("response.html", "w") as f:
        f.write(response.text)

    soup = None

    with open("response.html") as fp:
        soup = BeautifulSoup(fp, features="lxml")

    searchchunk = soup.find(id="s-results")
    
    resultlist = searchchunk.findChildren("a", recursive=False)
    
    searchresults = []
    
    try:
        for i, j in enumerate(resultlist):
            splitelement = str(j).split(">")
            searchresults.append(
                SearchResult(
                    splitelement[1].split("\"")[1],
                    splitelement[0].split("\"")[3]
                )
            )

    except:
        pass
    return searchresults
    #     return []

def loadDriver(config):
    config = json.loads(config)
    # this will be a choice (COOL!!!)
    if(config["browser"] == "Firefox"):
        return webdriver.Firefox()
    if(config["browser"] == "Chrome"):
        return webdriver.Chrome()



def createMeme(driver, text, url):
    driver.get(f"https://imgflip.com{url}")
    
    element = driver.find_element(By.CLASS_NAME, "recaption-text")
    element.click()
    boxesContainer = driver.find_element(By.CLASS_NAME, "mm-boxes")

    boxes = boxesContainer.find_elements(By.CLASS_NAME, "mm-text")
    # print(boxes)

    for i, j in enumerate(boxes):

        boxes[i].send_keys(text[i])

    generate = driver.find_element(By.XPATH,"//*[text()='Generate']")
    generate.click()