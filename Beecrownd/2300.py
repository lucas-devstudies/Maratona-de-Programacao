def bfs(lista,origem,e):
    visitados = [0]*(e+1)
    f = [origem]
    
    visitados[origem] = 1
    while len(f)!=0:
        a = f[0]
        del f[0]
        
        for v in lista[a]:
            if visitados[v] ==1:
                continue
            
            f.append(v)
            visitados[v]=1
            
    return visitados.count(0)==1
            
    
cont=1
while True:
    e, l = map(int,input().split())
    if e == 0:
        break
    
    lista = [[] for i in range(e+1)]
    for i in range(l):
        a,b = map(int,input().split())
        lista[a].append(b)
        lista[b].append(a)
    
    print(f'Teste {cont}')
    cont+=1
    
    if bfs(lista,a,e):
        print(f'normal')
        
    else:
        print(f'falha')

    print()