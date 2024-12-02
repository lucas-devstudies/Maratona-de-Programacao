maiores = []
maiorRepeticao = 0
n = int(input())
vetor = [int(i) for i in input().split()]
for i in range(n):
    v = vetor.count(vetor[i])
    if maiorRepeticao<v:
        maiores.clear()
        maiorRepeticao = v
        maiores.append(vetor[i])
    
    elif maiorRepeticao == v:
        maiores.append(vetor[i])
    
maxV=0
for m in range(len(maiores)):
    if m == 0:
        maxV = maiores[m]
    elif maxV< maiores[m]:
      maxV = maiores[m]
      
print(maxV)