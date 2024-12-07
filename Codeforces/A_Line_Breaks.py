t = int(input())
for i in range(t):
    t=s=0
    leitura = True
    n,m = map(int,input().split())
    for i in range(n):
        word = input()
        if (t+len(word))<=m and leitura == True:
            t+=len(word)
            s+=1
        else:
            leitura = False
    print(s)
