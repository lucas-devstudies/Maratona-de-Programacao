L,D = input().split(' ')
K,P = input().split(' ')

L = int(L)  
D = int(D)  
K = int(K)  
P = int(P)  

Q = L//D

print(int((Q*P)+(L*K)))