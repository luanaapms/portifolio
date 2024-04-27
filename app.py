from flask import Flask, render_template 
app = Flask(__name__, static_url_path='/static', template_folder='template')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/projetos")
def projetos():
    return render_template('projetos.html')

@app.route("/contatos")
def contatos():
    return render_template('contatos.html')


