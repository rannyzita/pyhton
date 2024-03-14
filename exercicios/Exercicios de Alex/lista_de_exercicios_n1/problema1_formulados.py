#tem que botar dicionário na lista itens?
#a lista itens tem que estar nos dois objetos? queue e stack

class Queue:

    def __init__(self):
        itens = []

    def adicionar(self, item):
        return self.itens.append(item)
    
    def urgência_baixa(self, item):
        pass
    
    def urgência_alta(self, item):
        pass

    def urgência_média(self, item):
        pass

class Stack:

    def __init__(self):
        itens = []

    def cancelar_tarefa(self):
        pass

queue = Queue()
stack = Stack()

while True:

    print('\nOPÇÕES')
    print('\n1 - Adicionar tarefa')
    print('\n2 - Processar tarefa')
    print('\n3 - Cancelar tarefa')
    print('\n4 - Sair')
    
    opção = int(input('Digite a opção:'))

    while True:

        if opção == 1:  
            item = input('Digite o item que você quer adicionar: ')

            print('\nNÍVEL DE URGÊNCIA\n')
            print('\n1 - Urgência Baixa')
            print('\n2 - Urgência Média')
            print('\n3 - Urgência Baixa')

            urgência = int(input('Digite o nível de Urgência:'))

            if urgência == 1:
                mostrar = queue.urgência_baixa(item)
                break

            elif urgência == 2:
                mostrar = queue.urgência_média(item)
                break

            elif urgência == 3:
                mostrar = queue.urgência_alta(item)
                break

            elif urgência == 4:
                break
            else:
                print('Opção inválida')


    


        

        