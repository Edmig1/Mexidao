def operacao():
    t1 = (input("Digite a primeira medida de temperatura (use C, F ou K): "))
    n1 = float(input("Digite ao primeiro número de temperatura: "))
    t2 = (input("Digite a segunda medida de temperatura (use C, F ou K): "))
    if(t1 == "C" and t2 == "F"):
        ctof = lambda n1: n1*1.8 +32
        print(ctof(n1))

    if(t1 == "F" and t2 == "C"):
        ctof = lambda n1: (n1 - 32)/1.8
        print(ctof(n1))

    if(t1 == "C" and t2 == "K"):
        ctof = lambda n1: n1 +273.15
        print(ctof(n1))

    if(t1 == "C" and t2 == "K"):
        ctof = lambda n1: n1 +273.15
        print(ctof(n1))

    if(t1 == "F" and t2 == "K"):
        ctof = lambda n1: (n1 +459.67)/1.8
        print(ctof(n1))
    if (t1 == "K" and t2 == "F"):
        ctof = lambda n1: n1*1.8 - 459.67
        print(ctof(n1))
    while(t1 not in "CFK" and t2 not in "CFK"):
        operacao()
operacao()