v = float(input("Digite o valor do produto: "))
t = float(input("Digite a taxa: "))
T= float(input("Digite o tempo em meses: "))

p= v +(v*(t/100) *T)

print("o valor da prestação é: " + str(p))
