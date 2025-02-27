c=0
for _ in range(5):
    linha = [int(i) for i in input().split()]
    if sum(linha)!=1:
        c+=1
    else:
        c+=1
        v = linha.index(1)
        h = c
        passou = True
print(abs((v+1)-3)+abs(h-3))