from modules.scrapper import getWithBs4
from modules.mercadolivre import getItensAndPrices, getNextUrl


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

    getItensAndPrices(getWithBs4(firstUrl)).to_csv(f"itens_precos_{category}_mercadolivre.csv", index = False)
    
    try:
        next_url = getNextUrl(firstUrl)
    except AttributeError:
        pass
    try:
        while next_url:
            print("Sending a GET request to a: ", next_url)
            getItensAndPrices(getWithBs4(next_url)).to_csv(f"itens_precos_{category}_mercadolivre.csv", header = False, index = False, mode='a')
            next_url = getNextUrl(next_url)
    except AttributeError:
        pass