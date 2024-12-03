while True:
    try:
        n = int(input())
        if n==0:
            break
        elif n<3:
            print(1)
        else:
            t=1
            h = 3
            m=[]
            while True:
                if t>n:
                    break
                else:
                    m.append(str(t))
                    t+=h
                    h+=2
            print(" ".join(m))
    except EOFError:
        break
