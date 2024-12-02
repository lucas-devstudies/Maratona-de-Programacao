def buscar_meio(parede):
    k=0
    for i in range(2,9,2):
        k+=2
        for j in range(1,k,2):
            meio = (parede[i-2][j-1]-((parede[i][j-1])+(parede[i][j+1])))/2
            parede[i][j] = int(meio)
            
    return parede

def buscar_cantos(parede):
    k = 0
    for i in range(1,9,2):
        k+=2
        for j in range(k):
            parede[i][j]=(parede[i+1][j]+parede[i+1][j+1])

    return parede

n = int(input())
for i in range(n):
    parede = []
    for k in range(5):
        v = [int(i) for i in input().split()]
        lista,lista2 = [],[]
        for t in range(len(v)):
            lista.append(0)
            lista.append(0)

        lista2.append(v[0])
        for t in range(1,len(v)):
            lista2.append(0)
            lista2.append(v[t])
        
        parede.append(lista2)
        if k!=4:
            parede.append(lista)
    
    buscar_meio(parede)
    buscar_cantos(parede)
    for i in parede:
        m = ''
        for j in i:
            m = m + f'{j} '
        print(m.strip())