lista_1 = []
lista_2 = []
lista_intercalada = []

def intercalar(lista_1, lista_2, lista_intercalada):
    tamanho_menor = min(len(lista_1), len(lista_2))
    
    for i in range(tamanho_menor):
        lista_intercalada.append(lista_1[i])
        lista_intercalada.append(lista_2[i])
    
    # Adiciona os elementos restantes da lista 1
    for elemento in lista_1[tamanho_menor:]:
        lista_intercalada.append(elemento)
    
    # Adiciona os elementos restantes da lista 2
    for elemento in lista_2[tamanho_menor:]:
        lista_intercalada.append(elemento)

while True:
    print('1 - adicionar item na lista 1')
    print('2 - adicionar item na lista 2')
    print('3 - intercalar listas')         
    print('4 - mostrar lista intercalada')
    print('5 - sair')
    
    opcao = int(input('\nDigite a opcao: '))
    
    if opcao == 1:
        item = input('\nDigite o item que você quer adicionar na lista 1: ')
        lista_1.append(item)
        print(f'\nElemento "{item}" adicionado com sucesso!')
    elif opcao == 2:
        item = input('\nDigite o item que você quer adicionar na lista 2: ')
        lista_2.append(item)
        print(f'\nElemento "{item}" adicionado com sucesso!')
    elif opcao == 3:
        intercalar(lista_1, lista_2, lista_intercalada)
        print('Listas intercaladas!')
    elif opcao == 4:
        print(lista_intercalada)
    elif opcao == 5:
        break
    else:
        print('Opção inválida')
