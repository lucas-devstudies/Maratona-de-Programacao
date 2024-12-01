n,k= map(int,input().split())
l = [int(i) for i in input().split()]
 
c = 0
for i in range(len(l)):
    if l[i]>=l[k-1] and l[i]>0:
        c+=1
print(c)