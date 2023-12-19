q= int(input("Digite quantas fitas vocês possuem na loja: "))
v = float(input("Digite o valor das fitas: "))

la= q/3

print("O lucro com aluguéis é: " + str((la*v)*12))

lat= la/10

print("O lucro com atrasos é: " + str(lat*(v/10)))

re= q*0.02

re2= re +q +(q*0.1)

print("A quantidade final de fitas foi:" + str(re2))

