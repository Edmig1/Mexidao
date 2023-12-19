v = float(input('Digite o valor: '))
p = int(input('Digite a quantidade de parcelas: '))
div = v/p
print('o valor da parcela foi', div)
if div>500:
    print('Você não conseguirá pagar esse valor por parcela')