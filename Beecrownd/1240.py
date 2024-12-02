n=int(input())
for i in range(n):
    try:
        txt,li=input().split()
        encaixa = True
        c=0
        for j in range(-1,((len(li)*-1)-1),-1):
            if c==len(li):
                break
            elif txt[j]!=li[j]:
                encaixa = False
            else:
                c+=1
        if encaixa == True:
            print('encaixa')
        else: 
            print('nao encaixa')
    except:
        print('nao encaixa')