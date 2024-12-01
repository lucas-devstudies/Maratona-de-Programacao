t = int(input())
for i in range(t):
    c=0
    n,k = map(int,input().split())
    l = [int(i) for i in input().split()]
    e = 0
    for i in range(n):
        if l[i]==0 and e>0:
            e+=-1
            c+=1
        else:
            if l[i]>=k:
                e+=l[i]
            else:
                pass
    print(c)