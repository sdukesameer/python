xx,kk=input().split()
p=input().split(" ")
#-x**13,x**2
#[-x,13],[x,2]
t=0
for i in range(len(p)):
    if p[i]=='-':
        t=1
        continue
    if t==1:
        p[i]='-'+p[i]
        t=0
for f in p:
    if f=='-' or f=='+':
        p.remove(f)
r=0;x=int(xx);k=int(kk)
for j in p:
    if j.isnumeric():
        r+=int(j)
    elif j=='x':
        r+=x
    elif j=='-x':
        r-=x
    elif j.find("x")>-1:
        s=j.split("**")
        if s[0]=='x':
            r+=int(pow(x,int(s[1])))
        elif s[0]=='-x':
            r-=int(pow(x,int(s[1])))
        else:
            #q=[-1,x]
            q=s[0].split("*")
            if q[0].startswith("-"):
                q[0]=q[0][1:]
                r-=int(q[0])*(int(pow(x,int(s[1]))))
            else:
                r+=int(q[0])*(int(pow(x,int(s[1]))))
    else:
            try:
                r-=int(j[1:])
            except:
                pass
if r==k:
    print("True")
else:
    print("False")