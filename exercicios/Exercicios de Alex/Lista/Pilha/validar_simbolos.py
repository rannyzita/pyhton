class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            return None

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        else:
            return None

def valida_simbolos(expressao):
    pilha = Pilha()
    mapeamento = {')': '(', '}': '{', ']': '['}
    for simbolo in expressao:
        if simbolo in mapeamento.values():
            pilha.empilhar(simbolo)
        elif simbolo in mapeamento.keys():
            if pilha.esta_vazia() or mapeamento[simbolo] != pilha.desempilhar():
                return False
    return pilha.esta_vazia()


# Teste da função com exemplos de entrada
expressao1 = "{[()]}"
print(valida_simbolos(expressao1))  # Saída esperada: True

expressao2 = "{[(])}"
print(valida_simbolos(expressao2))  # Saída esperada: False
