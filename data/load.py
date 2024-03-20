import json
import requests
from pandas import read_csv

sources = {
    "prezunic" : [
        "carnes-e-aves",
        "bebida-alcoolica",
        "bebida-nao-alcoolica",
        "congelados"
        "frios-e-laticinios",
        "higiene-e-beleza",
        "hortifruti",
        "limpeza",
        "mercearia",
    ]
}

def post(sources: dict):
    url = f"http://127.0.0.1:8000/api/{list(sources.keys())[0]}/add_itens"
    headers = {
    'Content-Type': 'application/json'
    }

    for source, categories in sources.items():
        for category in categories:
            json_file_path = f"data/{source}_data/{category}/{category}.json"
            data = []
            with open(json_file_path, 'r') as file:
                for line in file:
                    objeto_json = json.loads(line)
                    data.append(objeto_json)
    
    json_data = json.dumps(data[0])
    print("Sending a POTS request to a: ", url)

    try:
        response = requests.request("POST", url, headers=headers, data=json_data)
        print(response.text)
    except:
        pass

post(sources)          


