from pandas import DataFrame
from bs4 import BeautifulSoup

def getWithBs4(url: str) -> BeautifulSoup:
    from requests import get
    try:
        response = get(url)    
        page_contents = response.text
        doc = BeautifulSoup(page_contents,'html.parser')
        return doc
    except TypeError:
        pass

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

def getItensAndPrices(doc: BeautifulSoup) -> DataFrame:
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
    firstUrls = {
            "Alimentos": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/mercearia/#origin=supermarket_navigation&from=search-frontend",
            "Bebidas": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/bebidas/#origin=supermarket_navigation&from=search-frontend",
            "Pets": "https://lista.mercadolivre.com.br/supermercado/animais/#origin=supermarket_navigation&from=search-frontend",
            "Higiene e Perfumaria": "https://lista.mercadolivre.com.br/supermercado/beleza-cuidado-pessoal/#origin=supermarket_navigation&from=search-frontend",
            "Limpeza": "https://lista.mercadolivre.com.br/supermercado/casa-moveis-decoracao/cuidado-casa-lavanderia/#origin=supermarket_navigation&from=search-frontend",
            "Bebês": "https://lista.mercadolivre.com.br/supermercado/bebes/#origin=supermarket_navigation&from=search-frontend"        
        }

    for category, firstUrl in firstUrls.items():
        print("Category: ", category)
        print("Sending a GET request to a: ", firstUrl)

        getItensAndPrices(getWithBs4(getNextUrl(firstUrl))).to_csv(f"itens_precos_{category}_mercadolivre.csv", index = False, mode='a')
        
        try:
            next_url = getNextUrl(firstUrl)
        except AttributeError:
            pass
        try:
            while next_url:
                print("Sending a GET request to a: ", next_url)
                getItensAndPrices(getWithBs4(getNextUrl(next_url))).to_csv(f"itens_precos_{category}_mercadolivre.csv", header = False, index = False, mode='a')
                next_url = getNextUrl(next_url)
        except AttributeError:
            pass

main()