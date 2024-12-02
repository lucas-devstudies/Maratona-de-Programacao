lista = [float(i) for i in input().split()]

lista.sort()
soma = lista[1]+lista[2]+lista[3]

print(f'{soma:.1f}')