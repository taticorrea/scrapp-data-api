import json
import requests
from pandas import read_csv

def post(source: str):
    url = f"http://127.0.0.1:8000/api/{source}/add_itens"
    print(source)

    df = read_csv(f'data/{source}_data/itens_precos_{source}.csv', header=0, delimiter=';', engine='python')

    for i in df.index:
        payload = json.dumps({
        "id": i,
        "nome": df["Item"][i],
        "preco": df["Preco"][i]
        })
        
        headers = {
        'Content-Type': 'application/json'
        }

        print("Sending a POTS request to a: ", url)
        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

sources = ["mercadolivre","prezunic"]
for source in sources:
    # print(source)
    post(source)
