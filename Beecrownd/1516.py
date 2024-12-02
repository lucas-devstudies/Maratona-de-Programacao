while True:
    try:
        lista = []
        n,m = map(int,input().split())
        if n==0 and m == 0:
            break
        else:
            for i in range(n):
                l = []
                v = [i for i in input()]
                for t in v:
                    l.append(t)
                lista.append(l)

            a,b = map(int,input().split())

            divA = a//n
            divB = b//m

            for i in range(n):
                mensagem=''
                for j in range(m):
                    for d in range(divB):
                        mensagem += f'{lista[i][j]}'
                
                for t in range(divA):
                    print(mensagem)

            print()
    except EOFError:
        break