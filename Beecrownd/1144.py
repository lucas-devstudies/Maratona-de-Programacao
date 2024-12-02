N  = int(input())
for i in range(1,N+1):
    a = i*i
    print("{} {} {}".format(str(i), str(a), str(i*a)))
    print("{} {} {}".format(str(i), str(a+1), str((i*a)+1)))