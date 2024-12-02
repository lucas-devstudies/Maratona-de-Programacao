a,b,c= input().split()

a = int(a)
b = int(b)
c = int(c)

if a>b and a>c or c>b and a==c or a>b and a==c:
    print(f"{a} eh o maior")
    
elif b>a and b>c or b>a and b==c or b>c and b==a:
    print(f"{b} eh o maior")
    
elif c>b and c>a or c>a and b==c or c>b and c==a:
    print(f"{c} eh o maior")