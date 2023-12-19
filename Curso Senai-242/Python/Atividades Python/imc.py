a = float(input("Informe sua altura em Metros: "))
p = float (input("Informe o seu Peso em Kg: "))



imc = p / (a ** 2)

if imc < 18.5:
    print ("Magreza, seu imc é: " + str(imc))

elif 18.5 <= imc < 24.9:
    print("Normal, seu imc é: "+ str(imc))

elif 25 <= imc < 29.9:
    print("Sobrepeso, seu imc é: " + str(imc))

elif 30 <= imc < 39.9:
    print("Obesidade, seu imc é: " + str(imc))

elif imc > 40:
    print("Obesidade grave, seu imc é: " + str(imc))


