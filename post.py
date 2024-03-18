import json
import requests
from pandas import read_csv

sources = {
    "prezunic" : [
        "carnes-e-aves",
        # "bebida-alcoolica",
        # "bebida-nao-alcoolica",
        # "congelados"
        # "frios-e-laticinios",
        # "higiene-e-beleza",
        # "hortifruti",
        # "limpeza",
        # "mercearia",
    ]
}


def consolidate_json(sources: dict) -> list:
    for source, categories in sources.items():
        for category in categories:
            df = read_csv(f"data/{source}_data/{category}.csv", sep=',',header=None,names=["id","item",'preco',"fonte"],index_col=0)
            df.reset_index(drop=False,inplace=True)
            df.drop_duplicates(inplace=True)
            df.dropna(inplace=True)
            # df.to_csv(f"data/{source}_data/{category}_reset_index.csv", header=None, sep=';')
            df.to_json(f"data/{source}_data/{category}.json", orient='records', lines=False)
    
            caminho_arquivo_json = f'data/{source}_data/{category}.json'    
            json_data = []

            with open(caminho_arquivo_json, 'r') as arquivo:
                for linha in arquivo:
                    objeto_json = json.loads(linha)
                    json_data.append(objeto_json)

    return json.dumps(json_data[0])

def post(source: str):
    url = f"http://127.0.0.1:8000/api/{list(sources.keys())[0]}/add_itens"
    headers = {
    'Content-Type': 'application/json'
    }

    json_data = consolidate_json(sources)
    # print(json_data)
    print("Sending a POTS request to a: ", url)
    try:
        response = requests.request("POST", url, headers=headers, data=json_data)
        print(response.text)
    except:
        pass

post(sources)
