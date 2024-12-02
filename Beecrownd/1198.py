while True:
    try:
        a,b = map(int,input().split())
        if b>a:
            b,a=a,b
        print(a-b)
    except EOFError:
        break