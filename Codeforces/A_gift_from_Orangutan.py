t = int(input())
for i in range(t):
    n = int(input())
    lista = [int(i) for i in input().split()]
    maxL = max(lista)
    minL = min(lista)
    soma=0
    for j in range(len(lista)):
        if j==0:
            continue
        else:
            soma += (maxL-minL)
    
    print(soma)