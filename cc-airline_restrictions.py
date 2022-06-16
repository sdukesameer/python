t=int(input())
l=[]
for i in range(t):
    (a,b,c,d,e)=map(int,input().split())
    if min(a,b,c)>e:#cant carry
        l.append("NO")
        continue
    elif a+b<=d and c<=e:
            l.append("YES")
            continue
    elif b+c<=d and a<=e:
            l.append("YES")
            continue
    elif c+a<=d and b<=e:
            l.append("YES")
            continue
    else:
        l.append("NO")
for j in l:
    print(j)