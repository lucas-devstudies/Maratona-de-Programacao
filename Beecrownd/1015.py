from math import sqrt

x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())

v=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

print(f'{v:.4f}')