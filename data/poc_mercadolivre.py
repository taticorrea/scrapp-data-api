import os
from shutil import rmtree
from pandas import read_csv, concat, DataFrame, notnull
from modules.scrapper import getWithBs4, dataTransformation
from modules.mercadolivre import getItensAndPrices, getNextUrl

firstUrls = {
        "Alimentos": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/mercearia/#origin=supermarket_navigation&from=search-frontend",
        "Bebidas": "https://lista.mercadolivre.com.br/supermercado/alimentos-bebidas/bebidas/#origin=supermarket_navigation&from=search-frontend",
        "Pets": "https://lista.mercadolivre.com.br/supermercado/animais/#origin=supermarket_navigation&from=search-frontend",
        "Higiene e Perfumaria": "https://lista.mercadolivre.com.br/supermercado/beleza-cuidado-pessoal/#origin=supermarket_navigation&from=search-frontend",
        "Limpeza": "https://lista.mercadolivre.com.br/supermercado/casa-moveis-decoracao/cuidado-casa-lavanderia/#origin=supermarket_navigation&from=search-frontend",
        "Bebês": "https://lista.mercadolivre.com.br/supermercado/bebes/#origin=supermarket_navigation&from=search-frontend"
    }

df_result = DataFrame({'Item' : [], "Preco": [], "Fonte": []})

source = "mercadolivre"
path = f"data/{source}_data/"

if os.path.exists(path) and os.path.isdir(path):
    rmtree(path)
    os.mkdir(path)
else:
    os.mkdir(path)

for category, firstUrl in firstUrls.items():
    print("Category: ", category)
    print("Sending a GET request to a: ", firstUrl)
    dataTransformation(getItensAndPrices(getWithBs4(firstUrl)),source).to_csv(f"{path}/itens_precos_{category}_mercadolivre.csv", sep = ';', index = False)
    try:
        next_url = getNextUrl(firstUrl)
    except AttributeError:
        pass
    try:
        while next_url:
            print("Sending a GET request to a: ", next_url)           
            dataTransformation(getItensAndPrices(getWithBs4(next_url)),source).to_csv(f"{path}/itens_precos_{category}_mercadolivre.csv", sep = ';',header = False, index = False, mode='a')
            next_url = getNextUrl(next_url)
    except:
        pass
    df = read_csv(f"{path}/itens_precos_{category}_{source}.csv", header=0, delimiter=';')
    df_result = concat([df_result,df])

df_result = df_result.where(notnull(df_result), None)
df_result.to_csv(f"{path}/itens_precos_{source}.csv", sep = ';', header = True, index = False, mode='a')

