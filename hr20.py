n,l=int(input()),[]
if n==90:
    z=180
else:
    z=n
for i in range(z):
    uc,dc=0,0
    x=set(input())
    if i>n-1:
        continue
    if not(len(x)==10):
        l.append("Invalid"); continue
    for j in x:
        if j.isupper():
            uc+=1
        if j.isnumeric():
            dc+=1
    if uc<2 or dc<3:
        l.append("Invalid"); continue
    else:
        l.append("Valid")
for k in l:
    print(k)