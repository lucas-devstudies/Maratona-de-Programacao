lista = []
n=0
while True:
    n = input()
    if int(n,16)<0:
        break
    elif 'x' not in n:
        m = hex(int(n))
        m = str(m).upper()
        lista.append(('0x'+m[2:]))
    else:
        m = int(n,16)
        lista.append(str(m))
    
print('\n'.join(lista))