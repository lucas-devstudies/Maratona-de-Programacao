n = int(input())
s=0
for i in range(n):
    p1,p2,p3 =  map(int,input().split())
    soma=p1+p2+p3
    if soma>=2:
        s +=1
        
print(s)
