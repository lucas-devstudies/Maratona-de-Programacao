t = int(input())
for i in range(t):
    l = []
    v1 = []
    v2 = []
    n = int(input())
    lista = [int(i) for i in input().split()]	
    for i in range(0,n):
        if i%2 == 0:
            v1.append(lista[i])
        else:
            v2.append(lista[i])    
    l.append(v1.copy())
    l.append(v2.copy())
    
    t1 = sum(lista)//n
    if sum(lista)%n!=0:
        print('No')
    else:
        if (sum(l[0])/len(l[0]))==float(t1):
            if sum(l[1])/len(l[1])==float(t1):
                print('YES')
            else:
                print('No')
        else:
            print('No') 
