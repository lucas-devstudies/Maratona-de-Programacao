n = int(input())

for i in range(n):
    alunos=[int(i) for i in input().split()]
    media=0
    for i in range(1,len(alunos),1):
        media = alunos[i]+media
    
    qtd=0
    media = (media/alunos[0])
    
    for i in range(1,len(alunos)):
        if alunos[i]>media:
            qtd+=1
    
    if qtd==0:
        print('0.000%')
    else:
        print(f'{((qtd/alunos[0])*100):.3f}%')