n = int(input())
fila = [int(i) for i in input().split()]
m = int(input())
removidos = [int(i) for i in input().split()]
mensagem = ''

for i in range(len(removidos)):
    fila.remove(removidos[i])

for i in range(len(fila)):
    if i==0:
        mensagem = str(fila[i])
    else:
        mensagem = mensagem + ' ' + str(fila[i])

print(mensagem)