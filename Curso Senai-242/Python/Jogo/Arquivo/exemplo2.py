arquivo = open("teste.html", "r")
nome=(arquivo.read())
arquivo.close()
nome =nome.upper()
arquivo = open("teste.html", "a")
arquivo.write(nome)
arquivo.close()