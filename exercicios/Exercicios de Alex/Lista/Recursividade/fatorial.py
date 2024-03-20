def fatorial(n):

    if n == 0 or n == 1:
        return n
    
    return n*fatorial(n-1)

numero = int(input("Digite o número que você quer fatorar: "))

auxiliar = fatorial(numero)

resultado = 0
resultado = resultado + auxiliar

print(f'O fatorial de {numero}!: {resultado}')