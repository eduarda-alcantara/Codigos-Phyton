from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return('HOME: Bem vindo ao site !')


@app.route('/autores', methods=['GET'])
def nome_dos_desenvolvedores():
    return('Turma de desenvolvimento')


@app.route('/help', methods=['GET'])
def ajuda():
    return('Este é o tópico de ajuda do sistema')


app.run(host='0.0.0.0', port=80)