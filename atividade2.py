class Animal:
    def falar(self):
        print("O animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro diz: Au au!")

class Gato(Animal):
    def falar(self):
        print("O gato diz: Miau!")

class Papagaio(Animal):
    def falar(self):
        print("O papagaio diz: Olá!")

animais = [Cachorro(), Gato(), Papagaio(), Gato(), Cachorro()]

for animal in animais:
    animal.falar()
