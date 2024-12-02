def jurosSimples(c,i,n):
    m = (i*n)*c
    return m

def jurosCompostos(c,i,n):
    m = (c*((1+i)**n))-c 
    return m   

while True:
    try:
        c = float(input())
        i = float(input())
        n = int(input())

        js = jurosSimples(c,i,n)
        jc = jurosCompostos(c,i,n)

        a,b = js,jc
        if a<b:
            a,b=b,a

        print(f'DIFERENCA DE VALOR = {(a-b):.2f}')
        print(f'JUROS SIMPLES = {js:.2f}')
        print(f'JUROS COMPOSTO = {jc:.2f}')
    except EOFError:
        break