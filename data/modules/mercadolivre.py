from pandas import DataFrame
from bs4 import BeautifulSoup
from modules.scrapper import getWithBs4

def getNextUrl(url: str) -> str:
    try:
        url = [a['href'] for a in getWithBs4(url).find('li', {'class': 'andes-pagination__button andes-pagination__button--next shops__pagination-button'})][0]
        return url
    except TypeError:
        pass

def proccesPrices(prices: list) -> list:
    processedPrices = []
    for price in prices:
        if "Antes:" not in price:
            processedPrices.append(price)

    processedPrices = [i.replace('reais',"") for i in processedPrices if "reais" in i]
    processedPrices = [i.replace('con',"") for i in processedPrices if "con" in i]
    processedPrices = [i.replace('centavos',"") for i in processedPrices if "centavos" in i]
    processedPrices = [i.replace('   ',".") for i in processedPrices if "   " in i]
    processedPrices = [i.replace('  ',"") for i in processedPrices if "  " in i]
    processedPrices = [float(i) for i in processedPrices]
    return processedPrices

def getItensAndPrices(soup: BeautifulSoup) -> DataFrame:
    try:
        itens = soup.find_all('h2', class_="ui-search-item__title shops__item-title")
        itens = [content.contents for content in itens]
        itens = [item[0] for item in itens]
    except AttributeError:
        pass
    try:
        prices = soup.find_all('span', class_="price-tag-text-sr-only")
        prices = [content.contents for content in prices]
        prices = [str(price[0]) for price in prices]

        proccesedPrices = proccesPrices(prices)
        
        itens_prices = list(zip(itens,proccesedPrices))
        df = DataFrame(itens_prices, columns=['Item', 'Preco'])
        return df
    except AttributeError:
        pass
