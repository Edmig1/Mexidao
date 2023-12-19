import mysql.connector
def inserir(nome, telefone, email, endereco):
    try:
        conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='agenda')
        cursor =conexao.cursor()
        inserir = f"INSERT INTO agendatelefonica (nome,telefone,email,endereco) VALUES('{nome}','{telefone}','{email}','{endereco}');"
        cursor.execute(inserir)
        conexao.commit()
        cursor.close()
        conexao.close()
    except mysql.connector.Error as erro:
        print('erro')
nome = input('Digite o Nome: ')
telefone = input('Digite o Telefone: ')
email = input('Digite o Email: ')
endereco = input('Digite o Endereco: ')
inserir(nome,telefone,email,endereco)

