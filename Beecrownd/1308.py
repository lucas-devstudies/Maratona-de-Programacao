from math import sqrt

t = int(input())
for _ in range(t):
    n = int(input())	
    v = (-1+sqrt(1+(8*n)))//2
    print(f'{v:.0f}')