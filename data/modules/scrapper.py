from requests import get
from pandas import DataFrame
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")


def getWithBs4(url: str) -> BeautifulSoup:

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(3) 
    
    html = driver.page_source
    
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")   
    return soup

def getNextUrl(url_base, category: str, args: str, page: str) -> str:
    url = f"{url_base}{category}?{args}" + page
    return url