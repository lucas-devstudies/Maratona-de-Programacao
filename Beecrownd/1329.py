n = 1
lista = []
resultados = []

while True:
    n = int(input())
    if n == 0:
        break
    
    else:
        Jo = 0
        Ma = 0
        lista = [i for i in input().split()]
    
        for j in range(n):
            valor = int(lista[j])
            if valor == 0:
                Ma += 1
            
            else:
                Jo += 1
                   
        resultados.append('Mary won {} times and John won {} times'.format(Ma,Jo))

for a in range(len(resultados)):
    print(f'{resultados[a]}')