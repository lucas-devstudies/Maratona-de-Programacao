n = int(input())
for i in range(n):
    p = input()
    if len(p)>10:
        t = len(p)
        s = f'{p[0]}{len(p)-2}{p[-1]}'
        print(s)
    else:
        print(p)