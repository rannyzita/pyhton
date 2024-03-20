class Lista:
    def __init__(self):
        self.lista = []
        
    def adicionar(self, elemento):
        self.lista.append(elemento)
        
    def remover(self, elemento):
        
        if elemento in self.lista:
            self.lista.remove(elemento)
            return True
        else: 
            return False  
        
    def buscar(self, elemento):
        
        if elemento in self.lista:
            return True
        else:
            return False    
        
    def listar(self):
        return self.lista    
        
Lista = Lista()
        
while True:
    
    print('1 - Adicionar')    
    print('2 - Remover')
    print('3 - Buscar')
    print('4 - Listar')
    print('5 - Sair')
    
    opção = int(input('\nDigite a opção: '))
    
    if opção == 1:
        adicionar = input('\nAdicione o elemento: ')
        Lista.adicionar(adicionar)
        print('\nElemento adicionado com Sucesso! ')
        
    elif opção == 2:
        remover = input('\nDigite o elemento para remover: ')
        mostrar = Lista.remover(remover)
        
        if mostrar == True:
            print('\nElemento removido com sucesso!')
        elif mostrar == False:
            print('\nElemento não existe')    
        
    elif opção == 3:
        buscar = input('\nDigite o elemento que você quer buscar na lista: ')
        resultado = Lista.buscar(buscar)
        if resultado == True :
            print('\nEsse elemento existe na lista!')
        elif resultado == False:
            print('\nEsse elemento não existe na lista!')    
            
    elif opção == 4:
        mostrar = Lista.listar()
        print(mostrar)
    elif opção == 5:
        break
    else: 
        print('Opção Inválida') 
