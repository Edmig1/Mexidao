from personagem import personagem
class Guerreiro(personagem):

    def __init__(self,nome):
        super().__init__(nome,'Guerreiro',200,17)
    def bater(self):
        print(f'{self.nome} Desferiu um poderoso ataque com sua espada, causando:', self.dano,'de dano')
    def defender(self):
        print(f'{self.nome} se defendeu com seu escudo, porém sofreu:', self.dano,'de dano')
    def esquivar(self):
        esquivou = False
        if esquivou == True:
            print(f'{self.nome} se esquivou sem sofrer danos')