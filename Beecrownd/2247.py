n = 1
cont = 1
joaozinho = 0
zezinho = 0
saidas = []

n = int(input())
while n != 0:
    saidas.append(f'Teste {cont}')
    joaozinho = 0
    diferenca = 0
    zezinho = 0
    
    for i in range(n):
        j,z = map(int,input().split())
        joaozinho += j
        zezinho += z
        diferenca = joaozinho - zezinho
        saidas.append(diferenca)

    cont += 1
    n = int(input())
    saidas.append('')
    
for j in range(len(saidas)):
    print(saidas[j])