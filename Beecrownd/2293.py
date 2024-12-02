n,m = map(int,input().split())
matriz =[[int(i)*0 for i in range(n)] for i in range(m)]
somaMaior = 0
for i in range(n):
    if i == 0:
        matriz.clear()
    valores = [int(i) for i in input().split()]
    matriz.append(valores)

for i in range(n):
    soma=0
    for j in range(m):
        soma=soma+matriz[i][j]
    
    if somaMaior<soma:
        somaMaior = soma

for c in range(m):
    soma = 0
    for i in range(n):
        soma = soma + matriz[i][c]
    
    if somaMaior<soma:
        somaMaior = soma
print(somaMaior)