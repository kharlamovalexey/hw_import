import requests
def get_employees():
    data  = requests.get('https://akabab.github.io/superhero-api/api/all.json').json()
    return data