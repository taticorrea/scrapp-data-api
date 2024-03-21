from json import loads, dumps
from requests import request

sources = {
    "prezunic" : [
        "carnes-e-aves"
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
    url = f"http://127.0.0.1:8000/api/v2/create-item"
    headers = {
    'Content-Type': 'application/json'
    }

    for source, categories in sources.items():
        for category in categories:
            json_file_path = f"data/{source}_data/{category}/{category}.json"
            data = []
            with open(json_file_path, 'r') as file:
                for line in file:
                    objeto_json = loads(line)
                    data.append(objeto_json)
    
    json_data = dumps(data[0])
    print("Sending a POST request to a: ", url)

    try:
        response = request("POST", url, headers=headers, data=json_data)
        print('Response Code:', response.status_code)
    except:
        pass

post(sources)          


