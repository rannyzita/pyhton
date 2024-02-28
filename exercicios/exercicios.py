#1. Escreva um programa que calcula a média de três números digitados pelo usuário.

n1 = float (input('\nDigite a nota 1: '))
n2 = float (input('\nDigite a nota 2: '))
n3 = float (input('\nDigite a nota 3: '))

#cálculo da média 
media = (n1 + n2 + n3)/3

print(f'\n{media}')

#2. Crie uma função em Python que recebe uma lista de números como parâmetro e retorna o maior número da lista.

lista = [1, 3, 5, 7]

def calcular_numero_maior(lista):
    
    maior = -1
    
    for count in lista:
        if count > maior:
            maior = count
            
    return(maior)
    
print(calcular_numero_maior(lista))

#Ou…

lista = [1, 3, 5, 7]

def calcular_numero_maior(lista):
    return(max(lista))
    
print(calcular_numero_maior(lista))

#Tem o min, que retornará o valor mínimo. Ou seja, imprimirá 1.

#3. Escreva um programa que solicita ao usuário o raio de um círculo e calcula a área e o perímetro desse círculo.

raio_do_circulo = float (input('Digite a medida do raio do circulo: '))

#Cálculo do perímetro do circulo
π = 3.1415
perimetro = 2*π*raio_do_circulo
area_do_circulo = π*(raio_do_circulo**2)

print(f'\nPerímetro do circulo: {perimetro:.2f}')
print(f'\nÁrea do círculo: {area_do_circulo:.2f}')

#4. Crie uma função que receba como parâmetro um número inteiro e retorne True se o número for primo, caso contrário retorne False.

numero = int (input('Digite um número: '))
 
def primo_ou_n(numero):
    count = 2 
    resultado = 0
    
    while count <= numero/2:
        if numero % count == 0:
            resultado += 1
            break
        count+= 1
        
    if resultado == 0:
        return 'True'
    else:
        return 'False'
    
print(primo_ou_n(numero))       

#5. Crie uma função que receba dois números como parâmetros e retorne a soma deles.
n1 = int (input('Digite um numero: '))
n2 = int (input('Digite outro número: '))

def calcular_numero_maior(n1,n2):
    
    return(n1 + n2)
    
print(calcular_numero_maior(n1, n2))  

#6. Escreva um programa que utilize uma estrutura de repetição para imprimir os números de 1 a 10.
for i in range (1, 11) :
    print(f'\n{i}')

#7. Desenvolva um programa que utilize estruturas condicionais para verificar se um número é par ou ímpar.

numero = int (input('Digite um número: '))

if numero % 2 == 0 :
    print('\nÉ par')
else: 
    print('\nÉ ímpar')
