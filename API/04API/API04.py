from flask import Flask, jsonify
from flask import request
from flask import render_template

from datetime import date

import sqlite3
from sqlite3 import Error

#######################################################
# Instancia da Aplicacao Flask

app = Flask(__name__)


#######################################################
# 1. Cadastrar produtos

@app.route('/produtos/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':

        codproduto = request.form['codproduto']
        descricao = request.form['descricao']
        precocompra = request.form['precocompra']
        precovenda = request.form['precovenda']
        datacriacao = date.today()

        mensagem = 'Erro - nao cadastrado'

        if codproduto and descricao and precocompra and precovenda and datacriacao:
            registro = (codproduto, descricao, precocompra, precovenda, datacriacao)

            try:
                conn = sqlite3.connect('database/db-produtos.db')

                sql = ''' INSERT INTO produtos(codproduto, descricao, precocompra, precovenda, datacriacao)
                              VALUES(?,?,?,?) '''

                cur = conn.cursor()

                cur.execute(sql, registro)

                conn.commit()

                mensagem = 'Sucesso - cadastrado'

            except Error as e:
                print(e)
            finally:
                conn.close()

    return render_template('cadastrar.html')


#######################################################
# 2. Listar produtos

@app.route('/produtos/listar', methods=['GET'])
def listar():
    try:
        conn = sqlite3.connect('database/db-produtos.db')

        sql = '''SELECT * FROM produtos'''

        cur = conn.cursor()

        cur.execute(sql)

        registros = cur.fetchall()

        return render_template('listar.html', regs=registros)

    except Error as e:
        print(e)
    finally:
        conn.close()


#######################################################
# 3. Excluir produtos

@app.route('/produtos/excluir/<int:codproduto>', methods=['DELETE'])

def excluir(codproduto = None):
    if codproduto == None:
        return jsonify({'mesagem': 'Parametro inválido'})
    else:
        try:
            conn = sqlite3.connect('database/db-produtos.db')

            sql = '''DELETE FROM produtos WHERE codproduto = ''' + str(codproduto)

            cur = conn.cursor()
            cur.execute(sql)

            conn.commit()

            return jsonify({'mensagem': 'Registro Excluido'})

        except Error as e:
            return jsonify({'mensagem': e})
        finally:
            conn.close()


#######################################################
# 4. Alterar/Atualizar produtos

@app.route('/produtos/alterar/<int:codproduto>', methods=['PUT'])

def alterar (codproduto = None):
    if codproduto == None:
        return jsonify({'mesagem': 'Parametro inválido'})
    else:
        try:
            conn = sqlite3.connect('database/db-produtos.db')

            sql = '''UPDATE FROM produtos WHERE idproduto = ''' + str(codproduto)

            cur = conn.cursor()
            cur.execute(sql)

            conn.commit()

            return jsonify({'mensagem': 'Registro Modificado'})

        except Error as e:
            return jsonify({'mensagem': e})
        finally:
            conn.close()

#######################################################
# Rota de Erro

@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return render_template('404.html'), 404


#######################################################
# Execucao da Aplicacao

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
#######################################################
