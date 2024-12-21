t = int(input())
for i in range(t):
    l = list([i for i in input()])
    t = []
    for i in range(len(l)-1,-1,-1):
        if l[i]=='p':
            t.append('q')
        elif l[i]=='q':
            t.append('p')
        else:
            t.append('w')
    print(''.join(t))
        
