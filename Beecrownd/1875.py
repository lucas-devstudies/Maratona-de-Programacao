c = int(input())
for _ in range(c):
    g = b = r = 0
    p = int(input())
    for i in range(p):
        l,k = input().split()
        if l=='G' and k=='R':
            g+=1
        if l=='G' and k=='B':
            g+=2

        if l == 'B' and k == 'G':
            b+=1
        if l == 'B' and k == 'R':
            b+=2
        
        if l == 'R' and k == 'B':
            r+=1
        if l == 'R' and k == 'G':
            r+=2
    if g ==r == b:
        print('trempate')
    elif g == r and b<g or g==b and r<g or r==b and g<b:
        print('empate')
    else:
        l = [('green',g),('blue',b),('red',r)]
        t = sorted(l,key=lambda x: x[1],reverse=True)
        print(t[0][0])