from flask import Flask, render_template, request, redirect, session
from usuario import Usuario
app = Flask(__name__)
app.config['SECRET_KEY'] = '43r78934yt6y5907'

        
usuarios = [
    Usuario("João", "Santos", "masculino","J@hotmail.com","32423","Buri","SP"),
    Usuario("Joana", "Cardoso", "feminino","Ja@hotmail.com","32413","Buri","SP"),
    Usuario("Ana", "Bert", "feminino","a@hotmail.com","31423","Buri","SP"),
    Usuario("Flavia", "Bert", "feminino","f@gmail.com","31423","Buri","SP"),
    Usuario("Toni", "Santos", "masculino","t@hotmail.com","32423","Itu","SP"),
    Usuario("André", "Rui", "masculino","aa@hotmail.com","32411","São Paulo","SP"),
    Usuario("Thiago", "Ribeiro", "masculino","tr@outlook.com","32411","Buri","SP"),
    Usuario("Marco", "Priotto", "masculino","marco_prioto@hotmail.com","32423","Pirai do Sul","PR")
    ]
        

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Cliente')
def Cliente():
    return render_template('Cliente.html', lista = usuarios)
@app.route('/Veiculos')
def Veiculos():
    return render_template('Veiculos.html')
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

@app.route("/incluirUsuario", methods = ['post', 'get'])
def incluir():
    nome= request.form["nome"]
    snome= request.form["snome"]
    sexo= request.args.get("sexo")
    email= request.form["email"]
    tel= request.form["telefone"]
    cidade= request.form["cidade"]
    estado= request.form["estado"]
    nova = Usuario(nome,snome,sexo,email,tel,cidade,estado)
    usuarios.append(nova)

    return redirect("/Cliente")

@app.route("/excluir_usuario")
def excluir_usuario():
    excluir = None
   
    nome = request.args.get("nome")
    
    for usuario in usuarios:
        #
        if nome == usuario.nome:
           
            excluir = usuario
            break

    
    if excluir != None: 
        usuarios.remove(excluir)
    
   
    return Cliente()

@app.route("/Alt_cliente")
def Alt_cliente():
   
    nome = request.args.get("nome")
    
    for usuario in usuarios:
      
        if nome == usuario.nome:
           
            return render_template("Alt_cliente.html", usuario=usuario)
    
    return Cliente()

@app.route("/alterar_usuario")
def alterar_usuario():
    nome= request.args.get("nome")
    snome= request.args.get("snome")
    sexo= request.args.get("sexo")
    email= request.args.get("email")
    tel= request.args.get("telefone")
    cidade= request.args.get("cidade")
    estado= request.args.get("estado")
    nome_original = request.args.get("nome_original")
    indice = -1
    for i in range(len(usuarios)):
        if usuarios[i].nome == nome_original:
            indice = i
            break
    if indice >= 0:
        usuarios[indice] = Usuario(nome,snome,sexo,email,tel,cidade,estado)
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


app.run(debug=True, port=4001)


