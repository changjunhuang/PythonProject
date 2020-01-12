import requests

r = requests.get('https://baidu.com')
print(r.text)