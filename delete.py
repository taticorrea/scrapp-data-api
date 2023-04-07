import requests

def delete(source:str):
    try:
        for i in range(0,1130):
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
