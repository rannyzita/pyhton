#Questão: 
#Considere um sistema de uma loja que possui diferentes tipos de produtos, incluindo eletrônicos, roupas e alimentos. Cada produto tem um nome, um preço e métodos para calcular desconto e verificar disponibilidade.

#Abstração e Encapsulamento: 
#Crie uma classe abstrata chamada Produto que contenha os atributos comuns a todos os produtos (nome e preço) e métodos abstratos calcular_desconto() e verificar_disponibilidade(). Encapsule os atributos da classe Produto para garantir que eles só possam ser acessados e modificados por métodos da própria classe.
class Produto:
    def __init__(self, nome = '', preco = 0, quantidade = 0):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_desconto(self, preco):
        pass

    def verificar_disponibilidade(self):
        pass

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

    def set_quantidade(self, quantidade):
        self.quantidade = quantidade
        
    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco
    
    def get_quantidade(self):
        return self.quantidade
        
#Herança: 
#Crie três subclasses de Produto: Eletronico, Roupa e Alimento. A classe Eletronico deve ter um atributo adicional para armazenar a marca. A classe Roupa deve ter um atributo adicional para armazenar o tamanho. A classe Alimento deve ter um atributo adicional para armazenar a data de validade.

#Polimorfismo: 
#Implemente os métodos calcular_desconto() e verificar_disponibilidade() nas subclasses Eletronico, Roupa e Alimento de forma que cada um aplique um desconto e verifique a disponibilidade de acordo com as características de cada tipo de produto. Crie instâncias de um Eletronico, uma Roupa e um Alimento, chame os métodos calcular_desconto() e verificar_disponibilidade() para cada um e exiba os resultados obtidos para cada produto.

class Eletronico(Produto):
    def __init__(self):
        super().__init__()
        self.marca = ''

    def calcular_desconto(self):
        #desconto de 25%
        preco_com_desconto = 0
        quantidade_desconto = self.get_preco()*0.25
        preco_com_desconto = - quantidade_desconto
        return preco_com_desconto

    def verificar_disponibilidade(self):
        if self.get_quantidade() > 0:
            return True
        else:
            return False
    
    def set_remover(self, nome):
        if self.nome == nome:
            self.nome = ''
            self.quantidade = 0
            self.marca = ''
            return True
        else:
            return False
        
    def set_marca(self, marca):
        self.marca = marca

    def get_marca(self):
        return self.marca

class Roupa(Produto):
    def __init__(self):
        super().__init__()
        self.tamanho = ''

    def calcular_desconto(self):
        #desconto de 20%
        preco_com_desconto = 0
        quantidade_desconto = self.get_preco()*0.20
        preco_com_desconto = - quantidade_desconto
        return preco_com_desconto

    def verificar_disponibilidade(self):
        if self.get_quantidade() > 0:
            return True
        else:
            return False
    
    def set_remover(self, nome):
        if self.nome == nome:
            self.nome = ''
            self.quantidade = 0
            self.tamanho = ''
            return True
        else:
            return False
        
    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    def get_tamanho(self):
        return self.tamanho

class Alimento(Produto):
    def __init__(self):
        super().__init__()
        self.data_de_validade = ''

    def calcular_desconto(self):
        #desconto de 15%
        preco_com_desconto = 0
        quantidade_desconto = self.get_preco()*0.15
        preco_com_desconto = - quantidade_desconto
        return preco_com_desconto

    def verificar_disponibilidade(self):
        if self.get_quantidade() > 0:
            return True
        else:
            return False
    
    def set_remover(self, nome):
        if self.nome == nome:
            self.nome = ''
            self.quantidade = 0
            self.data_de_validade = ''
            return True
        else:
            return False
        
    def set_data_validade(self, data):
        self.data_de_validade = data

    def get_data_validade(self):
        return self.data_de_validade

Eletronico = Eletronico()
Roupa = Roupa()
Alimento = Alimento()

while True:
    print('\n1 - Adicionar produto no sistema')
    print('2 - Remover produto do sistema')
    print('3 - Mostrar desconto do produto')
    print('4 - Mostrar quantidades do produto')
    print('5 - Geral do Produto')
    print('6 - Geral dos 3 produtos')
    print('7 - Sair do sistema')

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
                Eletronico.set_nome(nome)
                Eletronico.set_marca(marca)
                Eletronico.set_quantidade(quantidade)
                Eletronico.set_preco(preco)
                print(f'\nEletrônico: {nome} adicionado com sucesso!')
                break
            elif tipo_produto == 2:
                nome = input('\nDigite o nome da roupa: ')
                tamanho = input('Digite o tamanho da roupa: ')
                quantidade = int(input('Digite a quantidade do produto: '))
                preco = float(input(f'Digite o preço do {nome}: '))
                Roupa.set_nome(nome)
                Roupa.set_tamanho(marca)
                Roupa.set_quantidade(quantidade)
                Roupa.set_preco(preco)
                print(f'\nRoupa: {nome} adicionado com sucesso!')
                break
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto: ')
                validade = input('Digite a validade do produto: ')
                quantidade = int(input('Digite a quantidade do produto: '))
                preco = float(input(f'Digite o preço do {nome}: '))
                Alimento.set_nome(nome)
                Alimento.set_data_validade(marca)
                Alimento.set_quantidade(quantidade)
                Alimento.set_preco(preco)
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
                if Eletronico.set_remover(nome) == True:
                    print('\nProduto removido com sucesso!')
                else:
                    print('\nProduto não consta no sistema.')
                break
            elif tipo_produto == 2:
                nome = input('Digite o nome do produto que você quer remover: ')
                if Roupa.set_remover(nome) == True:
                    print('\nProduto removido com sucesso!')
                else:
                    print('\nProduto não consta no sistema.')
                break
            elif tipo_produto == 3:
                nome = input('Digite o nome do produto que você quer remover: ')
                if Alimento.set_remover(nome) == True:
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
                if Eletronico.get_nome() == nome:
                    resultado = Eletronico.calcular_desconto()
                    print('\nO desconto do produto vai ser de:')
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 2:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if Roupa.get_nome() == nome:
                    resultado = Roupa.calcular_desconto()
                    print('\nO desconto do produto vai ser de:')
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if Alimento.get_nome == nome:
                    resultado = Alimento.calcular_desconto()
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
                if Eletronico.get_nome() == nome:
                    resultado = Eletronico.get_quantidade()
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 2:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if Roupa.get_nome() == nome:
                    resultado = Roupa.get_quantidade()
                    print(f'\n{nome}: {resultado}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto que você quer ver o desconto: ')
                if Alimento.get_nome == nome:
                    resultado = Alimento.get_quantidade()
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
                if Eletronico.get_nome() == nome:
                    print(f'Nome: {Eletronico.get_nome()}')
                    print(f'Marca: {Eletronico.get_marca()}')
                    print(f'Quantidade: {Eletronico.get_quantidade()}')
                    print(f'Preço sem desconto: {Eletronico.get_preco()}')
                    print(f'Preço com desconto: {Eletronico.get_preco() - Eletronico.calcular_desconto()}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 2:
                nome = input('\nDigite o nome do produto que você quer ver o geral: ')
                if Roupa.get_nome() == nome:
                    print(f'Nome: {Roupa.get_nome()}')
                    print(f'Tamanho: {Roupa.get_tamanho()}')
                    print(f'Quantidade: {Roupa.get_quantidade()}')
                    print(f'Preço sem desconto: {Roupa.get_preco()}')
                    print(f'Preço com desconto: {Roupa.get_preco() - Roupa.calcular_desconto()}')
                    break
                else:
                    print('Produto não consta no sistema.')
            elif tipo_produto == 3:
                nome = input('\nDigite o nome do produto que você quer ver o geral: ')
                if Alimento.get_nome == nome:
                    print(f'Nome: {Alimento.get_nome()}')
                    print(f'Data de validade: {Alimento.get_marca()}')
                    print(f'Quantidade: {Alimento.get_quantidade()}')
                    print(f'Preço sem desconto: {Alimento.get_preco()}')
                    print(f'Preço com desconto: {Alimento.get_preco() - Alimento.calcular_desconto()}')
                    break
                else:
                    print('\nProduto não consta no sistema.')
            else:
                print('\nOpção Inválida.')
    elif opc == 6:
        nome_eletronico = input('\nDigite o nome do Eletrônico que você quer ver o geral: ')
        nome_roupa = input('\nDigite o nome da roupa que você quer ver o geral: ')
        nome_alimento = input('\nDigite o nome do produto que você quer ver o geral: ')
        if Eletronico.get_nome() == nome_eletronico:
            print(f'\nNome: {Eletronico.get_nome()}')
            print(f'Marca: {Eletronico.get_marca()}')
            print(f'Quantidade: {Eletronico.get_quantidade()}')
            print(f'Preço sem desconto: {Eletronico.get_preco()}')
            print(f'Preço com desconto: {Eletronico.get_preco() - Eletronico.calcular_desconto()}')
            break
        else:
            print('Produto não consta no sistema.')
        if Roupa.get_nome() == nome_roupa:
            print(f'\nNome: {Roupa.get_nome()}')
            print(f'Tamanho: {Roupa.get_tamanho()}')
            print(f'Quantidade: {Roupa.get_quantidade()}')
            print(f'Preço sem desconto: {Roupa.get_preco()}')
            print(f'Preço com desconto: {Roupa.get_preco() - Roupa.calcular_desconto()}')
            break
        else:
            print('Produto não consta no sistema.')
        if Alimento.get_nome == nome_alimento:
            print(f'\nNome: {Alimento.get_nome()}')
            print(f'Data de validade: {Alimento.get_marca()}')
            print(f'Quantidade: {Alimento.get_quantidade()}')
            print(f'Preço sem desconto: {Alimento.get_preco()}')
            print(f'Preço com desconto: {Alimento.get_preco() - Alimento.calcular_desconto()}')
            break
        else:
            print('\nProduto não consta no sistema.')
    elif opc == 7:
        break
    else:
        print('\nOpção Inválida')
