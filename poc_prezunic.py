from bs4 import BeautifulSoup
import requests
import pandas as pd

def getWithBs4(url: str) -> tuple[BeautifulSoup, str]:
    if url is not None:
        response = requests.get(url)    
        page_contents = response.text
        doc = BeautifulSoup(page_contents,'html.parser')
        return (doc,page_contents)
    else: 
        pass

# def getNextUrl(url: str) -> str:
#     try:
#         url = [a['href'] for a in get(url).find('li', {'class': 'andes-pagination__button andes-pagination__button--next shops__pagination-button'})][0]
#         if url is not None:
#             return url
#     except TypeError:
#         pass

# def proccesPrices(prices: list) -> list:
#     pricesFiltered = []
#     for price in prices:
#         if "Antes:" not in price:
#             pricesFiltered.append(price)

#     pricesFiltered = [i.replace('reais',"") for i in pricesFiltered if "reais" in i]
#     pricesFiltered = [i.replace('con',"") for i in pricesFiltered if "con" in i]
#     pricesFiltered = [i.replace('centavos',"") for i in pricesFiltered if "centavos" in i]
#     pricesFiltered = [i.replace('   ',".") for i in pricesFiltered if "   " in i]
#     pricesFiltered = [i.replace('  ',"") for i in pricesFiltered if "  " in i]
#     pricesFiltered = [float(i) for i in pricesFiltered]
#     return pricesFiltered

def getItensAndPrices(doc: BeautifulSoup) -> pd.DataFrame:
    try:
        itensFalse = doc.find_all('span', class_="prezunic-prezunic-components-0-x-ProductName false")
        itensFalse = [content.contents for content in itensFalse]
        itensFalse = [i[0] for i in itensFalse]

        itensUndefined = doc.find_all('span', class_="prezunic-prezunic-components-0-x-ProductName undefined")
        itensUndefined = [content.contents for content in itensUndefined]
        itensUndefined = [i[0] for i in itensUndefined]

        allItens = itensFalse + itensUndefined
        print(itensUndefined)

#     int_prices = doc.find_all('span', class_="prezunic-prezunic-components-0-x-currencyInteger")
#     int_prices = [int_prices[i].contents for i in range(len(int_prices))]
#     int_prices = [str(i[0]) for i in int_prices]

    # pricesFiltered = proccesPrices(int_prices)
    
    # itens_prices = list(zip(allItens,int_prices))
        df = pd.DataFrame(allItens, columns=['Item'])
        df.to_csv("itens_precos_prezunic.csv", index = False)
        return df
    except AttributeError as error:
        print(error)

url = "https://www.prezunic.com.br/carnes-e-aves/carnes"
with open("main.html", "w", encoding='utf-8') as file:
    file.write(getWithBs4(url)[1])
getItensAndPrices(getWithBs4(url)[0])

# def main():
#     first_urls = {
#             "Alimentos": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/mercearia/#origin=supermarket_navigation&from=search-frontend",
#             "Bebidas": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/bebidas/#origin=supermarket_navigation&from=search-frontend",
#             "Pets": "https://lista.mercadolivre.com.br/supermercado/animais/#origin=supermarket_navigation&from=search-frontend",
#             "Higiene e Perfumaria": "https://lista.mercadolivre.com.br/supermercado/beleza-cuidado-pessoal/#origin=supermarket_navigation&from=search-frontend",
#             "Limpeza": "https://lista.mercadolivre.com.br/supermercado/casa-moveis-decoracao/cuidado-casa-lavanderia/#origin=supermarket_navigation&from=search-frontend",
#             "Bebês": "https://lista.mercadolivre.com.br/supermercado/bebes/#origin=supermarket_navigation&from=search-frontend"        
#         }

#     for category, first_url in first_urls.items():
#         print("Category: ", category)
#         print("Sending a GET request to a url: ", first_url)

#         getItensAndPrices(get(getNextUrl(first_url))).to_csv(f"itens_precos_{category}_mercadolivre.csv", index = False, mode='a')
        
#         try:
#             next_url = getNextUrl(first_url)
#         except AttributeError:
#             pass
#         try:
#             while next_url:
#                 print("Sending a GET request to a url: ", next_url)
#                 getItensAndPrices(get(getNextUrl(next_url))).to_csv(f"itens_precos_{category}_mercadolivre.csv", header = False, index = False, mode='a')
#                 next_url = getNextUrl(next_url)
#         except AttributeError:
#             pass

# main()