import math 
cont=0
while True:
    try:
        r,w,l = map(int,input().split())
        area = math.sqrt(((w/2)**2)+((l/2)**2))
        cont+=1
        if area<=r:
            print(f'Pizza {cont} fits on the table.')
        else:
            print(f'Pizza {cont} does not fit on the table.')
    except ValueError:
        break