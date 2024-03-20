lista = []

def remover_duplicata(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas
    
while True:
    print('1 - adicionar item na lita')
    print('2 - mostrar lista sem itens duplicados')
    print('3 - sair')
    
    opcao = int(input('\nDigite a opcao: '))
    
    if opcao == 1:
        item = input('\nDigite o item que você quer adicionar na lista 1: ')
        lista.append(item)
        print(f'\nElemento "{item}" adicionado com sucesso!')
    elif opcao == 2:
        resultado = remover_duplicata(lista)
        print(resultado)
    elif opcao == 3:
        break
    else:
        print('Opção inválida')
