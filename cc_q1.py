n=int(input())
for i in range(n):
    t=int(input())
    j=1; k=1
    while k<=t:
        if j+1>4:
            j=1;k+=1
            continue
        j+=1; k+=1
    if j==1:
        print("North")
    elif j==2:
        print("East")
    elif j==3:
        print("South")
    else:
        print("West")