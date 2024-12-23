t = int(input())
for _ in range(t):
    n,a,b,c = map(int,input().split())
    v = a+b+c
    t = [a,a+b,c+a+b]
    h = (n//v)*3
    j = n%v
    if j==0:
        print(h)
    else:
        c=0
        for i in range(3):
            c+=1
            if j<=t[i]:
                print(h+c)
                break