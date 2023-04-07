import json
from pandas import DataFrame
from bs4 import BeautifulSoup

def getItensAndPrices(soup: BeautifulSoup) -> DataFrame:
    try:
        script = soup.find_all("script")[4].text
        script = json.loads(script)
        itens = [script["itemListElement"][i]["item"]["name"] for i in range(24)]
        prices = [script["itemListElement"][i]["item"]["offers"]["highPrice"] for i in range(24)]
        itens_prices = list(zip(itens,prices))
        df = DataFrame(itens_prices, columns=['Item','Preco'])
        return df
    except:
        pass

def getNextUrl(page: str, category: str) -> str:
    url = f"https://www.prezunic.com.br/{category}?page=" + page
    return url
