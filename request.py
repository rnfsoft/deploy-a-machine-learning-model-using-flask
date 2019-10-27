import requests

url = 'http://localhost:5000/api'

r = requests.post(url, json={'exp':5.0})
print(r.json())