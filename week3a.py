def contracting(l):
    if len(l) < 3:
        return (False)
    diff=abs(l[0]-l[1])
    for i in range(1,len(l)-1):
        if abs(l[i]-l[i+1]) < diff:
            diff=abs(l[i]-l[i+1])
        else:
            return (False)
    return (True)
def counthv(l):
    (hc,vc)=(0,0)
    if len(l) < 3:
        return ([hc,vc])
    for i in range(1,len(l)-1):
        if l[i-1] < l[i] and l[i+1] < l[i]:
            hc=hc+1
        elif l[i-1] > l[i] and l[i+1] > l[i]:
            vc=vc+1
    return ([hc,vc])
def leftrotate(m):
    new=[]
    for i in range(len(m)):
        temp=[]
        for j in m[i]:
            temp.append(j)
        new.append(temp)
    for i in range(len(m)):
        r=len(m)-1
        for j in range(len(m)):
            new[r][i]=m[i][j]
            r=r-1
    return (new)
import copy
def rotate(m):
    new=copy.deepcopy(m)
    for i in range(len(m)):
        r=len(m)-1
        for j in range(len(m)):
            new[r][i]=m[i][j]
            r=r-1
    return (new)