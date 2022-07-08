from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()
SECRET = os.getenv("SECRET")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<h1>Integração contínua</h1> <p>{SECRET}</p>"

if __name__=="__main__":
    app.run(debug=True)

    #teste2
