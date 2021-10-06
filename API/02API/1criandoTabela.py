import sqlite3

conn = sqlite3.connect('bdcotacoes.db')
print('Banco de dados aberto com sucesso')

conn.execute('''CREATE TABLE "moedas" (
"Data"	TEXT     NOT NULL,
"Dolar"	INTEGER  NOT NULL,
"Euro"	INTEGER  NOT NULL,
PRIMARY KEY("Data")); ''')

print('Tabela criada com sucesso')
conn.close()