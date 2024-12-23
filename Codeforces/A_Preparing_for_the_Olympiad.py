t = int(input())
for _ in range(t):
    n = int(input())
    #criar lista de 1 a n
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    m = ''
    somaA=somaB=0
    for i in range(n):
        if i<n-1:
            if a[i]>b[i+1]:
                somaA+=a[i]
                somaB+=b[i+1]
        else:
            somaA+=a[i]
    print(somaA-somaB)