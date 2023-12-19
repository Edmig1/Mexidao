idade = int(input('Digite sua idade: '))
while idade < 1:
    idade = int(input('Digite sua idade: '))
    print('Você não pode ter menos de 1 Ano')

if idade < 18:
    print('Você é menor de idade')
else:
    print('Você é maior de idade')