# Criacao de lista com 1 elemento senao ela nao existe
lista = ["edson"]

# Funcao Adicionar
def Adicionar():
    if lista:
        nome = input("Nome: ")
        lista.append(nome)
    else:
        print("Lista nao existe!")

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

if __name__ == "__main__":
    while True:
        Adicionar()
        sair = input("")
        if sair == "":break
    
    Listar()