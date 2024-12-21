minusculo ='abcdefghijklmnopqrstuvwxyz'
 
m = n = 0
txt = input()
for i in txt:
	if i in minusculo:
		n+=1
	else:
		m+=1
		
if m==n:
	print(txt.lower())
elif n>m:
	print(txt.lower())
else:
	print(txt.upper())