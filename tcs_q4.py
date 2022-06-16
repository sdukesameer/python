l=[int (i) for i in input()]
s=input()
m = 0
for i in range(len(s)):
    if s[i] =='R' and m+1<len(l):
        m+=1
    elif s[i] =='L' and m-1>=0:
        m-=1
    elif s[i]  =='T' and l[m]!=9:
        l[m] = l[m]+1
    elif s[i]  =='D' and l[m]!=0:
        l[m] = l[m]-1
    elif s[i]  =='S':
        l[m],l[int(s[i+1])-1]=l[int(s[i+1])-1],l[m]
        i=i+1
print("".join(map(str,l)),sep='',end='\n')
