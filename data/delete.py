import requests
from pandas import read_csv

def delete(source:str):
    # df = read_csv(f"data/{source}_data/itens_precos_{source}.csv", header=0,sep=';', engine='python')

    try:
        for i in range(256):
            url = f"http://127.0.0.1:8000/api/{source}/delete_item/{i}"

            payload={}
            headers = {}

            response = requests.request("DELETE", url, headers=headers, data=payload)

            print(response.text)
    except:
        pass
sources = ["prezunic"]

for source in sources:
    delete(source)
