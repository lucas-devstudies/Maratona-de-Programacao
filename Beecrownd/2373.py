N = int(input())
quebrou = 0

for i in range(N):
    latas,copos = map(int,input().split())
    if latas>copos:
        quebrou = quebrou+copos
    
print(f"{quebrou}")