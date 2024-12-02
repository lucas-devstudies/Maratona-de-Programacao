A,B,C = input().split()

pi = 3.14159

A = float(A)
B = float(B)
C = float(C)

tri= (A*C)/2
cir= pi*(C*C)
tra= ((A+B)*C)/2
qua= B*B
ret= A*B

print('TRIANGULO: {:.3f}'.format(tri))
print('CIRCULO: {:.3f}'.format(cir))
print('TRAPEZIO: {:.3f}'.format(tra))
print('QUADRADO: {:.3f}'.format(qua))
print('RETANGULO: {:.3f}'.format(ret))