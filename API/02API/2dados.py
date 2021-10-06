import sqlite3
import requests
from datetime import date

conn = sqlite3.connect('bdcotacoes.db')
print('\nBanco de dados aberto com sucesso')

r = requests.get('https://api.hgbrasil.com/finance?format=json-cors&key=bbd4b1d1')
resposta = r.json()
Data = date.today()
Exibir_data = Data.strftime("%d/%m/%Y")
Dolar = resposta['results']['currencies']['USD']['buy']
Euro = resposta['results']['currencies']['EUR']['buy']

def inserir():
    conn.execute("INSERT INTO moedas (Data, Dolar, Euro) \
            VALUES(?, ?, ?)", (Exibir_data, Dolar, Euro))

    conn.commit()
    print('Dados inseridos com sucesso\n')

def buscar():
    busca = conn.execute("SELECT Data, Dolar, Euro from moedas")
    for row in busca:
        print('Cotação Atual:')
        print("Data = ", row[0])
        print("Dólar = ", row[1])
        print("Euro = ", row[2])

    print("\nOperação realizada com sucesso")
    conn.close()

if r.status_code == 200:
    inserir()
    buscar()
else:
    print('Erro!')