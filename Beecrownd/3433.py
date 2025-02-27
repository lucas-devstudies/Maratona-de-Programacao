n = int(input())
maria = joao = 0
cartas = {1:4,2:4,3:4,5:4,6:4,7:4,8:4,9:4,10:4,11:4,12:4,13:4}
for i in range(2):
    x,y = map(int,input().split())
    cartas[x]-=1
    cartas[y]-=1
    if i==0:
        joao = x+y
    else:
        maria = x+y
l = [int(i) for i in input().split()]
for i in range(n):
    cartas[l[i]]-=1
    if l[i]>=10:
        maria+=10
        joao+=10
    else:
        joao+=l[i]
        maria+=l[i]

if maria>23:
    print(-1)
elif joao>23:
    print(0)
else:
    x = 23 - maria
    print(x)