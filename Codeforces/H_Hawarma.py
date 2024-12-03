n = int(input())
t = []
for x in range(-5000,5001):
    v = 5*x*(n**2)
    h = (x**2)+(3*(x)*n)-(5*(n**2))
    if v/h==x:
        t.append(str(x))

print(len(t))
print(" ".join(t))
