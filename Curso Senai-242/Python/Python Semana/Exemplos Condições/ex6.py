t1 = str(input('Digite o primeiro time: '))
t2 = str(input('Digite o segundo time : '))
g1 = str(input('Digite o placar: '))
g1 = g1.split('x')
if(int(g1[0]) > int(g1[1])):
    print(f'{t1} ganhou')
elif (int(g1[1]) > int(g1[0])):
    print(f'{t2} ganhou')
elif (int(g1[0]) == int(g1[1])):
    print(f'{t1} e {t2} empataram')