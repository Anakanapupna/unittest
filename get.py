import requests
import json

def https_get():
    url = "https://icanhazdadjoke.com"
    headers = {"Accept":"application/json"}
    request = requests.get(url,headers=headers).json()
    return request


def main(): 
    dadjoke_json = https_get()
    print(json.dumps(dadjoke_json,indent=2))

if __name__ == '__main__':
    main()