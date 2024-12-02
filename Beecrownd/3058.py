N = int(input())
menor = 0
for i in range(N):
    p, g = map(float,input().split())
    kg = p * 1000/g

    if i == 0:
        menor = kg
    
    elif menor>kg:
        menor = kg
    
print('{:.2f}'.format(menor))