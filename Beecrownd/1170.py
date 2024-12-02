def qtd(dias,kg):
    soma = kg/2 
    if soma>1:
       dias=dias+1
       qtd(dias,soma)
    else: 
       print(f'{dias+1} dias')
       
n = int(input())
for i in range(n):
    kg = float(input())
    qtd(0,kg)