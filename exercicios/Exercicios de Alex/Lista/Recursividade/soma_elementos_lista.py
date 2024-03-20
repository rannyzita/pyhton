def soma_lista(quantidade_elementos, lista = None):
    
    if lista is None:
        lista = []
    
    if quantidade_elementos > 0:
        n = int(input('Digite o número: '))
        lista.append(n)
        return soma_lista(quantidade_elementos - 1, lista)
        
    return lista
        
while True:
    
    quantidade_elementos = int(input('Digite a quantidade de elementos da lista: '))
    
    numeros = soma_lista(quantidade_elementos)
        
    print(f"\nSoma de todos os elementos:{sum(numeros)}")
    
    break
