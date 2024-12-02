passou = False
falha = None
while True:
    try:
        n = int(input())
        if passou==False:
            passou = True
            anterior = n
        else:
            if anterior<n:
                anterior=n

            else:
                if falha==None:
                    falha = anterior+1
                anterior=n
    except EOFError:
        if falha==None:
            falha=anterior+1
        print(falha)
        break  