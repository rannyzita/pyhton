lista = []
#código de rannyzita

def adicionar(lista, pedido):
    lista.append({"Pedido": pedido})
    print(f'\nPedido "{pedido}" adicionado!')

def remover(lista, pedido):
    for count in lista:
        #validação de dados
        if count["Pedido"] == pedido:
           lista.remove(count)
           print(f'\nPedido "{pedido}" removido com sucesso!') 

def alterar(lista, pedido, pedido_novo):
    for count in lista:
        #validação e alteração de dados
        if count["Pedido"] == pedido:
           count["Pedido"] = pedido_novo
           print('Pedido alterado com sucesso!')
            
while True:

    print('1 - Adicionar\n2 - Remover\n3 - Alterar\n4 - Listar\n5 - Sair')

    opcao = input('\nDigite a opção que você deseja: ')
    #desvio condicional de opções
    if opcao == '1':
        pedido = input('\nDigite o pedido que vc deseja: ')
        adicionar(lista, pedido)
    elif opcao == '2':
        pedido = input('\nDigite o pedido que vc quer remover: ')
        remover(lista, pedido)
    elif opcao == '3':
        pedido = input('\nDigite o pedido que vc quer alterar: ')
        pedido_novo = input('\nDigite o novo pedido: ')
        alterar(lista, pedido, pedido_novo)
    elif opcao == '4':
        print('\n')
        for count in lista:
            print(count['Pedido'])
        print('\n')     
    elif opcao == '5':
        break
    else:
        print('\nOpção Inválida\n')