import requests
import json
for i in range(100):
    r=requests.get('https://randomuser.me/api/')
    if r.status_code:
        print(i)
        data=r.json()
        result=data['results'][0]['name']
        print(result)