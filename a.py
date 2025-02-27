j,r = map(int,input().split())
l = [int(i) for i in input().split()]
v=[0]*j
c=0
indice_maior=0
valor_maior=0
for i in range(len(l)):
    if c==j:
        c=0
    
    v[c]+=l[i]
    if valor_maior<=v[c]:
        valor_maior=v[c]
        indice_maior=c+1
    c+=1
print(indice_maior)