from flask import Flask, json, jsonify
from flask import request
from modelo import Pessoa
from modelo import Rio
from playhouse.shortcuts import model_to_dict


app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    return "<a href=/listar_pessoas>API listar pessoas</a>"

@app.route('/listar_pessoas')
def listar():
    # converte para pessoa para inserir em uma lista json

    rios = list(map(model_to_dict, Rio.select()))
    # adiciona à lista json um nome
    response = jsonify({"rio": rios})

    # informa que outras origens podem acessar os dados desse servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

# curl -d '{"nome":"joao"}' -X POST http://localhost:4999/incluir_pessoa
@app.route('/incluir_pessoa', methods=['post'])
def incluir_pessoa():
    # prepara a resposta padrão otimista
    response = jsonify({"message": "ok","details":"ok"})
    try:
        # pega os dados informados
        dados = request.get_json(force=True)

        Rio.create(cd_estacao = dados['estacao'], ds_cidade = dados['cidade'], data = dados['data'], 
        vlr_nivel = dados['nivel'], vlr_precipitacao = dados['precipitacao'], ds_ativo_nivel = dados['nivel1'], 
        ds_ativo_chuva = dados['chuva'], status = ['status'])
            
    except Exception as e:
        # resposta de erro
        response = jsonify({"message": "error","details":str(e)})
        
    # informa que outras origens podem acessar os dados desde servidor/serviço
    response.headers.add('Access-Control-Allow-Origin', '*')
    # retorno!
    return response

app.run(debug=True, port=4999)