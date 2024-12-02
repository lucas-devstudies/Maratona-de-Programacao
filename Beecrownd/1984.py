n = int(input())
valor = str(n)
lista = []
texto = ''

for i in range(len(valor)):
    lista.append(valor[i])

for j in range(len(valor)-1,-1,-1):
    texto = texto + lista[j]
    
print(texto)