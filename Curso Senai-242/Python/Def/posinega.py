def posi(pgt):
    if(pgt < 0):
        print("Número Negativo")
    elif(pgt == 0):
        print("Número é 0")
    else:
        print("Número Positivo")
pgt = int (input("Digite um número qualquer: "))
posi(pgt)