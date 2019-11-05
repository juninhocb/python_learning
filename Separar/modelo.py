from peewee import *
import os

arq = '/tmp/pessoas-backend.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Pessoa(BaseModel):
    nome = CharField()
    endereco = CharField()
    telefone = CharField()
    email = CharField()

class Rio(BaseModel): 
    nivel = FloatField()

    
if __name__ == "__main__":
    # apagar o arquivo caso ele exista
    if os.path.exists(arq):
        os.remove(arq)

    db.connect() # conecta-se ao banco de dados
    db.create_tables([Pessoa,Rio]) # cria a tabela de pessoas
    marco = Pessoa.create(nome="Marco Priotto", 
        endereco="Casa 1", telefone="334", email="marco@gmail.com")
    marquinho = Pessoa.create(nome = "Marquinho Priotto", 
        endereco = "Ap 2, S/N", telefone="32443", email= "marq@hotmail.com")
    print(marco.nome, ",", marco.endereco, ",", marco.telefone, ",", marco.email) 
    print(marquinho.nome, ",", marquinho.endereco, ",", marquinho.telefone, ",", marco.email)