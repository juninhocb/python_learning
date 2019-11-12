from flask import Flask, render_template, request, redirect, session
from usuario import Usuario
from veiculo import Veiculo
from peewee import *
import os
import requests
from playhouse.shortcuts import dict_to_model

app = Flask(__name__)
app.config['SECRET_KEY'] = '43r78934yt6y5907'


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Cliente')
def Cliente():
    dados_usuarios = requests.get('http://localhost:4001/Cliente')
    json_usuarios = dados_usuarios.json()
    usuarios = []
    
    for usuario_json in json_usuarios:
        u = dict_to_model(Usuario, usuario_json)
        usuarios.append(u)
    return render_template('Cliente.html', lista = usuarios)
@app.route('/Veiculos')
def Veiculos():
    dados_veiculos = requests.get('http://localhost:4001/Veiculos')
    json_veiculos = dados_veiculos.json()
    veiculos = []
    
    for veiculos_json in json_veiculos:
        v = dict_to_model(Veiculo, veiculos_json)
        veiculos.append(v)
    
    return render_template('Veiculos.html', lista = veiculos)
@app.route('/Diagnosticos')
def Diagnostico():
    return render_template('Diagnosticos.html')
@app.route('/Contato')
def Contato():
    return render_template('Contato.html')
@app.route('/Login')
def Login():
    return render_template('Login.html')
@app.route('/Cad_Cliente')
def Cad_cliente():
    return render_template('Cad_Cliente.html')
@app.route('/Cad_Veiculo')
def Cad_Veiculo():
    return render_template('Cad_Veiculo.html')

@app.route("/incluirUsuario", methods = ['post'])
def incluir():
    nome= request.form["nome"]
    snome= request.form["snome"]
    sexo= request.form["sexo"]
    email= request.form["email"]
    
    tel= request.form["telefone"]
    cidade= request.form["cidade"]
    estado= request.form["estado"]
    Usuario.create(nome = nome, sobrenome = snome, sexo = sexo, email = email, telefone = tel, cidade= cidade
    , estado = estado)

    return redirect("/Cliente")

@app.route("/incluirVeiculo", methods = ['post'])
def incluirV():
    marca= request.form["marca"]
    modelo= request.form["modelo"]
    chassi= request.form["sexo"]
    nome= request.form["nome"] 
    nmrPlaca= request.form["nmrPlaca"]
    ano= request.form["ano"]
    Veiculo.create(marca = marca, modelo = modelo, chassi = chassi, nome = nome, nmrPlaca = nmrPlaca, ano = ano)
    

    return redirect("/Veiculos")

@app.route("/excluir_usuario")
def excluir_usuario():
   
    id = request.args.get("id")

    Usuario.delete_by_id(id)
    
    return Cliente()

@app.route("/Alt_cliente")
def Alt_cliente():
   
    id = request.args.get("id")
    
    usuario_alt = Usuario.get_by_id(id)
           
    return render_template("Alt_cliente.html", usuario=usuario_alt)
 

@app.route("/alterar_usuario")
def alterar_usuario():
    id = request.args.get("id")
    nome= request.args.get("nome")
    snome= request.args.get("snome")
    sexo= request.args.get("sexo")
    email= request.args.get("email")
    tel= request.args.get("telefone")
    cidade= request.args.get("cidade")
    estado= request.args.get("estado")
    usuario = Usuario.get_by_id(id)
    
    usuario.nome = nome
    usuario.sobrenome = snome
    usuario.sexo = sexo
    usuario.email = email
    usuario.telefone = tel
    usuario.cidade = cidade
    usuario.estado = estado
    

    usuario.save()

    return redirect("Cliente")

@app.route("/login", methods=['POST'])
def login():
    login = request.form["login"]
    senha = request.form["senha"]
    if login == 'admin' and senha == '123':
        session['usuario'] = login
        return redirect("/")
    else:
        return render_template('Login.html')

@app.route("/logout")
def logout(): 
    session.pop("usuario")
    return redirect("/")


app.run(debug=True, port=5000)


