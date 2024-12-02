while True:
    try:
        lista = [i for i in input().split()]
        palavraAnterior=''
        letras =  []
        permisao = True
        for i in range(len(lista)):
            if i==0:
                palavra = lista[i]
                palavraAnterior = palavra[0].upper()
            else:
                palavra = lista[i]
                atual = palavra[0].upper()
        
                if atual != palavraAnterior:
                    palavraAnterior = atual
                    letras.append('#')            
                else:
                    v = len(letras)
                    if v==0:
                        letras.append(atual)
                    elif letras[-1]!=atual:
                        letras.append(atual)
        cont=0
        for letra in letras:
            if letra!='#':
                cont+=1
        
        print(cont)
    except EOFError:
        break