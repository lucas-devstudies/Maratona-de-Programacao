n = int(input())
l = [int(i) for i in input().split()]
l.sort(reverse=True)
d=[]
for i in range(n):
    if i==0:
        d.append(l[i])
    else:
        if i+1!=n and i%2==0:
            l[i],l[i+1]=l[i+1],l[i]
            d.append(l[i])
        else:
            d.append(l[i])
print(d)