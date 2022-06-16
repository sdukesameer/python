n=int(input())
f=[]
for i in range(n):
    l=input().split()
    f.append(l)
for j in f:
    try:
        print(int(j[0])//int(j[1]))
    except ZeroDivisionError as e:
        print("Error Code:",e,sep=" ")
    except ValueError as v:
        print("Error Code:",v,sep=" ")
    finally:
        continue