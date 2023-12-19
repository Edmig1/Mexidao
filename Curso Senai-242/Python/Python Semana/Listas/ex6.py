num = []
num.append(int(input('Digite um num: ')))
cont = int(input('Deseja continuar? 1-S 2-N: '))
while cont ==1:
    num.append(int(input('Digite uma num: ')))
    cont = int(input('Deseja continuar? 1-S 2-N: '))
if cont == 2:
    num.sort(reverse=True)
    print(num)
    print('A lista tem:',len(num),'Números')
    if 5 in num:
        print('O número 5 está na lista')