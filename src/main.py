# Criacao de lista com 1 elemento senao ela nao existe
lista = []

# Funcao Adicionar
def Adicionar():
        nome = input("Nome: ")
        lista.append(nome)

# Funcao Listar
def  Listar():
    if lista:
        for i, nome in enumerate(lista):
            print(f"[{i} - {nome}]") 
    else:
        print("Lista nao existe!")


#Rodar o programa
while True:
    Adicionar()
    sair = input("")
    if sair == "":break
    
Listar()