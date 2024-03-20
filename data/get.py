import json
import requests

def get(source:str):
    url = f"http://127.0.0.1:8000/api/{source}/list_itens"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


sources = ["prezunic","mercadolivre"]
for source in sources:
    get(source)
