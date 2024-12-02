def verificarLinhas(matriz):
    for i in range(9):
        verificar = [matriz[i][k] for k in range(9)]
        t = set(verificar)
        if len(t)!=9:
            return False
    return True

def verificarColunas(matriz):
    for i in range(9):
        verificar= [matriz[k][i] for k in range(9)]
        t = set(verificar)
        if len(t)!=9:
            return False
    return True

def verificarSub(matriz):
    caixa1 = [matriz[i][0:3] for i in range(3)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    caixa1 = [matriz[i][0:3] for i in range(3,6)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    caixa1 = [matriz[i][0:3] for i in range(6,9)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    
    
    caixa4 = [matriz[i][3:6] for i in range(3)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    caixa1 = [matriz[i][3:6] for i in range(3,6)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    caixa1 = [matriz[i][3:6] for i in range(6,9)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    
    caixa1 = [matriz[i][6:9] for i in range(3)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    caixa1 = [matriz[i][6:9] for i in range(3,6)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    caixa1 = [matriz[i][6:9] for i in range(6,9)]
    t = set(sum(caixa1,[]))
    if len(t)!=9:
        return False
    
    return True
    
    
        

n = int(input())
saidas = []
for i in  range(n):
    matriz = []
    for j in range(9):
        v = [int(i) for i in input().split()]
        matriz.append(v)
    
    if verificarColunas(matriz) == True:
        if verificarLinhas(matriz) == True:
            if verificarSub(matriz) == True:
                saidas.append('SIM')
            else:
                saidas.append('NAO')
        else:
            saidas.append('NAO')
    else:
        saidas.append('NAO')
        

for i in range(n):
    print(f'Instancia {i+1}')
    print(saidas[i],end='')
    print('\n')