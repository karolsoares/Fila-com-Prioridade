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

fila = MaxHeap()

class Paciente:

    def dados_paciente(nome,tipoSanguineo, nascimento):
        numero= [999]   # como naõ sobreescrever valores
        
        numero[0] - 1
        numero.append(numero)

        dicPaciente= {
            "nome": (nome, str(numero)),
            "tipoSanguineo": tipoSanguineo,
            "nascimento": nascimento      
        } 

       

        lista= []
        len(lista) + 1
        lista.append(dicPaciente["nome"])

        print(lista)
        return dicPaciente

        
        
    print(dados_paciente("Gabriela", "AB", "17/11/2001" ))
    print(dados_paciente("Joao", "AB", "19/11/2001" ))



 
