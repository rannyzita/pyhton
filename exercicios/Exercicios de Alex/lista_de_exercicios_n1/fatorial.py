#fatorial com parâmetro N, função recursiva

def fatorial(N):

    if N == 0:
        return 1
    else:
        return N*fatorial(N-1)

final = 0 

while True:

    N = int(input('Digite um número para fazer o seu fatorial: '))

    resultado = fatorial(N)

    final = final + resultado

    print(f'Fatorial !{N}:{final}')