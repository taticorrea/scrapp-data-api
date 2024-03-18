import re
import json
from pandas import DataFrame
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')


def parse_html_content(url: str) -> BeautifulSoup:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(5) 
    
    html = driver.page_source
    
    driver.quit()

    soup = BeautifulSoup(html, "html.parser")   
    return soup

def get_itens(source: str, path: str, category: str ,soup: BeautifulSoup) -> DataFrame:
    if source=="prezunic":
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
            df = DataFrame(dict_data.items(), columns=['item','preco'])
            df["fonte"] = "Prezunic"
            # df["id"] = df.index
            
            df.drop_duplicates(inplace=True)
            df.to_csv(f"{path}/{category}.csv", sep = ';', header = False, index = True,  mode='a')
            # df.to_json(f"{path}/{category}.json",orient='records',lines=True, mode="a")
        except (KeyError, IndexError) as err:
            pass


def get_max_pages(url: str) -> int:
    soup = parse_html_content(url)
    span_class = soup.find("span", {"class":"prezunic-prezunic-components-2-x-showingPages"})
    numero = re.search(r'Página \d+ de (\d+)', span_class.text)
    if numero:
        max_pages = int(numero.group(1))
        return max_pages

def get_next_url(source: str, args: str, page: str, category: str) -> str:
    if source=="prezunic":
        url_base = "https://www.prezunic.com.br/"
    try:
        url = f"{url_base}{category}?{args}=" + page
        return url
    except:
        pass