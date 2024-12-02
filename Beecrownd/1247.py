import math
while True:
    try:
        d, vf, vg = map(int,input().split())
        D = 12
        c = math.sqrt(pow(d,2)+pow(D,2))
        
        if (c/vg)<=(D/vf):
            print('S')
        else:
            print('N')
    except EOFError:
        break