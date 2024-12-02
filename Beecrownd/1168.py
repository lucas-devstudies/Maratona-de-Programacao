N = int(input())

for i in range(N):
    numero = input()
    soma = 0
    for n in range(len(numero)):
        if numero[n]=='1':
            soma += 2
        elif numero[n]=='2':
            soma += 5
        elif numero[n]=='3':
            soma += 5
        elif numero[n]=='4':
            soma += 4
        elif numero[n]=='5':
            soma += 5
        elif numero[n]=='6':
            soma += 6
        elif numero[n]=='7':
            soma += 3
        elif numero[n]=='8':
            soma += 7
        elif numero[n]=='9':
            soma += 6
        else:
            soma+=6
    print(f'{soma} leds')