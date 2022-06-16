t=int(input())
for i in range(t):
    (sn,ss)=input().split()
    n,s,x=int(sn),int(ss),0
    for j in range(1,n+1):
        x=0
        cs=((n*n+n)/2)-j
        if cs==s:
            print(j)
            x=1
    if x==0:
        print("-1")