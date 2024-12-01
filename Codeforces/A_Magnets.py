n = int(input())
l=[]
for i in range(n):
    l.append(input())
 
c=1
for i in range(len(l)):
    if i!=len(l)-1:
        if l[i]!=l[i+1]:
           c+=1
print(c)