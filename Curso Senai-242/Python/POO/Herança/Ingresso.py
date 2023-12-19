class ingresso():
    def __init__(self, valor):
        self.valor = valor
    def imprimevalor(self):
        print(self.valor)
class vip(ingresso):
    def __init__(self, valorvip):
        self.valor = valorvip
    def imprimevalorvip(self):
        print(self.valor)
ingresso = ingresso(25)
ingresso.imprimevalor()
novo = vip(35)
novo.imprimevalorvip()


