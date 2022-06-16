def primeproduct(n):
    p=1
    for i in range(1,n):
        if n%i==0:
            p=p*i
    if p==n:
        return (True)
    else:
        return (False)
def delchar(s,c):
    if len(c)!=1:
        return (s)
    else:
        l=""
        for i in range(0,len(s)):
            if s[i]!=c:
                l=l+s[i]
    return (l)
def shuffle(l1,l2):
    l=[]
    for i in range(0,max(len(l1),len(l2))):
        if i<len(l1):
            l.append(l1[i])
        if i<len(l2):
            l.append(l2[i])
    return (l)