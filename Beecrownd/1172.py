lista = []
for i in range(10):
    valor = int(input())
    if valor<=0:
        lista.append(1)
    else:
        lista.append(valor)
    
for j in range(10):
    print(f'X[{j}] = {lista[j]}')