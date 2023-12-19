class func():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    def dnome(self):
        print("O nome do funcionário é:",self.nome)
    def sal(self):
        print("O salario do funcionário é:",self.salario)
nomef = str(input('Diga o Nome: '))
salf = str(input('Diga o Salário: '))
fun = func(nomef,salf)
fun.dnome()
fun.sal()