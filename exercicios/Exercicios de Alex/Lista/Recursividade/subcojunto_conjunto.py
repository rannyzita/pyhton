#função recursiva para determinar o subcojunto de um dado conjunto

def subconjuntos(elementos, atual = 0, conjunto_atual = []):
    if atual == len(elementos):
        print(conjunto_atual)
        return
    # Inclui o elemento atual no subconjunto
    subconjuntos(elementos, atual + 1, conjunto_atual + [elementos[atual]])
    # Não inclui o elemento atual no subconjunto
    subconjuntos(elementos, atual + 1, conjunto_atual)

numero_elementos = int(input('Digite o numero de elementos do conjunto: '))  
count = 0
elementos = []

while count < numero_elementos:
    
    elementos.append(float(input(f'Digite o elemento {count + 1}: ')))
    
    count += 1

subconjuntos(elementos)
