h = int(input())
for i in range(h):
	n = int(input())
	t = n//2
	if n<=2:
		t=0
	else:
		t= ((n+1)//2)-1
	print(t)
