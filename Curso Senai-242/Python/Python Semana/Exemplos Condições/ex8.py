idade = int(input('Digite sua idade: '))
if(idade >= 5 and idade <= 7):
    print('categoria: Infantil A')
elif(idade >= 8 and idade <= 11):
    print('categoria: Infantil B')
elif(idade >= 12 and idade <= 13):
    print('categoria: Juvenil B')
elif(idade >= 14 and idade <= 17):
    print('categoria: Juvenil B')
elif(idade <= 18):
    print('categoria: Adulto')