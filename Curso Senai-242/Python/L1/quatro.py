n= int(input("Digite um número inteiro de três dígitos: "))

c = n // 100
d = (n % 100) // 10
u = n % 10

print("centena é: " +str(c))
print("dezena é: " +str(d))
print("unidade é: " +str(u))
