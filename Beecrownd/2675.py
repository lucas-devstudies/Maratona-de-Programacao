while True:
    try:
        monte = [] 
        roubo = []
        soma=0
        n = int(input())
        lista = [int(i) for i in input().split()]
        for i in range(n):
            if i==0:
                monte.append(lista[i])
            else:
                for j in range(len(monte)):
                    if monte[-1] > lista[i]:
                        roubo.append(monte[-1])
                        del monte[-1]
                        
                    else:
                        continue
                monte.append(lista[i])
                    
        
        for miga in roubo:
            soma+=miga
        print(soma)
    except EOFError:
        break