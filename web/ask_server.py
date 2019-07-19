import requests

payload = {
    'text': 'Hello this movie sucks'
}

r = requests.post('http://localhost:5000', json=payload)
print(r.content)