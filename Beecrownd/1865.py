n = int(input())
lista = []

for i in range(n):
    nome,peso = input().split()
    if nome == 'Thor':
        lista.append('Y')
    else:
        lista.append('N')

for y in range(len(lista)):
    print(lista[y])