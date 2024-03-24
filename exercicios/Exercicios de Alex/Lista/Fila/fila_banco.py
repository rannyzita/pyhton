class FilaDeBanco:
    
    def __init__(self):
        self.fila = []
        
    def adicionar(self, cliente):
        self.fila.append(cliente)
        
    def atender_cliente(self):
        if self.fila:
            cliente = self.fila.pop(0)
            return cliente
        else:
            return False
            
    def mostrar_fila(self):
        if self.fila:
            print(self.fila)
        else:
            return False
            
fila = FilaDeBanco()            

while True: 
    
    print('1 - Adicionar Cliente || 2 - Atender Cliente') 
    print('3 - Mostrar fila || 4 - Sair')           
    print('\n Digite a opção:')
    
    opc = int(input())
    
    if opc == 1:
        cliente = input('\nDigite o nome do cliente:')
        retorno = fila.adicionar(cliente)
        print(f'\n{cliente} foi adicionado(a)!')
    elif opc == 2:
        retorno = fila.atender_cliente()
        if retorno != False:
            print(f'{retorno} atendido(a)!')
        else:
            print('Não existe fila!')    
    elif opc == 3:
        retorno = fila.mostrar_fila()
        if retorno == True:
            print(fila.mostrar_fila)
        elif retorno == False:
           print('\nNão existe fia')
    elif opc == 4:
        break
    else:
        print('\nOpção inválida')                