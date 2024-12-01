def redistribuir(lista, n, r):
    dupla = []
    sozinho = []
    for i in range(n):
        #print(lista[i]//2)
        dupla.append(lista[i]//2)
        if lista[i]%2==1:
            sozinho.append(1)
    
    linhas_restantes = r-sum(dupla)
    acentos_vazios = linhas_restantes*2
    if acentos_vazios == sum(sozinho):
        r = sum(dupla)*2
    elif acentos_vazios >= (sum(sozinho))*2:
        r = (sum(dupla)*2)+sum(sozinho)
    else:
        r = (sum(dupla)*2)+(acentos_vazios-sum(sozinho))
    print(r)
    
t = int(input())
for i in range(t):
    n,r = map(int,input().split())
    lista = [int(i) for i in input().split()]
    redistribuir(lista,n,r)