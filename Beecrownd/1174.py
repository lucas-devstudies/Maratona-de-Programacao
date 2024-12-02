lista = []
for i in range(100):
    valor = float(input())
    lista.append(valor)
    
for j in range(100):
    if lista[j] <= 10:
        print(f'A[{j}] = {lista[j]:.1f}')