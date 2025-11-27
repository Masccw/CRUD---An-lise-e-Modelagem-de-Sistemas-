# Importa CRUD origin
from utils.crud import Adicionar,Listar, atualizar, remover

#Programa rodando
while True: 
    print("\n1 - Adicionar Paciente\n2 - Listar Pacientes\n3 - Atualizar paciente\n4 - Remover\n5 - Sair")       
    o = input(": ")
    if o == "1":
        Adicionar()
    elif o == "2":
        Listar()
    elif o == "3":
        atualizar()
    elif o =="4":
        remover()
    elif o == "5":break