saidas = []
while True:
    try:
        n = int(input())
        EPR = 0
        EHD = 0
        INTRUSOS = 0
        for i in range(n):
            c,t = input().split()
           
            if len(c)!=5:
                break
            
            elif t == "EPR":
                EPR += 1

            elif t == "EHD":
                EHD += 1
            
            else:
                INTRUSOS += 1
                
        saidas.append(f'EPR: {EPR}')
        saidas.append(f'EHD: {EHD}')
        saidas.append(f'INTRUSOS: {INTRUSOS}')
    except EOFError:
        break
    
for j in range(len(saidas)):
    print(saidas[j])