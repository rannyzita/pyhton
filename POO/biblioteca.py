class Livro:
    def __init__(self, titulo = '', autor = '', quantidade_exemplares_disponiveis = 0):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_exemplares_disponiveis = quantidade_exemplares_disponiveis
        
    def adicionar_livro(self, titulo, autor, quantidade_exemplares_disponiveis):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_exemplares_disponiveis = quantidade_exemplares_disponiveis
            
class Biblioteca:
    def __init__(self):
        self.lista = []
        self.emprestimos = []
        
    def verificar(self):
        if self.lista:
            return True
        else:
            return False    
            
    def adicionar(self, item):
        self.lista.append(item)
               
    def emprestar(self, item):
        for livro in self.lista:
            if livro.titulo == item and livro.quantidade_exemplares_disponiveis > 0:
                self.emprestimos.append(livro)
                livro.quantidade_exemplares_disponiveis -= 1
                return livro.quantidade_exemplares_disponiveis
        else:
            return False    
                
    def devolver_livro(self, item):
        for livro in self.emprestimos:
            if livro.titulo == item:
                self.emprestimos.remove(livro)
                livro.quantidade_exemplares_disponiveis += 1
                return True
        else:
            return False    
        
    def mostrar(self):
        if self.verificar():
            return self.lista

biblioteca = Biblioteca()

def interface(biblioteca):
    while True:
        print('1 - Adicionar') 
        print('2 - Emprestar')
        print('3 - Devolver')   
        print('4 - Mostrar livros disponíveis')
        print('5 - Sair')
    
        opc = int(input('\nDigite a opção desejada: '))
    
        if opc == 1:
            titulo = input('\nDigite o título do livro: ')
            autor = input('\nDigite o autor(a) do livro: ')
            quantidade = int(input('\nDigite a quantidade de auxiliares: '))
            livro = Livro()
            livro.adicionar_livro(titulo, autor, quantidade)
            biblioteca.adicionar(livro)
            print(f'\n{titulo} do(a) autor(a) {autor} adicionado na Biblioteca.')
        elif opc == 2:
            titulo = input('\nDigite o título do livro que você quer emprestar: ')
            retorno = biblioteca.emprestar(titulo)
            if retorno != False:
                print(f'\nO livro {titulo} foi emprestado com sucesso.')
                print(f'\nAinda restam {retorno} exemplares deste livro.')
            else:
                print(f'\nO livro {titulo} não está disponível para empréstimo.')    
        elif opc == 3:
            titulo = input('\nDigite o título do livro que você quer devolver: ')
            retorno = biblioteca.devolver_livro(titulo)
            if retorno == True:
                print(f'\nO livro {titulo} foi devolvido com sucesso.')
            else:
                print(f'\nO livro {titulo} não pode ser devolvido.')    
        elif opc == 4:
            retorno = biblioteca.mostrar()
            if retorno:
                print('\nLivros Disponiveis')
                for itens in retorno:
                    print(f'\nTitulo do livro: {itens.titulo} || Exemplares: {itens.quantidade_exemplares_disponiveis}') 
            else:
                print('Nenhum livro disponivel para mostrar.')        
        elif opc == 5:
            break
    else:
         print('\nOpção inválida.')
                            
interface(biblioteca)    
    