import json
from re import search
from pandas import DataFrame
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tenacity import retry, stop_after_attempt, wait_fixed

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def parse_html_content(url: str) -> BeautifulSoup:
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(url)
        driver.implicitly_wait(20) 
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")   
        return soup
    finally:
        driver.quit()

def get_itens(source: str, path: str, category: str, soup: BeautifulSoup) -> DataFrame:
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
            df.drop_duplicates(inplace=True)         
            df.to_csv(f"{path}/{category}.csv", sep = ';', header = False, index = True,  mode='a')

        except (KeyError, IndexError) as err:
            pass

def get_max_pages(url: str, source: str) -> int:
    soup = parse_html_content(url)
    if source=="prezunic":
        span_class = soup.find("span", {"class":"prezunic-prezunic-components-2-x-showingPages"})
        numero = search(r'Página \d+ de (\d+)', span_class.text)
        if numero:
            max_pages = int(numero.group(1))
            print('Páginas: ',max_pages)
            return max_pages

def get_next_url(source: str, args: str, page: str, category: str) -> str:
    if source=="prezunic":
        url_base = "https://www.prezunic.com.br/"
    try:
        url = f"{url_base}{category}?{args}=" + page
        return url
    except:
        pass