
from peewee import *
import os

arq = './pessoas.db'
DB = SqliteDatabase(arq)


class BaseModel(Model):
    class Meta:
            database = DB

class Usuario(BaseModel):
    nome = CharField()
    sobrenome = CharField()
    sexo = CharField()
    email = CharField()
    telefone = IntegerField()
    cidade = CharField()
    estado = CharField()

class Pecas(BaseModel):
    nome = CharField()
    preco = FloatField()
    disponibilidade = BooleanField()

class Engenheiros(BaseModel):
    engenheiro = ForeignKeyField(Usuario)
    nmrCrea = IntegerField()

class Mecanicos(BaseModel):
    mecanico = ForeignKeyField(Usuario)
    preco = FloatField()
   
class Problemas(BaseModel):
    nome = CharField()
    possuiManutencao = BooleanField()

class Marca(BaseModel):
    nome = CharField()

class Informacoes(BaseModel):
    tipo = CharField()
    nome = CharField()
    conteudo = CharField()

class Diagnosticos(BaseModel):
    diagnostico = ManyToManyField(Informacoes)
    estado = CharField()

class Veiculo(BaseModel):
    marca = CharField()
    modelo = CharField()
    chassi = IntegerField()
    nome = CharField()
    nmrPlaca = IntegerField()
    ano = IntegerField()

class Fornecedores(BaseModel):
    nome = CharField()



if __name__ == "__main__":  # se estiver rodando esse programa, executa!  (evita rodar no import)


    if os.path.exists(arq):
        os.remove(arq)
   
    try:
        DB.connect()
        DB.create_tables([Usuario, Veiculo, Diagnosticos, Informacoes, Marca, Problemas, Mecanicos, Engenheiros, 
        Engenheiros.engenheiro.get_through_model(),Mecanicos.mecanico.get_through_model(), Pecas, Fornecedores])
    except OperationalError as e:
        print('erro ao criar tabela:' +str(e))


    marco = Usuario.create(nome = 'Marco', sobrenome = 'Prioto', sexo = 'masculino',
        email = 'm@gmail.com', telefone = '2439', cidade = 'Pirai', estado = 'PR')
    '''joao = Usuario.create(nome = 'Joao', sobrenome = 'Prioto',
        email = 'joao@gmail.com', telefone = '2329', cidade = 'Buri', estado = 'SP')
    caio = Usuario.create(nome = 'Caio', sobrenome = 'Prioto',
        email = 'c@gmail.com', telefone = '2139', cidade = 'Bahia', estado = 'PR')
    marcia = Usuario.create(nome = 'Marcia', sobrenome = 'Prioto',
        email = 'm@gmail.com', telefone = '2111', cidade = 'Pirai', estado = 'PR')
    renato = Usuario.create(nome = 'Renato', sobrenome = 'Prioto',
        email = 'r@gmail.com', telefone = '2454', cidade = 'Buri', estado = 'SP')
    jose = Usuario.create(nome = 'Jose', sobrenome = 'Prioto',
        email = 'j@gmail.com', telefone = '2239', cidade = 'Pirai', estado = 'PR')'''
    


    for u in Usuario.select():
        print(u.nome)
        print(u.sobrenome)
        print(u.sexo)
        print(u.email)
        print(u.telefone)
        print(u.cidade)
        print(u.estado)


    veiculo = Veiculo.create(marca = 'Audi', modelo = 'A3', chassi = '3244',
        nome = 'Marco', nmrPlaca = '2984ZZ', ano = '2014')
   


    for v in Veiculo.select():
        print(v.marca)
        print(v.modelo)
        print(v.chassi)
        print(v.nome)
        print(v.nmrPlaca)
        print(v.ano)
        