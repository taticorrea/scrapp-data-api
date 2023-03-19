from bs4 import BeautifulSoup
import requests
import pandas as pd

def get(url: str) -> BeautifulSoup:
    if url is not None:
        response = requests.get(url)    
        page_contents = response.text
        doc = BeautifulSoup(page_contents,'html.parser')
        return doc
    else: 
        pass

def getNextUrl(url: str) -> str:
    try:
        url = [a['href'] for a in get(url).find('li', {'class': 'andes-pagination__button andes-pagination__button--next shops__pagination-button'})][0]
        if url is not None:
            return url
    except TypeError:
        pass

def proccesPrices(prices: list) -> list:
    pricesFiltered = []
    for price in prices:
        if "Antes:" not in price:
            pricesFiltered.append(price)

    pricesFiltered = [i.replace('reais',"") for i in pricesFiltered if "reais" in i]
    pricesFiltered = [i.replace('con',"") for i in pricesFiltered if "con" in i]
    pricesFiltered = [i.replace('centavos',"") for i in pricesFiltered if "centavos" in i]
    pricesFiltered = [i.replace('   ',".") for i in pricesFiltered if "   " in i]
    pricesFiltered = [i.replace('  ',"") for i in pricesFiltered if "  " in i]
    pricesFiltered = [float(i) for i in pricesFiltered]
    return pricesFiltered

def getItensAndPrices(doc: BeautifulSoup) -> pd.DataFrame:
    try:
        itens = doc.find_all('h2', class_="ui-search-item__title shops__item-title")
        itens = [content.contents for content in itens]
        itens = [i[0] for i in itens]
    except AttributeError:
        pass
    try:
        prices = doc.find_all('span', class_="price-tag-text-sr-only")
        prices = [content.contents for content in prices]
        prices = [str(i[0]) for i in prices]

        pricesFiltered = proccesPrices(prices)
        
        itens_prices = list(zip(itens,pricesFiltered))
        df = pd.DataFrame(itens_prices, columns=['Item', 'Preço'])
        return df
    except AttributeError:
        pass

def main():
    first_urls = {
            "Alimentos": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/mercearia/#origin=supermarket_navigation&from=search-frontend",
            "Bebidas": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/bebidas/#origin=supermarket_navigation&from=search-frontend",
            "Pets": "https://lista.mercadolivre.com.br/supermercado/animais/#origin=supermarket_navigation&from=search-frontend",
            "Higiene e Perfumaria": "https://lista.mercadolivre.com.br/supermercado/beleza-cuidado-pessoal/#origin=supermarket_navigation&from=search-frontend",
            "Limpeza": "https://lista.mercadolivre.com.br/supermercado/casa-moveis-decoracao/cuidado-casa-lavanderia/#origin=supermarket_navigation&from=search-frontend",
            "Bebês": "https://lista.mercadolivre.com.br/supermercado/bebes/#origin=supermarket_navigation&from=search-frontend"        
        }

    for category, first_url in first_urls.items():
        print("Category: ", category)
        print("Sending a GET request to a url: ", first_url)

        getItensAndPrices(get(getNextUrl(first_url))).to_csv(f"itens_precos_{category}_mercadolivre.csv", index = False, mode='a')
        
        try:
            next_url = getNextUrl(first_url)
        except AttributeError:
            pass
        try:
            while next_url:
                print("Sending a GET request to a url: ", next_url)
                getItensAndPrices(get(getNextUrl(next_url))).to_csv(f"itens_precos_{category}_mercadolivre.csv", header = False, index = False, mode='a')
                next_url = getNextUrl(next_url)
        except AttributeError:
            pass

main()