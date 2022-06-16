n=int(input())
l=[]
for i in range(n):
    x=input()
    if (x[0]=='9' or x[0]=='8' or x[0]=='7') and len(x)==10 and x.isnumeric():
        l.append("YES")
    else:
        l.append("NO")
for y in l:
    print(y)