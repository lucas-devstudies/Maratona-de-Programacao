import math
while True:
    try:
        n=int(input())
        h,c,l = map(int,input().split())
        x = math.sqrt(c**2+h**2)
        y = (n*x)*l
        print(f'{(y/10000):.4f}')
    except EOFError:
        break