from flask import render_template, redirect, session, request, flash
from flask_app import app

#Importación del modelo
from flask_app.models.users import User

#Importación BCrypt

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrate', methods=['POST'])
def registrate():
    #Validar la información ingresada
    if not User.valida_usuario(request.form):
        return redirect('/')

    #request.form = FORMULARIO HTML
    User.save(request.form)
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')