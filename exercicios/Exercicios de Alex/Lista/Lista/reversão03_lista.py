lista = []
    
while True:
    
    print('1 - adicionar')         
    print('2 - reverter e encerrar')
    
    opcao = int(input('\nDigite a opcao: '))
    
    if opcao == 1:
        item = input('\nDigite o item que você quer adicionar: ')
        lista.append(item)
        print(f'\nElemento "{item}" adicionado com sucesso!')
    elif opcao == 2:
        lista.reverse()
        print(lista)
        break    
