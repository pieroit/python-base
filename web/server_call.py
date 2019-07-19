import requests

URL = 'http://localhost:5000/personaggi'

response = requests.get(URL)
print(response.json())

nuovo = {
    'nome' : 'Rockfeller',
    'sesso': 'M',
    'eta'  : 62
}
response = requests.post(URL, json=nuovo)

response = requests.get(URL)
print(response.json())