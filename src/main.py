# Biblioteca para marca o dia e hora
from datetime import datetime as dt

class Paciente():
    def __init__(self, nome, cpf, datNasc, endereco, dia):
        self.nome = nome
        self.cpf = cpf
        self.datNasc = datNasc
        self.endereco = endereco
        self.dia = dia

    def __str__(self):
        return f"\nNome: {self.nome}\nCPF: {self.cpf}\nData de nascimento: {self.datNasc}\nEndereco: {self.endereco}\nInternado: {self.dia}\n"

# Lista de Pacientes
Lista = []


#Funcoes Adicionar // CREATE
def Adicionar():

    nomeUsuario = input("Digite o nome: ").title()
    cpf = int(input("Digite o cpf: "))
    dataNasc = input("Digite o dataNasc: ")
    endereco = input("Digite o Endereco: ")

    #Dia da atual da internacao
    dia = dt.now().date()

    #Objeto
    p1 = Paciente(nomeUsuario, cpf, dataNasc, endereco, dia)
    Lista.append(p1)


#Listagem de pacientes // READ
def Listar():
    for i, paciente in enumerate(Lista):
        print(f"\n[{i}] | {paciente}\n")



#Programa rodando
while True: 
    print("\n1 - Adicionar Paciente\n2 - Listar Pacientes\n3 - Sair")       
    o = input(": ")
    if o == "1":
        Adicionar()
    elif o == "2":
        Listar()
    elif o == "3":break