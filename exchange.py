import requests
import json

r=requests.get('https://api.exchangeratesapi.io/latest')

data=r.json()
print(data)