
p1 = [6, 9, 7, 10, 8, 8, 4]
p2 = [8, 10, 6, 9, 10, 9, 2]
mediap1 = sum(p1)/len(p1)
mediap2 = sum(p2)/len(p2)
if (mediap1 > mediap2):
    print('prova 1 melhor, a média foi: '  +str(round(mediap1, 1)))
if (mediap2 > mediap1):
    print('prova 2 melhor, a média foi: ' +str(round(mediap2, 1)))

