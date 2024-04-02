def processar_categoria():
    print('1 - Urgente || 2 - Normal')
    print('Digite a opção:')

    opc = int(input())

    return opc

def ordem_chegada(lista):
    lista_urgencia = []
    lista_normal = []

    for item in lista:
        if item[1] == 1:
            lista_urgencia.append(item)
        elif item[1] == 2:
            lista_normal.append(item)
    lista_urgencia.extend(lista_normal)

    return lista_urgencia

class Queue:
    def __init__(self):
        self.lista = []

    def adicionar(self, item):
        categoria = processar_categoria()
        self.lista.append([item, categoria])
        ordem_chegada(self.lista)

    def atender(self):
        if self.lista:
            retorno = self.lista.pop(0)
            return retorno

    def cancelar(self, item):
        if self.lista:
            for elemento in self.lista:
                if item in elemento:
                    self.lista.remove(elemento)
                    return True
            else:
                return False

    def consultar(self):
        print(self.lista)

fila = Queue()

while True:

    print('1 - Adicionar')
    print('2 - Atender')
    print('3 - Cancelar')
    print('4 - Consultar')
    print('5 - Sair')

    opc = int(input('Digite a opção:'))

    if opc == 1:
        item = input('Digite o item que você quer adicionar: ')
        fila.adicionar(item)
        print(f'{item} adicionado com sucesso!')
    elif opc == 2:
        retorno = fila.atender()
        print(f'{retorno} atendido com sucesso!')
    elif opc == 3:
        item = input('Digite o item que você quer cancelar:')
        retorno = fila.cancelar(item)

        if retorno == True:
            print(f'{item} cancelado com sucesso!')
        elif retorno == False:
            print('item não consta na lista')
    elif opc == 4:
        retorno = fila.consultar()
        for item in retorno:
            print(item[0])
    elif opc == 5:
        break
    else: 
        print('opção inválida!')


    
