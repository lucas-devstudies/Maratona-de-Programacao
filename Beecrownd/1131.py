resposta = 1
gremio = inter = empate = cont = 0
while True:
    if resposta==1:
        i,g = map(int,input().split())
        cont+=1
        if i>g:
            inter+=1
        elif g>i:
            gremio+=1
        else:
            empate+=1
    else:
        break

    print('Novo grenal (1-sim 2-nao)')
    resposta = int(input())

print(f'{cont} grenais')
print(f'Inter:{inter}')
print(f'Gremio:{gremio}')
print(f'Empates:{empate}')
if inter>gremio:
    print('Inter venceu mais')
elif gremio>inter:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')