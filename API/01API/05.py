import requests

r = requests.get('http://www.google.com/search', params={'q': 'elson de abreu'})
if (r.status_code == 200):
    print()
    print('Retorno : ', r.text)
    arq = open("C:\\Users\\casa\\Pictures\\AulaElson1309.html", 'w')
    arq.write(r.text)
    arq.close()
else:
    print('Nao houve sucesso na requisicao.')


