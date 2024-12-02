n = int(input())
cubo=[]

for i in range(n):
    lista = [int(i) for i in input().split()]
    cubo.append(lista)

soma1 = sum(cubo[0])
soma2 = sum(cubo[1])
soma3 = sum(cubo[2])

if soma1 == soma2 == soma3:
    real = soma1

elif soma2 == soma1:
    real = soma1

elif soma1 == soma3:
    real = soma3

else:
    real = soma2

x = p = 0
for i in range(n):
    x = sum(cubo[i])
    if x == real:
        continue
    else:
        Imatriz = i
        break
    
for j in range(n):
    p = [cubo[k][j] for k in range(n)]
    p = sum(p)
    if p == real:
        continue
    else:
        Jmatriz = j
        break

t = p - real
total = cubo[Imatriz][Jmatriz] - t

print(f'{total} {cubo[Imatriz][Jmatriz]}')