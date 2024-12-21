n,m,a = map(int,input().split())
if n%a ==0:
    soma= n//a
else:
    soma= (n//a)+1
if m%a == 0:
    soma = (m//a)*soma
else:
    soma = ((m//a)+1)*soma
 
print(soma)
