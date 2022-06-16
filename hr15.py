import cmath
inp = input()
t=0;a="";b=""
for i in inp:
    if i=='+' or i=='-':
        if t==0:
            t=1
        else:
            t=0
    if t==0:
        a+=i
    if t==1:
        b+=i
if inp[0]=="-":
    (a,b)=(b,a)
if not(ord(a[-1])>47 and ord(a[-1])<58):
    a=a[0:-1]; 
if not(ord(b[-1])>47 and ord(b[-1])<58):
    b=b[0:-1]
x=int(a); y=int(b)
print('%.3f'%abs(complex(x,y)))
print('%.3f'%cmath.phase(complex(x,y)))