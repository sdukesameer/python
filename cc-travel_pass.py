x=int(input())
l=[]
for j in range(x):
    t=0
    (n,a,b)=input().split()
    s=input()
    for i in s:
        if i=='0':
            t+=int(a)
        if i=='1':
            t+=int(b)
    l.append(t)
for k in l:
    print(k)