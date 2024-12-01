n = int(input())
s=0
for i in range(n):
    p = input()
    if p == '++X'or p == 'X++':
        s+=1
    else:
        s-=1 
print(s)