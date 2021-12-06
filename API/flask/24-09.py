import requests
from flask import Flask

app = Flask(__name__)

@app.route('/consultacep/<cep>', methods=['GET'])
def home(cep):

    url = 'https://viacep.com.br/ws/'
    formato = '/json/'
    r = requests.get(url + cep + formato)

    if (r.status_code == 200):
        return(r.json())

app.run(host='0.0.0.0', port=80)