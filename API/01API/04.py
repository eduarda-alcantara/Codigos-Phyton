import requests

url = 'https://viacep.com.br/abc/'
r = requests.get(url)
print()
print('Retorno:', r.status_code)
print(r.text)
print()




