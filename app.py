import mysql.connector
from flask import Flask

app = Flask(__name__)

@app.route('/') # Define a URL principal
def home(): # Função executada ao acessar
    return 'Bem vindo a Old-Tech-Store!' # Resposta para o usuário

def conectar_banco(): # Função para conectar ao MySQL
 conn = mysql.connector.connect(
 host="localhost", # Servidor local
 user="root", # Usuário do MySQL
 password="sua_senha", # Senha do MySQL
 database="ecommerce_db" # Nome do banco
 )
 return conn # Retorna a conexão