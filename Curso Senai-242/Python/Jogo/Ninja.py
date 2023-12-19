from personagem import personagem
class Ninja(personagem):

    def __init__(self,nome):
        super().__init__(nome,'Ninja',170,21)
    def bater(self):
        print(f'{self.nome} usou sua destreza para atacar com sua shuriken, causando:', self.dano,'de dano')
    def defender(self):
        print(f'{self.nome} tentou se esquivar, mas sofreu:', self.dano,'de dano')
    def esquivar(self):
        esquivou = False
        if esquivou == True:
            print(f'{self.nome} se esquivou sem sofrer danos')