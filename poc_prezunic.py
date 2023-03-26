from modules.scrapper import getWithBs4
from modules.prezunic import getItensAndPrices, getNextUrl

basetUrls = {
        "carnes-e-aves": "https://www.prezunic.com.br/carnes-e-aves?page=",
        "automotivo":"https://www.prezunic.com.br/automotivo?page=",
        "bazar": "https://www.prezunic.com.br/bazar?page=",
        "bebida-alcoolica":"https://www.prezunic.com.br/bebida-alcoolica?page=",
        "bebida-nao-alcoolica": "https://www.prezunic.com.br/bebida-nao-alcoolica?page=",
        "congelados":"https://www.prezunic.com.br/congelados?page=",
        "frios-e-laticinios": "https://www.prezunic.com.br/frios-e-laticinios?page=",
        "higiene-e-beleza":"https://www.prezunic.com.br/higiene-e-beleza?page=",
        "hortifruti": "https://www.prezunic.com.br/hortifruti?page=",
        "limpeza":"https://www.prezunic.com.br/limpeza?page=",
        "mercearia": "https://www.prezunic.com.br/mercearia?page=",
        "padaria":"https://www.prezunic.com.br/padaria?page=",
    }

for category, firstUrl in basetUrls.items():
    print("Category: ", category)
    try:
        for page in range(1,200):
            next_url = getNextUrl(str(page), category)
            print("Sending a GET request to a: ", next_url)
            getItensAndPrices(getWithBs4(next_url)).to_csv(f"itens_precos_{category}_prezunic.csv", header = False, index = False, mode='a')
            next_url = getNextUrl(next_url, category)
    except:
        pass
