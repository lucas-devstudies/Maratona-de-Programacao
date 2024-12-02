n = int(input())
ano = mes = dia = 0

ano = n//365
mes = (n%365)//30
dia = (n%365) % 30

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
