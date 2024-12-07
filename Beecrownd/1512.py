from math import lcm
while True:
    n,a,b = map(int,input().split())
    if n==0:
        break
    else: 
        t1 = n//a
        t2 = n//b
        t3 = n//lcm(a,b)
        v = t1+t2-t3
        print(v)
        
