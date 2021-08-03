import requests
import json

def https_get(id = None):
    if id == None:
        url = "https://icanhazdadjoke.com/"
    else:
        url = "https://icanhazdadjoke.com/j/" + id
    headers = {"Accept":"application/json"}
    request = requests.get(url,headers=headers).json()
    return request


def main(): 
    dadjoke_json = https_get()
    print("First Joke is " + dadjoke_json["joke"])
    #print(json.dumps(dadjoke_json,indent=2))
    joke_id = dadjoke_json["id"]
    dadjoke2_json = https_get(joke_id)
    print("Second Joke is " + dadjoke2_json["joke"])


if __name__ == '__main__':
    main()