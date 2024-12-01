t = int(input())
for k in range(t):
    n = int(input())
    matriz = []
    for i in range(n):
        matriz.append([int(i) for i in input().split()])
    
    cont=0
    for i in range(n):
        for j in range(n):
            if matriz[i][j]<0:
                q = -matriz[i][j]
                cont+= q
                try:
                    for t in range(n):
                        matriz[i+t][j+t] += q
                except:
                    pass
            else:
                pass
    print(cont)