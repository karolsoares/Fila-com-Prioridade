class Paciente:
    pacientes = []
    
    def put(item): #def que insere a tupla na lista
        Paciente.pacientes.insert(0, item)
        print(Paciente.pacientes)

    def interacao(nome, dt_nasciento, tipo_sanguineo): #def que cria a tupla
        item= (nome, dt_nasciento, tipo_sanguineo)

        Paciente.put(item)