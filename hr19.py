n,l=int(input()),[]
for i in range(n):
    if i=='0':
        l.append("True")
        continue
    try:
        x=float(input())
        l.append("True")
    except:
        l.append("False")
    finally:
        continue;
for j in l:
    print(j)