produtos = ["doritos", "ruffles", "fandangos"]
estoque = [10, 15, 17]
min_estoque = [5, 7, 9]

for i in range(0, len(produtos)):
    print(f"produto: {produtos [i]}, o estoque é: {estoque [i]}, o estoque mínimo é: {min_estoque[i]}")


def add ():
    inp = input("deseja cadastrar um novo produto?: ")
    if(inp == "sim".lower()):
        prod = input("Produto: ")
        estq = input(" o estoque é: ")
        min_e = input(" o estoque mínimo é: ")
        produtos.append(prod)
        estoque.append(estq)
        min_estoque.append(min_e)
        for i in range(0, len(produtos)):
            print(f"produto: {produtos [i]}, o estoque é: {estoque [i]}, o estoque mínimo é: {min_estoque[i]}")
    elif(inp == "não".lower()):
        inp2 = input("tem certeza disso?: ")
        if(inp2 == "não".lower()):
            add()
        if(inp2 == "sim".lower()):
            return
        
add()

for num in range(0, len(estoque)):
    if(estoque[num] <= min_estoque[num]):
        print(f"produto: {produtos [num]} está com o estoque mínimo")

lista = []
for num in range(len(produtos)):
    lista.append([produtos[num], estoque[num], min_estoque[num]])

def deletar():

    dele = input("Deseja Apagar algum produto? ")
    if(dele == "sim"):
        remove = input("Qual produto deseja apagar? ")
        deletado = False
        for num in range(len(produtos)):
            if(remove == produtos[num].lower()):
                produtos.pop(num)
                estoque.pop(num)
                min_estoque.pop(num)
                deletado = True
                print(f"Os produtos agora são: {produtos} {estoque} {min_estoque}")
                break
        if(deletado == False):
            print("Produto Não encontrado")
            deletar()
deletar()




