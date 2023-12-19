import mysql.connector
def deletar(ids):
    try:
        conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='agenda')
        cursor =conexao.cursor()
        delete = f"DELETE FROM agendatelefonica WHERE id ={ids};"
        cursor.execute(delete)
        conexao.commit()
        cursor.close()
        conexao.close()
    except mysql.connector.Error as erro:
        print(erro)
ids = int(input('Digite o id: '))
deletar(ids)
