n=int(input())
b=0
p=0

for i in range(n):
    for j in range(n):
        if i==0 or i%2==0:
            if j == 0 or j%2==0:
                b = b + 1;   
            else:
                p = p + 1;
        else:
            if j == 0 or j%2==0:
                p = p + 1;   
            else:
                b = b + 1; 
print(f"{b} casas brancas e {p} casas pretas")