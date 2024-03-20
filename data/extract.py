import os
from shutil import rmtree
from modules.webscrapper import (parse_html_content,
                              get_itens,
                              get_max_pages,
                              get_next_url)

def scrapp_prezunic():


    args = "page"
    first_urls = {
            "carnes-e-aves":        f"https://www.prezunic.com.br/carnes-e-aves?{args}=1",
            "bebida-alcoolica":     f"https://www.prezunic.com.br/bebida-alcoolica?{args}=1",
            "bebida-nao-alcoolica": f"https://www.prezunic.com.br/bebida-nao-alcoolica?{args}=1",
            "congelados":           f"https://www.prezunic.com.br/congelados?{args}=1",
            "frios-e-laticinios":   f"https://www.prezunic.com.br/frios-e-laticinios?{args}=1",
            "higiene-e-beleza":     f"https://www.prezunic.com.br/higiene-e-beleza?{args}=1",
            "hortifruti":           f"https://www.prezunic.com.br/hortifruti?{args}=1",
            "limpeza":              f"https://www.prezunic.com.br/limpeza?{args}=1",
            "mercearia":            f"https://www.prezunic.com.br/mercearia?{args}=1"
            }

    for category, first_url in first_urls.items():
        source = "prezunic"
        path = f"data/{source}_data/{category}/"
        
        print("Category: ", category)
        print("Sending a GET request to a: ", first_url)

        if os.path.exists(path):
            rmtree(path)
            os.makedirs(path)
        else:
            os.makedirs(path)

        get_itens(source, path, category, parse_html_content(first_url))
        max_page = get_max_pages(first_url, source)

        try:
            for page_number in range(2,max_page+1):
                next_url = get_next_url(source,args,str(page_number), category)
                
                print("Sending a GET request to a: ", next_url) 
                get_itens(source, path, category, parse_html_content(next_url))
        except TypeError:
            pass

def main():   
    scrapp_prezunic()

if __name__ == "__main__":
    main()