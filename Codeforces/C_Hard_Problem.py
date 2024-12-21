t = int(input())
for i in range(t):
    m,a,b,c = map(int,input().split())
    if a >=m:
        fileira1 = m
    else:
        fileira1 = a        
    if b >=m:
        fileira2 = m
    else:
        fileira2 = b
    s = m*2 -(fileira1+fileira2)
    if c >=s:
        fileira3 = s
    else:
        fileira3 = c
    print(fileira1+fileira2+fileira3)
