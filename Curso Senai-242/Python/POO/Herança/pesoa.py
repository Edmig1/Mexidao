class pessoa():
    def __init__(self, nome, idade, aniv):
        self.nome = nome
        self.idade = idade
        self.aniv = aniv
    def niver(self):
        self.aniv = 2023 - self.idade
        print('O atleta:',self.nome,'faz aniversário em:', self.aniv)
class atleta(pessoa):
    def __init__(self,nome, idade, aniv, peso):
        pessoa.__init__(self, nome, idade, aniv)
        self.peso = peso

    def aquecer(self):
        print(True)
class corredor(atleta):
    def __init__(self,nome, idade, aniv, peso):
        atleta.__init__(self, nome, idade, aniv, peso)
    def correr(self):
        print(True)
class nadador(atleta):
    def __init__(self,nome, idade, aniv, peso):
        atleta.__init__(self, nome, idade, aniv, peso)
    def nada(self):
        print(True)
class Ciclista(atleta):
    def __init__(self,nome, idade, aniv, peso):
        atleta.__init__(self, nome, idade, aniv, peso)
    def pedalar(self):
        print(True)
class Triatleta(nadador, corredor, Ciclista):
    def __init__(self,nome, idade, aniv, peso):
        atleta.__init__(self, nome, idade, aniv, peso)
        nadador.nada(self)
        corredor.correr(self)
        Ciclista.pedalar(self)
    def maratona(self):
        print(True)
pes = Triatleta('luiz',19, 2004, 70)
pes.maratona()
pes.niver()