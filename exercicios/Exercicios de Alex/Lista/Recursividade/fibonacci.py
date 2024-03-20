def fibonacci(max_vezes, resultado = None):
    
    #se resultado estiver vazia, ou seja, sempre verdadeira...
    if resultado is None:
        resultado = [0, 1]

    #verifica se tem menos de 2 elementos na lista

    if len(resultado) < 2:

        n1 = 0
        n2 = 1

    #se o numero de elementos da lista "resultado" for menor que
    #n de vezes
    #do usuario...

    if len(resultado) < max_vezes:
        soma = resultado[-1] + resultado[-2]
        
        resultado.append(soma)
        return fibonacci(max_vezes, resultado)
        
    #retorna todos os numeros de fibonacci
    return resultado

while True:

    max_vezes = int(input('\nQuantos números de Fibonacci você quer gerar? \n'))

    resultado = fibonacci(max_vezes)

    #imprimi todos os numeros de fibonacci
    print(resultado)
    
    break
