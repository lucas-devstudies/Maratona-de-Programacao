sair = 1
media = 0
notas = []
saidas = []
cont = 0
while True:
    if sair == 1:
        while True:
            try:
                nota = float(input())
                if nota>= 0 and nota<=10:
                    notas.append(nota)
                    cont += 1
                    if cont == 2:
                        media = (notas[0] + notas[1]) / 2
                        print('media = {:.2f}'.format(media))
                        notas.clear()
                        media = cont = 0
                        break
                
                else:
                    print('nota invalida')

            except EOFError:
                print('nota invalida')
        
        print(f'novo calculo (1-sim 2-nao)')
        while True:
            try:
                sair = int(input())
                if sair == 1 or sair == 2:
                    break
                
                else:
                    print(f'novo calculo (1-sim 2-nao)')
                    
            except EOFError:
                print(f'novo calculo (1-sim 2-nao)')
            
    elif sair == 2:
        break
    
for j in range(len(saidas)):
    print(saidas[j])