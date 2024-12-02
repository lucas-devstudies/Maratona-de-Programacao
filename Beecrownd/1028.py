def mdc(a,b):
    while b!=0:
        temp=b
        b = a % b
        a = temp
        
    return a
        
n=int(input())
for num in range(n):
    f1,f2 = map(int,input().split())
    maior = mdc(f1,f2)
    print(maior)