lista = []
while True:
    try:
        valor = int(input())
        
        if valor == 0:
            lista.append('vai ter copa!')
            
        else:
            lista.append('vai ter duas!')
    except EOFError:
        break
    
for j in range(len(lista)):
    print(lista[j])