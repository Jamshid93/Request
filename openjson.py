import requests
r=requests.get('https://randomuser.me/api/')
txt=r.text
data=r.json()

results=data['results']
name=results[0]['name']
print(name)