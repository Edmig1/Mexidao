num = []
num.append(int(input('Digite um num: ')))
cont = int(input('Deseja continuar? 1-S 2-N: '))
while cont ==1:
    num.append(int(input('Digite uma num: ')))
    cont = int(input('Deseja continuar? 1-S 2-N: '))
if cont == 2:
    print(num)
    print('maior num é:',max(num),'menor num é:',min(num))
    print(sum(num))