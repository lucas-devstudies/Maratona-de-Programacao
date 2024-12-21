txt = list(input().lower())
vogais = 'aoyeui'
a = []
for i in txt:
    if i not in vogais:
        a.append('.')
        a.append(i)
 
print(''.join(a))