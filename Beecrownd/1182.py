n = int(input())
op = input()
soma = 0
lista = []
matriz = [[i for i in range(12)] for i in range(12)]
for i in range(12):
    for j in range(12):
        v = float(input())
        matriz[i][j]=v
if op == 'S':
    for i in range(12):
        soma = soma+matriz[i][n]
    print(f'{(soma):.1f}')

elif op == 'M':
    for i in range(12):
        soma = soma+matriz[i][n]
    print(f'{(soma/12):.1f}')