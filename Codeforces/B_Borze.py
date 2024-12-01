txt = input().split()
m=''
txt = list(txt[0])
while len(txt)!=0:
    if txt[0]=='.':
        del txt[0]
        m+='0'
    elif txt[0]=='-' and txt[1]=='.':
        del txt[0]
        del txt[0]
        m+='1'
    elif txt[0]=='-' and txt[1]=='-':
        del txt[0]
        del txt[0]
        m+='2'
        
print(str(m))