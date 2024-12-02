from math import factorial
while True:
    try:
        m,n = map(int,input().split())
        soma = factorial(m)+factorial(n)
        print(soma)
    except EOFError:
        break