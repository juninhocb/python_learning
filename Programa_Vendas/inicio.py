## New Program TEST

from modelo import Cliente

lista_clientes =[]
lista_casa =[
            Cliente(1,"Jeff", 0, "Casa"),
            Cliente(2, "Bia", 0, "Casa")
            ]
lista_amigos = [
            Cliente(3, "Marco", "0", "Amigo"),
            Cliente(4, "Bruno", "0", "Amigo")
            ]

#lista_amigos.sort()

while(1):
    x = int(input('Please, Input a number: '))
    if x == 1:
            who = int(input('quem pegou o fuckin espeto: '))
            qtd = int(input('quantos espetos o ser pegou?'))
            for i in lista_casa:
                if i.id == who:
                    i.divida += 1*qtd
                    break
            else:
                print('Numero inválido =(')
                   
    elif x ==2:
        print('Cala')
    elif x ==3:
        print("Tipo","ID","Nome","Divida")
        for i in lista_casa:
            print(i.tipo + "|"+str(i.id) + "|" +i.nome + "| " +"R$" +""+ str(i.divida) + ",00")
        for j in lista_amigos:
            print(j.tipo + "|"+str(j.id) + "|" +j.nome + "| " +"R$" +""+ str(j.divida) + ",00")
        for k in lista_clientes:
            print(k.tipo + "|"+str(k.id) + "|" +k.nome + "| " +"R$" +""+ str(k.divida) + ",00")    
            
    elif x ==4:
        id = len(lista_clientes) + len(lista_amigos) + len(lista_casa) + 1
        nome = input('Digite o nome do Cliente: ' )
        divida = 0
        tipo = "Cliente"
        new = Cliente(id,nome,divida,tipo)
        lista_clientes.append(new)
                    
                    
