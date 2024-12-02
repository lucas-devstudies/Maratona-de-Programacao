comp = 'FACE'
n = int(input())
palavras= []
cont=0
for i in range(n):
    palavra = [i for i in input().split()]
    if i==0 and palavra == comp:
        cont+=1
        comp='FACE'
        
    elif palavra[3]==comp[0] and palavra[2]==comp[1] and palavra[1]==comp[2] and palavra[0] == comp[3]:
        cont+=1
        if len(palavras)-1<=0:
            comp='FACE'
        else:
            del palavras[len(palavras)-1]
            comp = palavras[-1] 
    
    else:
        comp=f'{palavra[0]}{palavra[1]}{palavra[2]}{palavra[3]}'   
        palavras.append(comp)
print(cont)