lista = []

def inverter(lista):
    tamanho = len(lista)
    
    for count in range(tamanho // 2):
        lista[count], lista[-count-1] = lista[-count-1], lista[count]
        
while True:
    
    print('1 - adicionar')         
    print('2 - reverter e encerrar')
    
    opcao = int(input('\nDigite a opcao: '))
    
    if opcao == 1:
        item = input('\nDigite o item que você quer adicionar: ')
        lista.append(item)
        print(f'\nElemento "{item}" adicionado com sucesso!')
    elif opcao == 2:
        inverter(lista)
        print(lista)
        break    
