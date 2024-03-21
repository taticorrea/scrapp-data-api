import requests
from pandas import read_csv

def delete(source:str):
    try:
        url = f"http://127.0.0.1:8000/api/v2/delete-item/?fonte={source}"

        payload={}
        headers = {
        'Content-Type': 'application/json'
        }

        print("Sending a DELETE request to a: ", url)
        response = requests.request("DELETE", url, headers=headers, data=payload)
        print('Response Code:', response.status_code)
    except:
        pass    

sources = ["Prezunic"]
for source in sources:
    delete(source)
