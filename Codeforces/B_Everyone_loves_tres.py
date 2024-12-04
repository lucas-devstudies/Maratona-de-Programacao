t = int(input())
for i in range(t):
    n = int(input())
    if n == 1 or n == 3:
        print(-1)
    else:
        if n%2==0:
            r = []
            for i in range(n-1,-1,-1):
                if i==0 or i==1:
                    r.append('6')
                else:
                    r.append('3')
        else:
            r = []
            for i in range(n-1,-1,-1):
                if i==0 or i==1 or i == 3:
                    r.append('6')
                else:
                    r.append('3')
        print(''.join(r))
