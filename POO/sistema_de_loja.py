class Produto:
    def __init__(self, nome='', preco=0, quantidade=0):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def calcular_desconto(self):
        pass

    def verificar_disponibilidade(self):
        pass
    
    def remover_quantidade(self, quantidade):
        if self.__quantidade > 0 and quantidade <= self.__quantidade:
            self.__quantidade -= quantidade
            return True
        else:
            return False
            
    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
        
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco
    
    def get_quantidade(self):
        return self.__quantidade

class Eletronico(Produto):
    def __init__(self):
        super().__init__()
        self.__marca = ''

    def calcular_desconto(self):
        # Desconto de 25%
        return -self.get_preco() * 0.25

    def verificar_disponibilidade(self):
        return self.get_quantidade() > 0
    
    def set_remover(self, nome):
        if self.get_nome() == nome:
            self.set_nome('')
            self.set_quantidade(0)
            self.__marca = ''
            return True
        else:
            return False
        
    def set_marca(self, marca):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

class Roupa(Produto):
    def __init__(self):
        super().__init__()
        self.__tamanho = ''

    def calcular_desconto(self):
        # Desconto de 20%
        return -self.get_preco() * 0.20

    def verificar_disponibilidade(self):
        return self.get_quantidade() > 0
    
    def set_remover(self, nome):
        if self.get_nome() == nome:
            self.set_nome('')
            self.set_quantidade(0)
            self.__tamanho = ''
            return True
        else:
            return False
        
    def set_tamanho(self, tamanho):
        self.__tamanho = tamanho

    def get_tamanho(self):
        return self.__tamanho

class Alimento(Produto):
    def __init__(self):
        super().__init__()
        self.__data_de_validade = ''

    def calcular_desconto(self):
        # Desconto de 15%
        return -self.get_preco() * 0.15

    def verificar_disponibilidade(self):
        return self.get_quantidade() > 0
    
    def set_remover(self, nome):
        if self.get_nome() == nome:
            self.set_nome('')
            self.set_quantidade(0)
            self.__data_de_validade = ''
            return True
        else:
            return False
        
    def set_data_validade(self, data):
        self.__data_de_validade = data

    def get_data_validade(self):
        return self.__data_de_validade

eletronico = Eletronico()
roupa = Roupa()
alimento = Alimento()

while True:
    print('\n1 - Adicionar produto no sistema')
    print('2 - Remover produto do sistema')
    print('3 - Mostrar desconto do produto')
    print('4 - Mostrar quantidades do produto')
    print('5 - Geral do Produto')
    print('6 - Geral dos 3 produtos')
    print('7 - Remover quantidade de produto')
    print('8 - Sair do sistema')

    opc = int(input('\nDigite a opção desejada: '))

    if opc == 1:
        while True:
            print('1 - Eletronico')
            print('2 - Roupa')
            print('3 - Alimento')

            tipo_produto = int(input('\nDigite o tipo de produto que você quer adicionar: '))

            if tipo_produto == 1:
                nome = input('\nDigite o nome do produto: ')
                marca = input('Digite a marca do produto: ')
                quantidade = int(input('Digite a quantidade do produto: '))
                preco = float(input(f'Digite o preço do {nome}: '))
                eletronico.set_nome(nome)
                eletronico.set_marca(marca)
                eletronico.set_quantidade(quantidade)
                eletronico.set_preco(preco)
                print(f'\nEletrônico: {nome} adicionado com sucesso!')
                break
            elif tipo_produto == 2:
                nome = input('\nDigite o nome da roupa: ')
                tamanho = input('Digite o tamanho da roupa: ')
                quantidade = int(input('Digite a quantidade do produto: '))
                preco = float(input(f'Digite o preço do {nome}: '))
                roupa.set_nome(nome)
                roupa.set_tamanho(tamanho)
                roupa.set_quantidade(quantidade)
                roupa.set_preco(preco)
                print(f'\nRoupa: {nome} adicionado com sucesso!')
                break
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto: ')
                validade = input('Digite a validade do produto: ')
                quantidade = int(input('Digite a quantidade do produto: '))
                preco = float(input(f'Digite o preço do {nome}: '))
                alimento.set_nome(nome)
                alimento.set_data_validade(validade)
                alimento.set_quantidade(quantidade)
                alimento.set_preco(preco)
                print(f'\nAlimento: {nome} adicionado com sucesso!')
                break
            else:
                print('\nOpção Inválida.')
    elif opc == 2:
        while True: 
            print('1 - Eletronico')
            print('2 - Roupa')
            print('3 - Alimento')
            tipo_produto = int(input('\nDigite a categoria do produto que você quer remover: '))

            if tipo_produto == 1:
                nome = input('\nDigite o nome do produto que você quer remover: ')
                if eletronico.set_remover(nome):
                    print('\nProduto removido com sucesso!')
                else:
                    print('\nProduto não consta no sistema.')
                break
            elif tipo_produto == 2:
                nome = input('Digite o nome do produto que você quer remover: ')
                if roupa.set_remover(nome):
                    print('\nProduto removido com sucesso!')
                else:
                    print('\nProduto não consta no sistema.')
                break
            elif tipo_produto == 3:
                nome = input('Digite o nome do produto que você quer remover: ')
                if alimento.set_remover(nome):
                    print('\nProduto removido com sucesso!')
                else:
                    print('\nProduto não consta no sistema.')
                break
            else:
                print('\nOpção Inválida')
    elif opc == 3:
        while True: 
            print('1 - Eletronico')
            print('2 - Roupa')
            print('3 - Alimento')
            tipo_produto = int(input('\nDigite a categoria do produto que você quer ver o desconto: '))

            if tipo_produto == 1:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if eletronico.get_nome() == nome:
                    resultado = eletronico.calcular_desconto()
                    print('\nO desconto do produto vai ser de:')
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 2:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if roupa.get_nome() == nome:
                    resultado = roupa.calcular_desconto()
                    print('\nO desconto do produto vai ser de:')
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if alimento.get_nome() == nome:
                    resultado = alimento.calcular_desconto()
                    print('\nO desconto do produto vai ser de:')
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('\nProduto não consta no sistema.')
            else:
                print('\nOpção Inválida.')
    elif opc == 4:
        while True: 
            print('1 - Eletronico')
            print('2 - Roupa')
            print('3 - Alimento')
            tipo_produto = int(input('\nDigite a categoria do produto que você quer ver a quantidade: '))

            if tipo_produto == 1:
                nome = input('\nDigite o nome do produto que você quer ver a quantidade: ')
                if eletronico.get_nome() == nome:
                    resultado = eletronico.get_quantidade()
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 2:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if roupa.get_nome() == nome:
                    resultado = roupa.get_quantidade()
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if alimento.get_nome() == nome:
                    resultado = alimento.get_quantidade()
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            else:
                print('Opção Inválida.')
    elif opc == 5:
        while True: 
            print('1 - Eletronico')
            print('2 - Roupa')
            print('3 - Alimento')
            tipo_produto = int(input('\nDigite a categoria do produto que você quer ver o geral: '))

            if tipo_produto == 1:
                nome = input('\nDigite o nome do produto que você quer ver o geral: ')
                if eletronico.get_nome() == nome:
                    print(f'\nNome: {eletronico.get_nome()}')
                    print(f'Marca: {eletronico.get_marca()}')
                    print(f'Quantidade: {eletronico.get_quantidade()}')
                    print(f'Preço sem desconto: {eletronico.get_preco()}')
                    print(f'Preço com desconto: {eletronico.get_preco() + eletronico.calcular_desconto()}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 2:
                nome = input('\nDigite o nome do produto que você quer ver o geral: ')
                if roupa.get_nome() == nome:
                    print(f'\nNome: {roupa.get_nome()}')
                    print(f'Tamanho: {roupa.get_tamanho()}')
                    print(f'Quantidade: {roupa.get_quantidade()}')
                    print(f'Preço sem desconto: {roupa.get_preco()}')
                    print(f'Preço com desconto: {roupa.get_preco() + roupa.calcular_desconto()}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto que você quer ver o geral: ')
                if alimento.get_nome() == nome:
                    print(f'\nNome: {alimento.get_nome()}')
                    print(f'Data de validade: {alimento.get_data_validade()}')
                    print(f'Quantidade: {alimento.get_quantidade()}')
                    print(f'Preço sem desconto: {alimento.get_preco()}')
                    print(f'Preço com desconto: {alimento.get_preco() + alimento.calcular_desconto()}')
                    break
                else:
                    print('\nProduto não consta no sistema.')
            else:
                print('\nOpção Inválida.')
    elif opc == 6:
        nome_eletronico = input('\nDigite o nome do Eletrônico que você quer ver o geral: ')
        nome_roupa = input('\nDigite o nome da roupa que você quer ver o geral: ')
        nome_alimento = input('\nDigite o nome do produto que você quer ver o geral: ')
        if eletronico.get_nome() == nome_eletronico:
            print(f'\nNome: {eletronico.get_nome()}')
            print(f'Marca: {eletronico.get_marca()}')
            print(f'Quantidade: {eletronico.get_quantidade()}')
            print(f'Preço sem desconto: {eletronico.get_preco()}')
            print(f'Preço com desconto: {eletronico.get_preco() - eletronico.calcular_desconto()}')
        else:
            print('Produto não consta no sistema.')
        if roupa.get_nome() == nome_roupa:
            print(f'\nNome: {roupa.get_nome()}')
            print(f'Tamanho: {roupa.get_tamanho()}')
            print(f'Quantidade: {roupa.get_quantidade()}')
            print(f'Preço sem desconto: {roupa.get_preco()}')
            print(f'Preço com desconto: {roupa.get_preco() - roupa.calcular_desconto()}')
        else:
            print('Produto não consta no sistema.')
        if alimento.get_nome() == nome_alimento:
            print(f'\nNome: {alimento.get_nome()}')
            print(f'Data de validade: {alimento.get_data_validade()}')
            print(f'Quantidade: {alimento.get_quantidade()}')
            print(f'Preço sem desconto: {alimento.get_preco()}')
            print(f'Preço com desconto: {alimento.get_preco() - alimento.calcular_desconto()}')
        else:
            print('\nProduto não consta no sistema.')
    elif opc == 7:
        while True: 
            print('1 - Eletronico')
            print('2 - Roupa')
            print('3 - Alimento')
            tipo_produto = int(input('\nDigite a categoria do produto que você quer ver remover a quantidade: '))

            if tipo_produto == 1:
                nome = input('\nDigite o nome do produto: ')
                print(f'Quantidade atual: {eletronico.get_quantidade()}')
                quantidade = int(input('Digite a quantidade que você quer remover: '))
                if eletronico.get_nome() == nome:
                    if eletronico.remover_quantidade(quantidade):
                        print('\nQuantidade removida com sucesso!')
                    else:
                        print('\nNão há produtos suficientes em estoque.')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 2:
                nome = input('\nDigite o nome do produto: ')
                print(f'Quantidade atual: {roupa.get_quantidade()}')
                quantidade = int(input('Digite a quantidade que você quer remover: '))
                if roupa.get_nome() == nome:
                    if roupa.remover_quantidade(quantidade):
                        print('\nQuantidade removida com sucesso!')
                    else:
                        print('\nNão há produtos suficientes em estoque.')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 3:
                nome = input('\nDigite o nome: ')
                print(f'Quantidade atual: {alimento.get_quantidade()}')
                quantidade = int(input('Digite a quantidade que você quer remover: '))
                if alimento.get_nome() == nome:
                    if alimento.remover_quantidade(quantidade):
                        print('\nQuantidade removida com sucesso!')
                    else:
                        print('\nNão há produtos suficientes em estoque.')
                    break
                else:
                    print('Produto não consta no sistema.')
            else:
                print('Opção Inválida.')
    elif opc == 8:
        break
    else:
        print('\nOpção Inválida')
