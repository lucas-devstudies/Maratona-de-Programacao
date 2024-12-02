n = int(input())
t = input()
matriz = []

for i in range(12):
    lista = [int(i)*0 for i in range(12)]
    for j in range(12):
        v=float(input())
        lista[j] = v
        
    clone=lista.copy()
    matriz.append(clone)
    lista.clear()
    
soma=0
for i in range(12):
    soma = matriz[n][i]+soma

if t=='S':
    print(f'{soma:.1f}')
    
else:
    print(f'{(soma/12):.1f}')
