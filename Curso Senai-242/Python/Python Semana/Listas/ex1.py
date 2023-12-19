import numpy
num = []
num.append(int(input('Digite um num: ')))
cont = int(input('Deseja continuar? 1-S 2-N: '))
while cont ==1:
    num.append(int(input('Digite uma num: ')))
    cont = int(input('Deseja continuar? 1-S 2-N: '))
if cont == 2:
    maior = (max(num))
    menor = (min(num))
    print(num)
    print('maior num é:',maior,'menor num é:', menor)
print(numpy.prod(num))