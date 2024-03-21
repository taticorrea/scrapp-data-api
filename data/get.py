import json
import requests

def get(source:str):
    url = f"http://127.0.0.1:8000/api/v2/item?fonte={source}"

    payload={}
    headers = {
    'Content-Type': 'application/json'  
    }

    print("Sending a GET request to a: ", url)
    response = requests.request("GET", url, headers=headers, data=payload)

    print('Response Code:', response.status_code)
    # print('Response Data:', response.text)


sources = ["Prezunic"]
for source in sources:
    get(source)
