import math
while True:
    try:
        r1,x1,y1, r2,x2,y2 = map(int,input().split())

        dist = math.sqrt((x2-x1)**2+(y2-y1)**2)
        if r1+r2 == dist:
                print('RICO')
        else:
            if r1>= r2+dist:
                print('RICO')
            else:
                print('MORTO')
    except EOFError:
        break