import mysql.connector
from flask import Flask, render_template
from flask import request # importa request para pegar dados do formulário 

app = Flask(__name__)

@app.route('/') # Define a URL principal
def home(): # Função executada ao acessar
    return 'Bem vindo a Old-Tech-Store!' # Resposta para o usuário

def conectar_banco(): # Função para conectar ao MySQL
 conn = mysql.connector.connect(
 host="localhost", # Servidor local
 user="root", # Usuário do MySQL
 password="", # Senha do MySQL
 database="ecommerce_db" # Nome do banco
 )
 return conn # Retorna a conexão

#ROTA DE CADASTRO
@app.route("/cadastro", methods= ["GET", "POST"])
def cadastro():
   if request.method == "POST": #verifica se o formulário foi enviado
      #Pega os dados do formulário
      nome = request.form["nome"] #Pega o valor digitado no campo nome 
      email = request.form["email"] #Pega o valor digitado no campo de email
      senha = request.form["senha"] #Pega o valor digitado no campo de senha

      #Conecta do banco MySQL
      conn = conectar_banco()
      cursor = conn.cursor()
      
      #Insere um novo usuário
      cursor.execute(
       "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)", # %s -> placeholder do MySQL (diferente do ? do SQLite) e INSERT INTO -> Salva o novo usuário no banco
      (nome, email, senha)
      )
   
      #Salva e fecha
      conn.commit()
      conn.close()

      return "Cadastro realizado com sucesso!"

#Se for GET, mostra o formulário
   return render_template("cadastro.html")