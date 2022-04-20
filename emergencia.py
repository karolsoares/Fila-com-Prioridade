
from csv import list_dialects
from maxheap import MaxHeap
from paciente import Paciente

h = MaxHeap()
p = Paciente

lista = []
ordem = []

def prioridade():        
        while True:
            print("a) Acidente de transito") 
            print("b) Infarto") 
            print("c) Alergias graves") 
            print("d) queimaduras de segundo e terceiro grau") 
            print("e) Outros")
            escolha = input("Escolha uma das alternativas:")

            menos_urgente= 1
            mais_urgente= 10 #acidente de transito, infarto, alergia grave, queimaduras de segundo grau

            if escolha == "a":
                numero_chamada()
                insercao(mais_urgente, ordem[0], p.pacientes[0])
                break
            if escolha == "b":
                numero_chamada()
                insercao(mais_urgente,ordem[0], p.pacientes[0])
                break
            if escolha == "c":
                numero_chamada()
                insercao(mais_urgente,ordem[0], p.pacientes[0])
                break
            if escolha == "d":
                numero_chamada()
                insercao(mais_urgente,ordem[0], p.pacientes[0])
                break
            elif escolha == "e":
                numero_chamada()
                insercao(menos_urgente,ordem[0], p.pacientes[0])
                break
            else:
                print("Esta opção não esta disponivel\n")
                continue

def numero_chamada():
    ordenacao = 999 - len(ordem) #o len de ordem vai aumentando conforme vamos insrindo valor, sempre pegamos o primeiro valor que vai ser menor
    ordem.insert(0, ordenacao)
    return ordenacao

def insercao(a, b, c):
    inserir= (int(a), int(b), c)   
    print()
    lista.append(inserir) 
     
    '''
    if a == 10 and b == 999:
        
        print(lista)
    elif a == 10 and b == 998:
       lista.insert(0, inserir)
       print(lista)
    else:
        print("erro")
    '''
def pula_linha():
    print("\n")

#def chamada(c , d): # c = valor da prioridade d = valor da Ordem

### TESTE ###
while True:
    
    print( "----- Bem-Vindo a Emergência do Hospital -----\n")
    print("Para cadastrar sua ficha por favor insira os dados a baixo\n")

    ### DADOS
    nome= input("Digite seu nome completo:\n")
    dt_nasciento= input("Digite sua data de nascimento (dd/mm/aa):\n") # falta organizar para ser colocado dias validos
    tipo_sanguineo= input("Digite seu tipo sanguineo:\n")
    p.interacao(nome, dt_nasciento, tipo_sanguineo)
    pula_linha()

        ### PRIORIDADE
    print("Escolha uma das alternativas para especificar o seu problema:\n ")
    prioridade()
    pula_linha()
    
    #h.put(lista)
    #sprint(h.get())