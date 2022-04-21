from ctypes.wintypes import PULARGE_INTEGER
from maxheap import MaxHeap
from paciente import Paciente

h = MaxHeap()
p = Paciente

lista = []
ordem = []
f = []

def interacao():
    print( "----- Bem-Vindo a Emergência do Hospital -----\n")
    print("Para cadastrar sua ficha por favor insira os dados a baixo\n")

    ### DADOS
    nome= input("Digite seu nome completo:\n")
    dt_nasciento= input("Digite sua data de nascimento (dd/mm/aa):\n") # falta organizar para ser colocado dias validos
    tipo_sanguineo= input("Digite seu tipo sanguineo:\n")
    p.uniao(nome, dt_nasciento, tipo_sanguineo)
    pula_linha()
    ### PRIORIDADE
    prioridade()
    pula_linha()
    iniciar_chamada()

def prioridade():        
        while True:
            print("Escolha uma das alternativas para especificar o seu problema:\n ")
            print("a) Acidente de transito") 
            print("b) Infarto") 
            print("c) Alergias graves") 
            print("d) queimaduras de segundo e terceiro grau") 
            print("e) Outros")
            escolha = input("Escolha uma das alternativas:")

            menos_urgente= 1
            mais_urgente= 10 #acidente de transito, infarto, alergia grave, queimaduras de segundo grau

            if escolha == "a":
                lista_de_chamada(mais_urgente)
                break
            if escolha == "b":
                lista_de_chamada(mais_urgente)
                break
            if escolha == "c":
                lista_de_chamada(mais_urgente)
                break
            if escolha == "d":
                lista_de_chamada(mais_urgente)
                break
            elif escolha == "e":
                lista_de_chamada(menos_urgente)
                break
            else:
                print("Esta opção não esta disponivel\n")
                continue

def emergencia(): #casos graves
    ordenacao = 999 - len(ordem) #o len de ordem vai aumentando conforme vamos insrindo valor, sempre pegamos o primeiro valor que vai ser menor
    ordem.insert(0, ordenacao)
    return ordenacao

def urgencia(): #casos leves
    contagem = 700 - len(f)
    f.insert(0, contagem)

def insercao(a, b, c): #insere na kista de chamada
    inserir= (int(a), int(b), c)   
    lista.append(inserir)
    h.put(inserir) 
    print(lista)

def lista_de_chamada(c): 
    if c == 1:
        urgencia()
        insercao(c, f[0], p.pacientes[0])
    if c == 10:
        emergencia()
        insercao(c, ordem[0], p.pacientes[0])

def pula_linha():
    print("\n")

def iniciar_chamada():
    print("Chamar próximo da chamada:")
    print("Se a opcao for não, voltara para o menu inicial")

    resposta = input("Sim(1)\nNão(2)\n")
    if resposta == "1":
        chamada()
    elif resposta == "2":
        interacao()
    else: 
        print("Esta opção não está disponível")
        iniciar_chamada()

def chamada(): 
        print(h.get()) # chama o pessoal da lista
        pula_linha()
        iniciar_chamada() # para caso queira chamar o proximo da lista

### TESTE ###
while True:
    interacao()
    

