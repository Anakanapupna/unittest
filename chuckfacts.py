import requests
import json

def get_chuck_facts(joke_number):
    url = "http://api.icndb.com/jokes/" + str(joke_number)
    request = requests.get(url)
    chuck_json = request.json()

    return chuck_json


def main():
    n = 1
    while True:
        try:
            chuck_fact = get_chuck_facts(n)
            print(str(n) + ". " + chuck_fact["value"]["joke"])
            
        except:
            print(str(n) + ". Chuck Norris Killed That Joke!")
        n+=1
if __name__ == '__main__':
    main()
