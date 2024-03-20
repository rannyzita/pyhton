class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return self.itens == []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        return self.itens.pop()

def decimal_para_binario(decimal):
    pilha = Pilha()

    while decimal > 0:
        resto = decimal % 2
        pilha.empilhar(resto)
        decimal //= 2

    binario = ""
    while not pilha.vazia():
        binario += str(pilha.desempilhar())

    return binario

# Exemplo de uso
numero_decimal = input('Digite o numero que você quer transformar: ')
resultado_binario = decimal_para_binario(numero_decimal)
print(f"O número decimal {numero_decimal} em binário é: {resultado_binario}")
