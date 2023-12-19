num1 = float(input('Digite um Número: '))
num2 = float(input('Digite um Número: '))
op = str(input('Escolha uma operação entre as 4 básicas: '))
if (op.lower() == 'adição'):
    print(num1+num2)
elif (op.lower() == 'subtração'):
    print(num1-num2)
elif (op.lower() == 'divisão'):
    print(num1/num2)
elif (op.lower() == 'multiplicação'):
    print(num1*num2)
