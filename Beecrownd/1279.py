comecou = False

while True:
    nada = True        
    try:
        n = int(input())
        if comecou == False:
            comecou = True
        else:
            print()
        if n%4== 0 and n%100!=0 or n%400==0:
            print('This is leap year.')
            if n%15==0:
                print('This is huluculu festival year.')
                nada = False
            if n%55==0:
                print('This is bulukulu festival year.')
            nada = False
        else:
            if n%15==0:
                print('This is huluculu festival year.')
                nada = False
    
        if nada == True:
            print('This is an ordinary year.')
    except EOFError:
        break