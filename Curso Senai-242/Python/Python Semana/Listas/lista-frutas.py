fruta = []
fruta.append(str(input('Digite uma fruta: ')))
delet = int(input('Quer deletar uma fruta? 1-S 2-N: '))
if delet == 1:
    delet2 = str(input('Digite o nome da fruta: '))
    if delet2 in fruta:
        fruta.remove(delet2)
    else:
        print('Fruta Não Encontrada')
cont = int(input('Deseja continuar? 1-S 2-N: '))
while cont ==1:
    fruta.append(str(input('Digite uma fruta: ')))
    delet = int(input('Quer deletar uma fruta? 1-S 2-N: '))
    if delet == 1:
        delet2 = str(input('Digite o nome da fruta: '))
        if delet2 in fruta:
            fruta.remove(delet2)
        else:
            print('Fruta Não encontrada')
    cont = int(input('Deseja continuar? 1-S 2-N: '))
if cont == 2:
    maior = (max(fruta,key=len))
    menor = (min(fruta,key=len))
    print(fruta)
    print('maior fruta é:',maior,'menor fruta é:', menor)

#Append adiciona no final da lista, E Insert coloca na posição que eu definir,
# nesse caso ele está colocando a fruta na position 0
#Fruta.remove apaga uma fruta pelo nome, pop apaga pela posição e del deleta a lista toda.