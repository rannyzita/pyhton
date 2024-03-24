class Queue:
    
    def __init__(self):
        self.fila = []
        
    def adicionar(self, item):
        self.fila.append(item)
        
    def remover(self):
        if self.fila:
            retorno = self.fila.pop(0)
            return retorno
        else:
            return False
            
    def inverter(self):
        if self.fila:
            self.fila.reverse()
            return self.fila
        else:
            return False
            
fila = Queue()

while True:
    
    print('1 - adicionar || 2 - Remover')
    print('3 - Inverter || 4 - Sair')  
    print('\nDigite a opção: ') 
    
    opc = int(input())     
    
    if opc == 1:
        item = input('\nDigite o item que você quer adicionar: ')
        fila.adicionar(item)
        print(f'\n{item} adicionado com sucesso!')
    elif opc == 2:
        retorno = fila.remover()
        if retorno != False:
            print(f'{retorno} removido com sucesso da fila!')
        else:
            print('Não existe fila!')    
    elif opc == 3:
        retorno = fila.inverter()
        if retorno != False:
            print(retorno)
        else:
            print('Não existe fila!')    
    elif opc == 4:
        break
    else:
        print('Opção invalida!')    
            