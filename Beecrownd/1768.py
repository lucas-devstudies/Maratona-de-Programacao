while True:
    try:
        n = int(input())
        cont = (n//2) + 1
        v = cont
        menssage = ''
        
        for i in range(1, n+1, 2):
            menssage = menssage + (' ' * ((n-i)//2)) + ('*' * i) + '\n'
            
        menssage = menssage + (' ' * ((n-1)//2)) + '*' + '\n'
        menssage = menssage + (' ' * ((n-3)//2)) + '***' + '\n'
        print(menssage)
        
    except EOFError:
        break