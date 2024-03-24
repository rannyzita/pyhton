def definir_prioridade():
    print('Defina a prioridade da tarefa: ')
    print('1 - alta || 2 - Média || 3 - baixa')
    prioridade = int(input())

    return prioridade

def processar_tarefa(fila):
    fila_alta = []
    fila_media = []
    fila_baixa = []

    for item in fila:
        #se item do indice 1 for == 1...
        if item[1] == 1:
            fila_alta.append(item)
        elif item[1] == 2:
            fila_media.append(item)
        elif item[1] == 3:
            fila_baixa.append(item)

        #junta uma fila, "append de lista"
        fila_alta.extend(fila_media)
        fila_alta.extend(fila_baixa)

        return fila_alta

#Fila
class Queue:
    def __init__(self):
        self.fila = []

    def is_empty(self, item):
        #se a fila nao tiver vazia
        if not self.fila:
            return True
        else:
            return False
        
    #adicionar item na fila
    def enqueue(self, item):
        prioridade = definir_prioridade()
        self.fila.append([item, prioridade])

    #remove o primeiro elemento
    def dequeue(self):
        #se a lista nao estiver vazia, remove
        if not self.is_empty():
        #em vez de remover por indice
            self.fila.pop(0)
        else:
            print('fila vazia')

    #retorna o primeiro elemento, mostrar fila, ordem prioridade
    def front(self):
        #processa a fila, de forma bonita, organizado em prioridade...
        fila = processar_tarefa(self.fila)
        return fila[0]
    
    #snakecase separar palavras por underline
    
        
    def cancelar_tarefa(self, tarefa):
        #percorre os indices do tamanho da nossa lista (lenphy, tamanho)
        #percorre os elementos da lista, ignorando o segundo, sabendo só o ID
        for count in range(len(self.fila)):
            #se nosso item for == a tarefa que passou...
            if self.fila[count][0] == tarefa:
                #remove o item, o primeiro item da "dupla tarefa" [item, prioridade]
                self.fila.pop(count)
            else:
                print('Não existe essa tarefa!')

queue = Queue()

queue.enqueue('alex')

print(queue.front())

