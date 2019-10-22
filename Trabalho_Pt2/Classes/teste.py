from peewee import *
import os

arq = './classes.DB'
DB = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = DB
   

class Disciplina(BaseModel):

    nome = CharField()
    nota = FloatField()
    aprovado = BooleanField()

class Curso(BaseModel):

    nome = CharField()


class Aluno (BaseModel):

    nome = CharField()
    #endereco = CharField()
    cursos = ManyToManyField(Curso)



class Matricula(BaseModel):

    aluno = ForeignKeyField(Aluno)
    disciplina = ForeignKeyField(Disciplina)
    numero = IntegerField()   #numero da matricula

class Usuario(BaseModel):
    nome = CharField()
    sobrenome = CharField()
    sexo = CharField()
    email = CharField()
    telefone = IntegerField()
    cidade = CharField()
    estado = CharField()

class Veiculo(BaseModel):
    marca = CharField()
    modelo = CharField()
    chassi = IntegerField()
    nmrPlaca = CharField()
    ano = IntegerField()

class Fornecedores(BaseModel):
    nome = CharField()

class Informacao(BaseModel):
    tipo = CharField()
    nome = CharField()
    conteudo = CharField()

class Diagnostico(BaseModel):
    infos = ManyToManyField(Informacao)
    estado = CharField()

class Problema(BaseModel):
    nome = CharField()
    possuiManutencao = BooleanField()

class Marca(BaseModel):
    nome = CharField()

class Mecanico(BaseModel):
    usuarios = ForeignKeyField(Usuario)
    preco = FloatField()





if __name__ == "__main__":  # se estiver rodando esse programa, executa!  (evita rodar no import)


    if os.path.exists(arq):
        os.remove(arq)
   
    try:
        DB.connect()
        DB.create_tables([Aluno,Disciplina,Matricula,Aluno.cursos.get_through_model(),Curso, Usuario, Veiculo, Fornecedores, 
        Informacao, Diagnostico, Problema, Marca, Mecanico])
    except OperationalError as e:
        print('erro ao criar tabela:' +str(e))


    marco = Aluno.create(nome= 'Marco Priotto ')
    marcao = Aluno.create(nome = 'Marcao Prioto')
    mecanica = Curso.create(nome = 'Mecanica')
    eletronica = Curso.create(nome= 'Eletronica')
    eletronica.alunos.add(marcao)

    fornecedor = Fornecedores.create(nome = 'Marco Peças')
    informacao = Informacao.create(tipo = 'Perigosa', nome = 'Situacao Carburador', conteudo = 'Biela')
    diagnostico = Diagnostico.create(estado = 'Com Falhas')
    informacao2 = Informacao.create(tipo = 'Perigosa', nome = 'Motor', conteudo = 'Problemas de Ignição')
    problemas = Problema.create(nome = 'Suspensão', possuiManutencao = 'FALSE')
    marca = Marca.create(nome = 'Audi')
    


    marco = Usuario.create(nome = 'Marco', sobrenome = 'Prioto', sexo = 'masculino',
        email = 'm@gmail.com', telefone = '2439', cidade = 'Pirai', estado = 'PR')


    for a in Aluno.select():
        print(a.nome)
        for c in a.cursos:
            print(c.nome)

    print('USUARIO:')
    for u in Usuario.select():
        print(u.nome)
        print(u.sobrenome)
        print(u.sexo)
        print(u.email)
        print(u.telefone)
        print(u.cidade)     
        print(u.estado)

    veiculo = Veiculo.create(marca = 'Audi', modelo = 'A3', chassi = '3244', nmrPlaca = '2984ZZ', ano = '2014')

    print('VEICULO: ')
    for v in Veiculo.select():
        print(v.marca)
        print(v.modelo)
        print(v.chassi)
        print(v.nmrPlaca)
        print(v.ano)

    print('FORNECEDORES:')
    for f in Fornecedores.select():
        print(f.nome)
    
    print('INFORMACOES:')
    for i in Informacao.select():
        print(i.tipo)
        print(i.nome)
        print(i.conteudo)

    print('DIAGNOSTICOS:')
    for d in Diagnostico.select():
        print(d.estado)
    
    print('PROBLEMAS:')
    for p in Problema.select():
        print(p.nome)
        print(p.possuiManutencao)
    
    print('MARCA:')
    for m in Marca.select():
        print(m.nome)

