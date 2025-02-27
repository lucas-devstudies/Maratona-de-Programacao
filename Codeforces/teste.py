from math import sqrt
try:
    a,b,c = map(float, input().split())

    delta = (b*b)-(4*a*c)
    r1 = (-b+sqrt(delta))/(2*a)
    r2 = (-b-sqrt(delta))/(2*a)
       
    r1 = f'{r1:.5f}'
    r2 = f'{r2:.5f}'
    print(f'R1 = {r1}')
    print(f'R2 = {r2}')
except:
	print("Impossivel calcular")