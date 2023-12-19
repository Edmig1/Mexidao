from personagem import personagem
class Invencivel(personagem):
    def __init__(self,nome):
        super().__init__(nome,'Invencível',1000, 1000)

    def bater(self):
        print(f'{self.nome} atacou com sua onipotência, causando:', self.dano,'de dano')
    def defender(self):
        print(f'{self.nome} não sofreu muito dano com isso')
    def esquivar(self):
        esquivou = False
        if esquivou == True:
            print(f'{self.nome} se esquivou sem sofrer danos')