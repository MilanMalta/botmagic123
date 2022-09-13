import requests

res = requests.get('https://api.ipify.org?format=json')

print(res.text)
