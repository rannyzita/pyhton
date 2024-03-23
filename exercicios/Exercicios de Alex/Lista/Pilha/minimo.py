class Peek:
    def __init__(self):
        self.pilha = []
        self.min_pilha = []

    def push(self, valor):
        self.pilha.append(valor)
        if not self.min_pilha or valor <= self.min_pilha[-1]:
            self.min_pilha.append(valor)

    def pop(self):
        if not self.pilha:
            return None
        valor = self.pilha.pop()
        if valor == self.min_pilha[-1]:
            self.min_pilha.pop()
        return valor

    def min(self):
        if not self.min_pilha:
            return None
        return self.min_pilha[-1]

pilha = Peek()

quantidade = int(input('Digite a quantidade de elementos da pilha: '))

for count in range(quantidade):
    elemento = input(f'\nDigite o elemento {count+1}: ')
    pilha.push(elemento)

print("\nMenor elemento na pilha:", pilha.min())  
pilha.pop()
print("Menor elemento na pilha após a remoção:", pilha.min())  
    