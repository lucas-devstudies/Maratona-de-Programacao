O,B,I = map(float,input().split())

if O == B and I>B or B==I and O>I or I==O and B>O or B == I and I == O:
    print('Empate')
    
elif O<B and O<I:
    print('Otavio')
    
elif I<B and I<O:
    print('Ian')
    
else: 
    print('Bruno')