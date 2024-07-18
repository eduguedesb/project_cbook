from flask import Flask, render_template, request, redirect, url_for, flash, session
import mysql.connector
from config import Config
import random
import string

app = Flask(__name__)

# Configuração do banco de dados
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_cbook",
    port="3307"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT tb_dados.id, tb_dados.nome, tb_dados.email, tb_dados.telefone, tb_dados.data_criacao, tb_dados.descricao, tb_categorias.nome_categoria AS categoria_nome FROM tb_dados JOIN tb_categorias ON tb_dados.categoria = tb_categorias.id_categoria")

    #cursor.execute("SELECT * FROM tb_dados")
    results = cursor.fetchall()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
