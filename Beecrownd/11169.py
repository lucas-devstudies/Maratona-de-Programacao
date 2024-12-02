from math import pow

n = int(input())
for i in range(n):
    x = int(input())
    for i in range(x+1):
        if i==0:
            v=1
        elif i==1:
            v=2
        else:
            v=v*2
        
    print(f'{int((v/12)/1000)} kg')    