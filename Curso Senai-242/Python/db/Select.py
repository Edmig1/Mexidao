import mysql.connector
def selecionar(ids):
    try:
        conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='agenda')
        cursor = conexao.cursor()
        select = f"SELECT * FROM agendatelefonica WHERE id ={ids};"
        cursor.execute(select)
        print(cursor)
        for (id, nome, telefone, email, endereco) in cursor:
                print(f" Id: '{id}',\n Nome: '{nome}',\n Email: '{email}',\n endereco: '{endereco}'")
        cursor.close()
        conexao.close()
    except mysql.connector.Error as erro:
        print(erro)
ids = int(input('Digite o id: '))
selecionar(ids)
