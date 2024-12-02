n1, n2, n3, n4 = input().split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1*2)+(n2*3)+(n3*4)+(n4))/10

if media >= 7.0:
    print(f'Media: {media:,.1f}')
    print('Aluno aprovado.')
    
elif media >= 5.0 and media <= 6.9:
    nota = float(input())
    print(f'Media: {media:,.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {nota:,.1f}')
    media2 = (nota+media)/2
    if media2 >= 5.0:
        print('Aluno aprovado.')
        print(f'Media final: {media2:,.1f}')
        
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media2:,.1f}')
        
else:
    print(f'Media: {media:,.1f}')
    print('Aluno reprovado.')