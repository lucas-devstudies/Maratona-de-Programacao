n = int(input())
lista = []
valor = n

for i in range(1,11):
    lista.append(valor)
    valor = valor+valor

for j in range(10):
    print(f'N[{j}] = {lista[j]}')