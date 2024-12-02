numeros = [int(i) for i in input().split()]

dasher = True
dancer = True
prancer = True
vixen = True
comet = True
cupid = True
donner = True
blitzen = True
rudolph = True

for i in range(9):
    while numeros[i]>0:
        if dasher == True:
            numeros[i]  += -1    
            dasher = False
            if numeros[8]==0:
                print('Dasher')

        elif dancer == True:
            numeros[i]  += -1    
            dancer = False
            if numeros[8]==0:
                print('Dancer')
        
        elif prancer == True:
            numeros[i]  += -1    
            prancer = False
            if numeros[8]==0:
                print('Prancer')

        elif vixen == True:
            numeros[i]  += -1    
            vixen = False
            if numeros[8]==0:
                print('Vixen')

        elif comet == True:
            numeros[i]  += -1    
            comet = False
            if numeros[8]==0:
                print('Comet')

        elif cupid == True:
            numeros[i]  += -1    
            cupid = False
            if numeros[8]==0:
                print('Cupid')

        elif donner == True:
            numeros[i]  += -1    
            donner = False
            if numeros[8]==0:
                print('Donner')
        
        elif blitzen == True:
            numeros[i]  += -1    
            blitzen = False
            if numeros[8]==0:
                print('Blitzen')
        else:
            numeros[i]  += -1    
            dasher = True
            dancer = True
            prancer = True
            vixen = True
            comet = True
            cupid = True
            donner = True
            blitzen = True
            rudolph = True
            if numeros[8]==0:
                print('Rudolph')
        