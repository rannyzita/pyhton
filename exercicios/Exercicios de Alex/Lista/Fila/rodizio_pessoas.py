class Queue:
    
    def __init__(self):
        self.fila = []
        
    def adicionar(self, item):
        self.fila.append(item)
        
    def mudar_ordem(self, n_operações):
        if self.fila:
            for item in range(n_operações):
               temporario = self.fila.pop(0)
               self.fila.append(temporario)
            return self.fila   
        else:
            return False    
            
fila = Queue()

while True: 
    
    print('1 - Adicionar || 2 - Mudar ordem || 3 - Sair') 
    print('\nDigite a opção:')  
    
    opc = int(input())
    
    if opc == 1:
        item = input('\nDigite o item: ')
        fila.adicionar(item)
        print(f'{item} adicionado com sucesso!')
    elif opc == 2:
        n_operações = int(input('Quantas operações você quer alterar?'))
        retorno = fila.mudar_ordem(n_operações)
        if retorno != False:
            print(retorno)
        else:
            print('Não existe fila!')    
    elif opc == 3:
        break
    else:
        print('Opção Invalida')                    
                    
   