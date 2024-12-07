n = int(input())

notas = [100,50,20,10,5,2,1]
print(n)
for i in range(len(notas)):
    t = n//notas[i]
    n-= t*notas[i]
    m = f'{t} nota(s) de R$ {notas[i]},00'
    
    print(m)
