dicionario = {}
saida = []
inicio = True
while True:
    try:
        n = int(input())
        for i in range(n):
            c,v = input().split()
            v = int(v)
            
            dicionario[c] = v
        
        for j in sorted(dicionario, key = dicionario.get):
            if inicio == True:
                mensagem = f'{j}'
                inicio = False
                
            else:
                mensagem = mensagem + f' {j}'
        
        print(mensagem)
        dicionario.clear()
        mensagem = ''
        inicio = True
    
    except:
        break
    