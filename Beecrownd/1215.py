import re
import sys
lidos = set()

linhas = sys.stdin.readlines()
linhas = [linha.strip().lower() for linha in linhas]
for t in linhas:
    if t not in lidos:
        resultado = re.findall(r'[a-z]+',t)
        resultado = [item for item in resultado if item]
        for palavras in resultado:
            lidos.add(palavras)
    else:
        continue

for lido in sorted(lidos):
    print(lido)