n = int(input())
menor = 0
p = 0

lista = [i for i in input().split()]

for j in range(n):
    valor = int(lista[j])
    if j == 0:
        menor = valor
        p = j
        
    elif menor> valor:
        menor = valor
        p = j

print(f'Menor valor: {menor}')
print(f'Posicao: {p}')