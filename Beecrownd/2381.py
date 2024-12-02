m,n = map(int, input().split())
lista = []

for i in range(m):
    valor = input()
    lista.append(valor)
    valor=''
    
lista.sort()
print(lista[n-1])