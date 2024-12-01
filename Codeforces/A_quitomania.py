n = int(input())
for i in range(n):
    t = True
    v = int(input())
    lista = [int(i) for i in input().split()]
    for i in range(v-1):
        if lista[i] - lista[i+1] == 5:
            pass
        elif lista[i] - lista[i+1] == 7:
            pass
        elif lista[i+1]-lista[i] == 5: 
            pass
        elif lista[i+1]-lista[i] ==7:
            pass
        else:
            t=False
            break
    if t==True:
        print('YES')
    else:
        print('NO')