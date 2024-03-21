def definir_prioridade():
    print('Defina a prioridade da tarefa:')
    print('1 - Urgente || 2 - normal')

    prioridade = int(input())

    return prioridade

class Queue:
    def __init__(self):
        self.lista = []

    def is_empty(self, item):
        #se a fila nao tiver vazia
        if not self.fila:
            return True
        else:
            return False
        
    def adicionar(self, item):
    prioridade = definir_prioridade()

    self.lista.append([item, prioridade])

    
