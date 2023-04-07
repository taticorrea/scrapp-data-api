import json
from pandas import DataFrame
from bs4 import BeautifulSoup
# from modules.scrapper import getWithBs4

def getItensAndPrices(soup: BeautifulSoup) -> list:
    # try:
    itens = soup.find_all('div')
    return itens
    # itens = [content.contents for content in itens]
    # itens = [item[0] for item in itens]
    # except AttributeError:
    #     pass
    # try:
    #     prices = soup.find_all('div', class_="price-tag-normalstyle__LabelPrice-sc-1co9fex-0 lkWvql")
    #     prices = [content.contents for content in prices]
    #     prices = [str(price[0]) for price in prices]

        # proccesedPrices = proccesPrices(prices)
        
        # itens_prices = list(zip(itens,prices))
        # df = DataFrame(itens, columns=['Item', 'Preço'])
        # return df
    # except AttributeError:
    #     pass