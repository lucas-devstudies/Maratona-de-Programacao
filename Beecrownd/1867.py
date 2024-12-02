def soma(texto):
    texto = str(texto)
    valor = 0
    for t in texto:
        valor = int(t) + valor
        
    if valor>=0 and valor<=9:
        return int(valor)
       
    else:
        return soma(valor)
            
while True:
    n,m = map(int, input().split())
    v1 = soma(n)
    v2 = soma(m)
    if n == 0 and m == 0:
        break
    
    elif v1>v2:
        print(1)
        
    elif v2>v1:
        print(2)
        
    else:
        print(0)
        