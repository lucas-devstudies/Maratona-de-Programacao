t = int(input())
for _ in range(t):
    n = int(input())
    l1 = list(input())
    l2 = list(input())
    for i in range(n):
        l1[i] = int(l1[i])
        l2[i] = int(l2[i])
    c=0
    for i in range(n):
        if i == 0:
            if l2[i]==1:
                if l1[i]==0:
                    c+=1
                    l1[i]=3
                
                elif l1[i+1]==1 and i+1<=n-1:
                    c+=1
                    l1[i+1]=3
 
        elif i == n-1:
            if l2[i]==1: 
                if l1[i-1]==1:
                    c+=1
                    l1[i-1] = 3
                    
                elif l1[i]==0:
                    c+=1
                    l1[i] = 3
                                    
        else:
            if l2[i]==1:
                if l1[i-1]==1:
                    c+=1
                    l1[i-1] = 3
                
                elif l1[i]==0:
                    c+=1
                    l1[i] = 3
                    
                elif l1[i+1]==1:
                    c+=1
                    l1[i+1] = 3
                else:
                    pass
    print(c)