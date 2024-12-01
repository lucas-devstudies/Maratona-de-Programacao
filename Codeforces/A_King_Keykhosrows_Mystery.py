t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    k=a 
    l=b
    while True:
        if l==k:
            print(k)
            break
        else:
            if l>k:
                k+=a
            else:
                l+=b
                pass