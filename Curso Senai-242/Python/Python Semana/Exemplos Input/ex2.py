from Pacotes import operacoes
c1 = str(input('Digite 2 caractéres: '))
while(len(c1)>2 or len(c1)<2):
    print('valores inválidos')
    c1 = str(input('Digite 2 caractéres: '))
operacoes.twocarac(c1)