nota1 = float (input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if (media >= 7):
    print("Lansou a braba fdp, sua média foi " + str(media))
elif (media >= 3):
    print("Recuperacao, sua nota foi: " + str(media))
else:
    print("Desista dos seus sonhos e morra, sua média foi: " + str(media))