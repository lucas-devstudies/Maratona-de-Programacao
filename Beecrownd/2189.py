lista = []
resultados = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        lista = [i for i in input().split()]
    
        for j in range(len(lista)):
            if int(lista[j]) == j+1:
                resultados.append(j+1)
    
for r in range(len(resultados)):
    print(f'Teste {r+1}')
    print(f'{resultados[r]}')
    print()