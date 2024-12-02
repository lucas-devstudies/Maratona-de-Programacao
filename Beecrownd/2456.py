lista = [int(i) for i in input().split()]
cresc = lista.copy()
desc = lista.copy()

cresc.sort()
desc.sort(reverse=True)

if lista == cresc:
    print('C')
    
elif lista == desc:
    print('D')
    
else:
    print('N')