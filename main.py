class Animal:
    def __init__(self, nome, raca, cor, idade, peso) -> None:
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.idade = idade
        self.peso = peso

    def emitirSom(self):
        return "Este animal faz um som genérico"

class Cachorro(Animal):
    def __init__(self, nome, raca, cor, idade, peso, pedigree) -> None:
        super().__init__(nome, raca, cor, idade, peso)
        self.pedigree = pedigree

    def emitirSom(self):
        return "O cachorro está latindo"

class Gato(Animal):
    def __init__(self, nome, raca, cor, idade, peso) -> None:
        super().__init__(nome, raca, cor, idade, peso)

    def emitirSom(self):
        return "O gato está miando."

cachorro1 = Cachorro(nome="Rex", raca="Labrador", cor="Preto", idade=5, peso=30, pedigree=True)
gato1 = Gato(nome="Mimi", raca="Siamês", cor="Branco", idade=3, peso=5)

print(cachorro1.emitirSom())
print(gato1.emitirSom())
