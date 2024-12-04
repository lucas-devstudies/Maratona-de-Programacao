n = int(input())
l = [int(i) for i in input().split()]
c=0
for i in range(n):
    if ((l[i])-1)==0:
        pass
    else:
        c+=l[i]-1

print(c)
