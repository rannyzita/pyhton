livros = []

#primeira função    
def adicionar_livro (titulo, autor):
    livros.append({"titulo": titulo, "autor": autor, "emprestado": False})
    print(f"Livro '(titulo)' adicionado com sucesso!")
    
#segunda função
def emprestar_livro (titulo):
    for livro in livros:
        if livro["titulo"] == titulo and not livro["emprestado"]:
            livro["emprestado"] = True 
            print("Livro '(titulo)' emprestado com sucesso!")
            return 
        else: 
            print("Infelizmente, o livro '(titulo)' está indisponível para empréstimo.")
            
#terceira função
def retornar_livro (titulo):
    for livro in livros:
        if livro["titulo"] == titulo and livro["emprestado"]:
            livro["emprestado"] = False
            print("Livro '(titulo)' retornado com sucesso!")
            return 
        else:
            print("Infelizmente, o livro '(titulo)', não pode ser retornado.")
            
#quarta função            
def listar_livros():  
    if not livros:
        print("Nenhum livro registrado!")
        return
    print("Livros disponíveis na biblioteca\n")
    for livro in livros:
        status = "Disponível" if not livro["emprestado"] else "Emprestado"
        print(f"Titulo: {livro['titulo']}, Autor: {livro['autor']}, {status}")            
                        
while True:
    print("\nBiblioteca Estelar de Alexandria\n")
    
    print("1 - Adicionar livro")
    print("2 - Emprestar livro")
    print("3 - Retornar livro")
    print("4 - Listar livros")
    print("5 - Sair\n")
    
    opcao = input("Digite a opção que você deseja: ")
    
    if opcao == "1":
        titulo = input("Digite o titulo do livro: ")
        autor = input("Digite o nome do autor: ")
        adicionar_livro(titulo, autor)
    elif opcao == "2":
        titulo = input("Digite o livro que você quer emprestar: ")
        emprestar_livro(titulo)
    elif opcao == "3":
        titulo = input("Digite o livro que você quer retornar: ")
        retornar_livro(titulo)
    elif opcao == "4":
        listar_livros()
    elif opcao == "5":
        break
    else:
        print("Opcão inválida.")
