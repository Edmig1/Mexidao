from Pacotes import *
numero1 = int(input("Digite o primeiro número de 2 dígitos"))
numero2 = int(input("Digite o segundo número de 2 dígitos"))
while(numero1 > 99 or numero1 < 10 or numero2 > 99 or numero2 < 10):
    numero1 = int(input("Digite o primeiro número de 2 dígitos"))
    numero2 = int(input("Digite o segundo número de 2 dígitos"))
numero1 = operacoes.string(numero1)
numero2 = operacoes.string(numero2)
exibe = int(numero1[0] + numero2[1])
print(exibe)

