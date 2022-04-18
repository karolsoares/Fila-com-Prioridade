
##from pygame import KSCAN_SCROLLOCK
#from maxheap import MaxHeap

#fila = MaxHeap()

from multiprocessing.sharedctypes import Value


class Paciente:

    def put(item):
        pacientes = []
        pacientes.insert(0, item)
        print(pacientes)
        return pacientes
        #for i in range(len(pacientes)):
         #   pacientes.insert(1, item)
          #  print(pacientes)

    def interacao(nome, dt_nasciento, tipo_sanguineo):
        item= (nome, dt_nasciento, tipo_sanguineo)

        Paciente.put(item)
        
### TESTE ### 

p= Paciente
nome= input("Digite seu nome completo:\n")
dt_nasciento= input("Digite sua data de nascimento (dd/mm/aa):\n")
tipo_sanguineo= input("Digite seu tipo sanguineo:\n")

p.interacao(nome, dt_nasciento, tipo_sanguineo)

nome= input("Digite seu nome completo:\n")
dt_nasciento= input("Digite sua data de nascimento (dd/mm/aa):\n")
tipo_sanguineo= input("Digite seu tipo sanguineo:\n")

p.interacao(nome, dt_nasciento, tipo_sanguineo)

#lista=["banana", "abacaxi", "amora"]
#lista.append("amor")
#lista.append("paciencia")
#print(lista)
#lista.insert(3, 'capacidade')
#print(lista)

