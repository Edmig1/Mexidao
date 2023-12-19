class cc():
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
    def mult(self):
        print(self.numero*self.saldo)
cc = cc(10,0)
cc.mult()
