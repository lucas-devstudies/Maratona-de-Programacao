t = int(input())
qtd = 0
maxq = 0
for i in range(t):
    a,b = map(int,input().split())
    if i==0:
        qtd -=a
        qtd +=b
        maxq += qtd
    else:
        qtd -=a
        qtd +=b
        if qtd > maxq:
            maxq = qtd
        else:
            pass
        
print(maxq)
