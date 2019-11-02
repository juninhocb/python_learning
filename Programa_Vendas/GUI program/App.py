#bibliotecas
from tkinter import ttk
from tkinter import *
from modelo import Cliente

def out():
        root.destroy()

def callback():    
        print ("chamada de retorno")
    
    


###########################LISTAS#####################################

lista_clientes =[]
lista_casa =[
            Cliente(1,"Jeff", 0, "Casa"),
            Cliente(2, "Bia", 0, "Casa"),
            Cliente(3, "Ze", 0, "Casa")
            
            ]
lista_amigos = [
            Cliente(4, "Marco", "0", "Amigo"),
            Cliente(5, "Bruno", "0", "Amigo")
            ]

#######################################################################


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        
###########################CRIAÇÂO DE CONTAINERS##########################

        self.container0 = Frame(master)
        self.container0.pack()
        self.container1 = Frame()
        self.container1.pack()
        self.container2 = Frame()
        self.container2.pack()
        self.container3 = Frame()
        self.container3.pack()
        self.container4 = Frame()
        self.container4.pack()
        

############################MENU##################################
        
        
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Arquivo",menu=filemenu)
        menu.add_cascade(label="Rede Tonon",menu=None, command = self.vendaCasa)
        #menu.add_cascade(label="Ver o Marco",menu=None, command=self.verMarco)
        menu.add_cascade(label="Ajuda",menu=None)
        filemenu.add_command(label="Novo CTRL + N", command = callback)
        filemenu.add_command(label="Abrir CTRL + X")
        filemenu.add_command(label="Sair ALT + F4", command = out)



###################################################

        
        self.titulo = Label(self.container0, text="Programa Marco Priotto")
        self.titulo["font"] = ("Verdana", "15", "bold")
        self.titulo.pack()
  
        self.opcao = Label(self.container1, text="Escolha uma opção:")
        self.opcao["font"] = ("Calibri", "9")
        self.opcao.pack ()
        
        
        self.btnVenda = Button(self.container2, command=self.tipoVenda,text="Venda", 
        font=self.fonte, width=10)
        self.btnVenda.pack(side=LEFT)
        
        self.btnAlterar = Button(self.container2, command=self.tipoVenda,text="Alterar", 
        font=self.fonte, width=10)
        self.btnAlterar.pack(side=LEFT)
        
        self.Cadastrar = Button(self.container2, command=self.cadastrar,text="Cadastrar", 
        font=self.fonte, width=10)
        self.Cadastrar.pack(side=LEFT)
        
        self.Relatorio = Button(self.container2, command=self.relatorio,text="Relatório", 
        font=self.fonte, width=10)
        self.Relatorio.pack(side=RIGHT)
        
    
    def tipoVenda(self, master=None):
        self.opcao.pack_forget()
        self.btnVenda.pack_forget()
        self.btnAlterar.pack_forget()
        self.Relatorio.pack_forget()
        self.Cadastrar.pack_forget()
        
        self.text = Label(self.container1, text="Informe o tipo do Cliente")
        self.text.pack(side=TOP)
        
        self.combo0 = ttk.Combobox(self.container1, values=['Casa', 'Amigo', 'Cliente'])
        self.combo0.pack()
        
        self.escolher = Button(self.container2, command=self.tratar)
        self.escolher["text"] = "OK"
        self.escolher["font"] = ("Calibri", "8")
        self.escolher.pack()
        
        self.voltar1 = Button(self.container3, command=self.voltarInicio2)
        self.voltar1["text"] = "Voltar"
        self.voltar1["font"] = ("Calibri", "8")
        self.voltar1.pack() 
        
        
              
    def tratar(self):
        texto=self.combo0.get()
        
        if texto == 'Casa':
            self.escolher["command"] = self.vendaCasa
        
        elif texto == 'Amigo':
            self.escolher["command"] = self.vendaAmigo
            
            
        elif texto == 'Cliente':
            self.escolher["command"] = self.vendaCliente
        
        
    def vendaCasa(self, master = None):
        self.text.pack_forget()
        self.combo0.pack_forget()
        self.escolher.pack_forget()
        self.voltar1.pack_forget() 
            
        self.nomeLabel = Label(self.container1, text="Quem Comprou?", font=self.fonte)
        self.nomeLabel.pack(side=LEFT)
            
        self.nomeLabel1 = Label(self.container2, text="Quantos Comprou?", font=self.fonte)
        self.nomeLabel1.pack(side=LEFT)
        
        self.who = Label(self.container1)
        self.who.pack()
        self.who = ttk.Combobox(self.container1)
        self.who["values"] = 'Jeff', 'Bia', 'Ze'
        self.who["width"] = 30
        self.who["font"] = self.fonte
        self.who.pack()
            
        self.qtd = Entry(self.container2)
        self.qtd["width"] = 5
        self.qtd["font"] = self.fonte
        self.qtd.pack(side=LEFT)
        
        self.var1 = IntVar()
        self.check = Checkbutton(self.container3, text="pago", variable=self.var1)
        self.check.pack()
            
        self.concluir = Button(self.container4, command=self.concluiVenda)
        self.concluir["text"] = "Concluir Venda"
        self.concluir["font"] = ("Calibri", "8")
        self.concluir.pack()
        
        self.mensagem = Label(self.container4, text="", font=self.fonte)
        self.mensagem.pack()
        
                
            
            
    def concluiVenda(self):
        texto=self.who.get()
        if texto == 'Jeff':
            who = 1
            
        elif texto == 'Bia':
            who = 2
            
        elif texto == 'Ze':
            who = 3
        
        if self.var1.get() == 1:
            print('Já Pagou')
        else:
            print('Não pagou')
            
                    
        qtd = int(self.qtd.get())
        for i in lista_casa: 
            if i.id == who:
                i.divida += 1*qtd
                self.mensagem["text"] = "Dados atualizados!"
                break
            else:
                self.mensagem["text"] = "Nome inexsistente"
        
        
        self.voltar = Button(self.container4, command=self.voltarInicio)
        self.voltar["text"] = "Voltar"
        self.voltar["font"] = ("Calibri", "8")
        self.voltar.pack()       

    def voltarInicio(self):
        self.mensagem.pack_forget()
        self.escolher.pack_forget()
        self.voltar.pack_forget()
        self.who.pack_forget()
        self.concluir.pack_forget()
        self.qtd.pack_forget()
        self.nomeLabel.pack_forget()
        self.nomeLabel1.pack_forget()
        self.check.pack_forget()
        
        self.titulo.pack()
        self.opcao.pack ()
        self.btnVenda.pack(side=LEFT)
        self.btnAlterar.pack(side=LEFT)
        self.Cadastrar.pack(side=LEFT)
        self.Relatorio.pack(side=RIGHT)
        
    def voltarInicio2(self):
        self.escolher.pack_forget()
        self.voltar1.pack_forget()
        self.combo0.pack_forget()
        self.text.pack_forget()
        
        self.titulo.pack()
        self.opcao.pack ()
        self.btnVenda.pack(side=LEFT)
        self.btnAlterar.pack(side=LEFT)
        self.Cadastrar.pack(side=LEFT)
        self.Relatorio.pack(side=RIGHT)
    
    def voltarInicio3(self):
        self.nomeLabel.pack_forget()
        self.voltar2.pack_forget()
        self.Cadastrar.pack_forget()
        self.nome.pack_forget()
        self.concluir.pack_forget()
        self.mensagem.pack_forget()
        
        self.titulo.pack()
        self.opcao.pack ()
        self.btnVenda.pack(side=LEFT)
        self.btnAlterar.pack(side=LEFT)
        self.Cadastrar.pack(side=LEFT)
        self.Relatorio.pack(side=RIGHT)
    
    def voltarInicio4(self):
        self.nomeLabel.pack_forget()
        self.voltar2.pack_forget()
        self.Cadastrar.pack_forget()
        self.nome.pack_forget()
        self.concluir.pack_forget()
        self.voltar3.pack_forget()
        self.mensagem.pack_forget()
        
        self.titulo.pack()
        self.opcao.pack ()
        self.btnVenda.pack(side=LEFT)
        self.btnAlterar.pack(side=LEFT)
        self.Cadastrar.pack(side=LEFT)
        self.Relatorio.pack(side=RIGHT)
    
    def voltarInicio5(self):
         
        self.voltar4.pack_forget()
        
        self.titulo.pack()
        self.opcao.pack ()
        self.btnVenda.pack(side=LEFT)
        self.btnAlterar.pack(side=LEFT)
        self.Cadastrar.pack(side=LEFT)
        self.Relatorio.pack(side=RIGHT)
        
        
    def cadastrar(self):
        self.opcao.pack_forget()
        self.btnVenda.pack_forget()
        self.btnAlterar.pack_forget()
        self.Relatorio.pack_forget()
        self.Cadastrar.pack_forget()
        
        self.nomeLabel = Label(self.container1, text="Nome:", font=self.fonte)
        self.nomeLabel.pack(side=LEFT)
        
        self.nome = Entry(self.container1)
        self.nome["width"] = 30
        self.nome["font"] = self.fonte
        self.nome.pack()
        
        self.concluir = Button(self.container2, command= self.concluiCadastro)
        self.concluir["text"] = "Concluir"
        self.concluir["font"] = ("Calibri", "8")
        self.concluir.pack()
        
        self.voltar2 = Button(self.container3, command=self.voltarInicio3)
        self.voltar2["text"] = "Voltar"
        self.voltar2["font"] = ("Calibri", "8")
        self.voltar2.pack()
        
        self.mensagem = Label(self.container4, text="", font=self.fonte)
        self.mensagem.pack()
        
    def concluiCadastro(self):
        
        self.id = len(lista_clientes) + len(lista_amigos) + len(lista_casa) + 1
        self.nome1 = self.nome.get()
        self.divida = 0
        self.tipo = "Cliente"
        self.new = Cliente(self.id,self.nome1,self.divida,self.tipo)
        lista_clientes.append(self.new)
        self.mensagem["text"] = "Cliente Cadastrado!"
        
        self.voltar3 = Button(self.container4, command=self.voltarInicio4)
        self.voltar3["text"] = "Voltar"
        self.voltar3["font"] = ("Calibri", "8")
        self.voltar3.pack()
    
    def relatorio(self):
        
        self.opcao.pack_forget()
        self.btnVenda.pack_forget()
        self.btnAlterar.pack_forget()
        self.Relatorio.pack_forget()
        self.Cadastrar.pack_forget()
        
        self.mostrarTabela = Label(self.container1)
        print("Tipo","ID","Nome","Divida")
        for i in lista_casa:
            print(i.tipo + "|"+str(i.id) + "|" +i.nome + "| " +"R$" +""+ str(i.divida) + ",00")
        for j in lista_amigos:
            print(j.tipo + "|"+str(j.id) + "|" +j.nome + "| " +"R$" +""+ str(j.divida) + ",00")
        for k in lista_clientes:
            print(k.tipo + "|"+str(k.id) + "|" +k.nome + "| " +"R$" +""+ str(k.divida) + ",00")    
            
    
        
        self.voltar4 = Button(self.container4, command=self.voltarInicio5)
        self.voltar4["text"] = "Voltar"
        self.voltar4["font"] = ("Calibri", "8")
        self.voltar4.pack()
        
        
        
        
        
        
        
        
        
        
    #def verMarco(self):        
     #   print('OKAY')
    
            
        
        
        
        

root = Tk()
root.geometry('400x300')
root.title("Programinha")
Application(root)
root.mainloop()

