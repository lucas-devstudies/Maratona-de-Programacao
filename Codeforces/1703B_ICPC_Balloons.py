def busca(n,l):
    s = 0
    repetidos = []
    for i in range(n):
        if l[i] in repetidos:
            s += 1
        else:
            s+=2
            repetidos.append(l[i])	
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    l = list(input())
    print(busca(n,l))