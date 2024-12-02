import math
pi = 3.1415926535897 
while True:
    try:
        a,b,c = map(int,input().split())
        
        p = (a+b+c)/2
        
        Av = math.sqrt((p*(p-a)*(p-b)*(p-c)))
        r = Av/p
        
        Ar = pi*(r**2)
        Av = Av-Ar
        As = (((a * b * c / (4 * (Av+Ar)))**2)*pi)-(Av+Ar)
        
        print(f'{As:.4f} {Av:.4f} {Ar:.4f}')
        
    except EOFError:
        break