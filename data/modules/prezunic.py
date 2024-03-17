import json
import re
from pandas import DataFrame
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")

def get_itens(path: str, category: str ,soup: BeautifulSoup) -> DataFrame:
    script_tags = soup.find_all("script",{"type":"application/ld+json"})
    dict_data = {}
    script_contents = []
    list_data=[]
    for script_tag in script_tags:
        script_contents.append(json.loads(script_tag.text))
    for item in script_contents:
        item_type = item["@type"]
        if item_type == "ItemList":
            list_data.append(item)
        else:
            pass
    
    list_itens =[item["itemListElement"] for item in list_data]
    try:
        itens = list_itens[0]
        itens_names = [item["item"]["name"] for item in itens]
        itens_prices = [item["item"]["offers"]["highPrice"] for item in itens]
    
        dict_data = dict(zip(itens_names,itens_prices))

        # lista_de_jsons = []
        # with open(f"{path}/itens_precos_{category}_prezunic.json", 'a') as arquivo:
        #     arquivo.write(json.dumps(dict_data, indent=4))

        df = DataFrame(dict_data.items(), columns=['Item','Preco'])
        df["Fonte"] = "Prezunic"
        df.to_csv(f"{path}/itens_precos_{category}_prezunic.csv", sep = ';', header = False, index = False, mode='a')
    except IndexError:
        pass


def get_max_pages(url: str) -> int:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(3) 
    
    html = driver.page_source
    
    driver.quit()
    soup = BeautifulSoup(html ,'html.parser')
    span_class = soup.find("span", {"class":"prezunic-prezunic-components-2-x-showingPages"})
    numero = re.search(r'Página \d+ de (\d+)', span_class.text)
    if numero:
        max_pages = int(numero.group(1))
    return max_pages


def get_next_url(page: str, category: str) -> str:
    try:
        url = f"https://www.prezunic.com.br/{category}?page=" + page
        return url
    except:
        pass