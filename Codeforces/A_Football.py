def busca(lista):
    for i in range(len(lista)):
        if len(lista)>= i+6:
            if sum(lista[i:i+7])==0 or sum(lista[i:i+7]) == 7:
                return True
    return False

txt = list(map(int,input()))
if busca(txt)==True:
    print('YES')
else:
    print('NO')
    