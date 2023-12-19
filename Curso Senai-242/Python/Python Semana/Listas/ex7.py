num = []
while True:
    esc = int(input('Adicione um número: '))
    for i in num:
        if esc in num:
            num.remove(i)
    num.append(esc)
    sair = str(input('Deseja sair?[S/N]: '))
    if sair == 's':
        break
print (num)