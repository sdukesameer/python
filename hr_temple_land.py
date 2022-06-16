x=int(input())
a=[]
for i in range(x):
    n=int(input())
    l=[]
    l=input().split()
    if (n%2==0):
        a.append("no")
        continue
    j=1; c=n/2-1; t=0#3
    for k in range(n):
        if j!=int(l[k]):
            a.append("no")
            t=1; break
        if k>=c:
            j=j-1
        else:
            j=j+1
    if t==0:
        a.append("yes")
for m in a:
    print(m)