from flask import Flask
import os
from dotenv import load_dotenv
# import pyodbc


load_dotenv()
SECRET = os.getenv("SECRET")
server = os.getenv("server")
database = os.getenv("database")
tabela = os.getenv("tabela")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<h1>Integração contínua_UP</h1> <p>{SECRET}</p>"

# @app.route("/banco")
# def banco():
#     try:
#         dados_conexao = (
#             "Driver={SQL Server};"
#             f"Server={server};"
#             f"Database={database};"
#         )
#
#         connection = pyodbc.connect(dados_conexao)
#         print('connected')
#
#         cursor = connection.cursor()
#         cursor.execute(f"SELECT top 100 * FROM {tabela}")
#
#     except:
#         print('Erro na conexão como banco!')
#
#     html_string = ""
#
#     if cursor.rowcount:
#         for row in cursor.fetchall():
#             html_string = html_string + f"<p>{row}</p>"
#
#     return html_string

if __name__=="__main__":

    app.run(debug=True)

    #teste2
