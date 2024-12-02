pi = 3.1415
r,l = map(int,input().split())
v = (4/3) * pi*(r**3)
print(f'{(l//v):.0f}')