n = int(input())
for _ in range(n):
    l = [int(i) for i in input().split()]
    l.sort()
    t = len(l)//2
    print(f'Case {_+1}: {l[t]}')