from peewee import *
import os 

# http://docs.peewee-orm.com/en/latest/peewee/database.html#using-sqlite
# a leitura de dados será apenas em memória, 
# temporário, para renderizar os dados
arq = ':memory:'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()
#,"ds_ativo_nivel":true,"ds_ativo_chuva":true,"status":"normal"
class Rio(BaseModel):
    cd_estacao = IntegerField()
    ds_cidade = CharField()
    data = DateTimeField()
    vlr_nivel = CharField()
    vlr_precipitacao = CharField()
    ds_ativo_nivel = BooleanField()
    ds_ativo_chuva = BooleanField()
    status = CharField()
    

if __name__ == "__main__":
    db.connect()
    db.create_tables([Pessoa])
    joao = Pessoa.create(nome="Joao da Silva", 
        endereco="Casa 9", telefone="3541-1230", email="la@gmail.com")
    print(joao.nome, ",", joao.endereco, ",", joao.telefone, ",", joao.email)