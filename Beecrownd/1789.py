lista = []
listaMaior = []
while True:
    try:
        n = int(input())
        lista = [int(i) for i in input().split()]
        lista.sort()
        if lista[len(lista)-1] <10:
            listaMaior.append(1)
        elif lista[len(lista)-1] > 10 and lista[len(lista)-1]<20:
            listaMaior.append(2)
        
        else:
            listaMaior.append(3)
    except EOFError:
        break
    
for j in range(len(listaMaior)):
    print(listaMaior[j])