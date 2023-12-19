import mysql.connector
def atualizar(nome, telefone, email, endereco,ids):
    try:
        conexao = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='agenda')
        cursor =conexao.cursor()
        update = f"UPDATE `agendatelefonica` SET `nome` = '{nome}' ,telefone = '{telefone}', email = '{email}',endereco='{endereco}' WHERE `agendatelefonica`.`id` = '{ids}';"
        cursor.execute(update)
        conexao.commit()
        cursor.close()
        conexao.close()
    except mysql.connector.Error as erro:
        print(erro)
nome = input('Digite o Nome: ')
telefone = input('Digite o Telefone: ')
email = input('Digite o Email: ')
endereco = input('Digite o Endereco: ')
ids = int(input('Digite o id: '))
atualizar(nome,telefone,email,endereco,ids)
