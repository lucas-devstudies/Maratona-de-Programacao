while True: 
    try:
        s,va,vb=map(int,input().split())
        if vb>va:
            print('impossivel')
        else:
            print(f'{(s/(va-vb)):.2f}')
    except EOFError:
        break