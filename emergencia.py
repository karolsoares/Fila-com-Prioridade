'''
CENÁRIO:
- Organizar a ordem de chegada e prioridade dos pacientes a serem atendidos em uma emergência de um hospital.


Usar a classe MaxHeap desenvolvida em aula.
	Disponível no tópico 'Fila com Prioridades (heap)' no AVA.


TAREFAS:
Cada item dentro da fila deverá ser representado por uma tupla com o padrão:
(prioridade [int], ordem [int], paciente [classe Paciente])

- Prioridade: (MAIS URGENTE: 10 | MENOS URGENTE: 1)
- Ordem: Quem chegou primeiro terá um valor maior
- Paciente: objeto da classe Paciente que deverá guardar nome completo, tipo sanguíneo e data de nascimento.

* Por padrão, a linguagem Python ao comparar tupla, caso haja empate entre o primeiro parâmetro, o segundo é usado para desempate. *

Paciente:
	nome_completo
	tipo_sanguineo
	data_nascimento

IMPORTANTE: 
•	Manter os pacientes chamados (removidos da fila) em uma lista auxiliar
•	Usar um contador que inicie no valor 999 e decremente a cada novo paciente adicionado

   Deve ter interação com o usuário e as opções em um Menu:
1)	Adicionar novo paciente
2)	Chamar próximo paciente
3)	Mostrar próximo paciente (sem chamar)
4)	Listar os 5 últimos chamados

'''
import pickle
from maxheap import MaxHeap

fila = MaxHeap()

class Paciente:
    
    def ordem():
        ordem = [999] # criaria a ordem
        ordem= ordem[0] - 1 # e faria esse valor sempre ir diminuindo
        ordem.append(ordem) # iria adicionando na lista o valor dos numeors da ordem conorme fosse decrescendo 

        return ordem
    
    def interação():
        while True:
            nome= input("Digite seu nome:")
            tipo_sanguineo= input("Digite seu tipo sanguineo:")
            dt_nascimento= input("Digite sua data de nascimento:")

            adicionar= (nome, tipo_sanguineo, dt_nascimento) 

            Paciente.adicionar_dados(adicionar)
    
    def adicionar_dados(item):
        lista = [0]
        for lista in range(1, 1000): #não sei ageitar isso
            lista.append(item) 
            
        print(lista) 
 
p = Paciente 

p.interação()

    









 
