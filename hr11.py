inp=input()
l=inp.split(" ")
n=int(l[0]); m=int(l[1])
for i in range(1,n+1):
    if i==((n+1)/2):
        print("WELCOME".center(m,'-'))
    elif i<((n+1)/2):
        print((".|."*(i*2-1)).center(m,'-'))
    else:
        print((".|."*((abs(n-i+1))*2-1)).center(m,'-'))