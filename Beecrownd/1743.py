n1,n2,n3,n4,n5 = map(int,input().split())
m1,m2,m3,m4,m5 = map(int,input().split())

if n1 != m1 and n2 != m2 and m3 != n3 and n4 != m4 and m5 != n5:
    print('Y')
    
else:
    print('N')