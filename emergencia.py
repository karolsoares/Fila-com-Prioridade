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
from maxheap import MaxHeap
import pickle

fila = MaxHeap()

class Paciente:

    def ordem():
        ordem = [999] # criaria a ordem
        ordem= ordem[0] - 1 # e faria esse valor sempre ir diminuindo
        ordem.append(ordem) # iria adicionando na lista o valor dos numeors da ordem conorme fosse decrescendo 

        return ordem

    ''' 
    def interação():
        print("Digite seu nome:")
        nome= input()
        print("Digite seu tipo sanguineo:")
        tipo_sanguineo= input()
        print("Digite sua data de nascimento:")
        dt_nascimento= input()

        return 
        '''

    def adicionar_dados(nome, tipo_sanguineo, dt_nascimento):
        lista=[]
        arquivo= open('dados', 'w')
        if len(lista) == 0:
            lista.append((nome, tipo_sanguineo, dt_nascimento)) 

            indice = len((lista)) + 1 #teoricamnete seria um contador
            
            
            print(indice) #so pra ver se tava contando certo
            
            return lista 
        elif len(lista) == 1:
            lista.append((nome, tipo_sanguineo, dt_nascimento))

            indice = indice + 1
        
            return lista

        arquivo.close()
     
p = Paciente
while True:   
    print("Digite seu nome:")
    nome= input()
    print("Digite seu tipo sanguineo:")
    tipo_sanguineo= input()
    print("Digite sua data de nascimento:")
    dt_nascimento= input()

    print(p.adicionar_dados(nome, tipo_sanguineo, dt_nascimento))









 
