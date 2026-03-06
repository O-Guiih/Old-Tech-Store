import _mysql_connector
from flask import Flask

app = Flask(__name__)

@app.route('/') # Define a URL principal
def home(): # Função executada ao acessar
    return 'Bem vindo a Old-Tech-Store!' # Resposta para o usuário