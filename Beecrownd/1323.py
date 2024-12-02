n=1
while True:
    n = int(input())
    v=0
    if n==1:
        print(n)
    elif n==0:
        break
    else:
        while n>0:
            v +=(n*n)
            n-=1
        print(v)