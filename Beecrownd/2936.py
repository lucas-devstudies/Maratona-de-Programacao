lista = []
for i in range(5):
    valor = int(input())
    lista.append(valor)

soma = 225
for j in range(5):
    if j == 0:
        soma += (lista[j]*300)
        
    elif j == 1:
        soma += (lista[j]*1500)
    
    elif j == 2:
        soma += (lista[j]*600)
    
    elif j == 3:
        soma += (lista[j]*1000)
        
    elif j == 4:
        soma += (lista[j]*150)
        
print(soma)