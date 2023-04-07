from requests import get
from pandas import DataFrame
from bs4 import BeautifulSoup

def getWithBs4(url: str) -> BeautifulSoup:
    try:
        response = get(url)
        page_contents = response.text
        soup = BeautifulSoup(page_contents ,'html.parser')
        return soup
    except:
        pass

def getNextUrl(url_base, category: str, args: str, page: str) -> str:
    url = f"{url_base}{category}?{args}" + page
    return url

def dataTransformation(df: DataFrame, source: str) -> DataFrame:
    df["Fonte"] = source
    return df
