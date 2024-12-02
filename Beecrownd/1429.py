import math
n=1
while True:
    n = int(input())
    v=0
    if n==0:
        break
    else:
        l = str(n)
        cont=1
        for i in range(len(l),0,-1):
            t =int(l[i-1])*math.factorial((cont))
            v+= t
            cont+=1
        print(v)