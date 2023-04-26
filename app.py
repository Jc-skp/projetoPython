from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')
    
@app.route('/cadastro_usuario')
def cduser():
    return render_template('cadUsuario.html')
    
@app.route('/cadastro_tarefa')
def cdtarefa():
    return render_template('cadTarefas.html')

@app.route('/cadastro_projeto')
def cdproject():
    return render_template('cadProjetos.html')