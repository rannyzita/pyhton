class Fila:
    def __init__(self):
        self.items = []

    def adicionar(self, item):
        self.items.append(item)

    def remover(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def tamanho(self):
        return len(self.items)

    def esta_vazia(self):
        return self.tamanho() == 0


def distribuir_chamadas(fila_chamadas, fila_atendentes):
    chamadas_nao_atendidas = Fila()

    while not fila_chamadas.esta_vazia():
        if not fila_atendentes.esta_vazia():
            atendente = fila_atendentes.remover()
            chamada = fila_chamadas.remover()
            print(f"Atendendo chamada {chamada} pelo atendente {atendente}")
            # Simulação de atendimento da chamada
            fila_atendentes.adicionar(atendente)  # Coloca o atendente de volta na fila
        else:
            chamada_nao_atendida = fila_chamadas.remover()
            chamadas_nao_atendidas.adicionar(chamada_nao_atendida)

    return chamadas_nao_atendidas

fila_chamadas = Fila()
fila_chamadas.adicionar(1)
fila_chamadas.adicionar(2)
fila_chamadas.adicionar(3)

fila_atendentes = Fila()
fila_atendentes.adicionar('A')
fila_atendentes.adicionar('B')

chamadas_nao_atendidas = distribuir_chamadas(fila_chamadas, fila_atendentes)

print("Chamadas não atendidas:", list(chamadas_nao_atendidas.items))

