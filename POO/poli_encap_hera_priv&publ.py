class Animal:
    def __init__(self, nome = '', cor = '', tamanho = ''):
        self.nome = nome
        self._cor = cor
        self.tamanho = tamanho

    def som(self):
        return 'som generico'

    def get_cor(self):
        return self.cor
    
    def set_cor(self, cor):
        self._cor = cor
#definindo a herança
class Ave(Animal):
    def som(self):
        return 'Piu-piu'

class Mamifero(Animal):
    def som(self):
        return 'Se quiser sim mano'

alex_passaro = Ave()
ranny_humana = Mamifero()
animal = Animal()

print(animal.som())
print(ranny_humana.som())
print(alex_passaro.som())


