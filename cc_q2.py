t=int(input())
for x in range(t):
    n,s=input().split()
    l=-1
    for i in range(int(n)+1):
        if i>int(s):
            break
        for j in range(int(n)+1):
            if j>int(s) or i+j>int(s):
                break
            elif (i+j)==int(s):
                if l < abs(i-j):
                    l=abs(i-j)
    print(l)