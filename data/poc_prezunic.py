import os
from shutil import rmtree
from pandas import read_csv, concat, DataFrame, notnull
from modules.scrapper import getWithBs4, dataTransformation
from modules.prezunic import getItensAndPrices, getNextUrl

basetUrls = {
        "carnes-e-aves": "https://www.prezunic.com.br/carnes-e-aves?page=",
        "bebida-alcoolica":"https://www.prezunic.com.br/bebida-alcoolica?page=",
        "bebida-nao-alcoolica": "https://www.prezunic.com.br/bebida-nao-alcoolica?page=",
        "congelados":"https://www.prezunic.com.br/congelados?page=",
        "frios-e-laticinios": "https://www.prezunic.com.br/frios-e-laticinios?page=",
        "higiene-e-beleza":"https://www.prezunic.com.br/higiene-e-beleza?page=",
        "hortifruti": "https://www.prezunic.com.br/hortifruti?page=",
        "limpeza":"https://www.prezunic.com.br/limpeza?page=",
        "mercearia": "https://www.prezunic.com.br/mercearia?page="
        }

source = "prezunic"
path = f"data/{source}_data"

df_result = DataFrame({'Item' : [], "Preco": [], "Fonte": []})

if os.path.exists(path) and os.path.isdir(path):
    rmtree(path)
    os.mkdir(path)
else:
    os.mkdir(path)
    
for category, firstUrl in basetUrls.items():
    try:
        print("Category: ", category)
        dataTransformation(getItensAndPrices(getWithBs4(firstUrl)),source).to_csv(f"{path}/itens_precos_{category}_prezunic.csv", header=True, sep = ';', index = False)
        for page in range(1,200):
            next_url = getNextUrl(str(page), category)
            
            print("Sending a GET request to a: ", next_url)
            
            dataTransformation(getItensAndPrices(getWithBs4(next_url)),source).to_csv(f"{path}/itens_precos_{category}_prezunic.csv", sep = ';', header = False, index = False, mode='a')
                        
            df = read_csv(f"{path}/itens_precos_{category}_prezunic.csv", header=0, delimiter=';')
            df_result = concat([df_result,df])
    except:
        pass

df_result = df_result.where(notnull(df_result), None)
df_result.to_csv(f"{path}/itens_precos_{source}.csv", sep = ';', header = True, index = False, mode='a')
