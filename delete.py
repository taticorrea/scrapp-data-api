import requests

def delete(source:str):
    for i in range(2854,2856):
        url = f"http://127.0.0.1:8000/api/{source}/delete_item/{i}"

        payload={}
        headers = {}

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)
source = "mercadolivre"
delete(source)
