import os
from shutil import rmtree
from modules.scrapper import getWithBs4
from modules.prezunic import get_itens, get_next_url, get_max_pages

source = "prezunic"
path = f"data/{source}_data"

if os.path.exists(path) and os.path.isdir(path):
    rmtree(path)
    os.mkdir(path)
else:
    os.mkdir(path)

first_urls = {
        "carnes-e-aves": "https://www.prezunic.com.br/carnes-e-aves?page=1",
        "bebida-alcoolica":"https://www.prezunic.com.br/bebida-alcoolica?page=1",
        # "bebida-nao-alcoolica": "https://www.prezunic.com.br/bebida-nao-alcoolica?page=",
        # "congelados":"https://www.prezunic.com.br/congelados?page=",
        # "frios-e-laticinios": "https://www.prezunic.com.br/frios-e-laticinios?page=",
        # "higiene-e-beleza":"https://www.prezunic.com.br/higiene-e-beleza?page=",
        # "hortifruti": "https://www.prezunic.com.br/hortifruti?page=",
        # "limpeza":"https://www.prezunic.com.br/limpeza?page=",
        # "mercearia": "https://www.prezunic.com.br/mercearia?page="
        }

for category, first_url in first_urls.items():
    print("Category: ", category)
    print("Sending a GET request to a: ", first_url)
    # get_itens(path, category, getWithBs4(first_url))
    max_page = get_max_pages(first_url)

    for page_number in range(2,max_page+1):
        next_url = get_next_url(str(page_number), category)
        
        print("Sending a GET request to a: ", next_url) 
        get_itens(path, category, getWithBs4(next_url))