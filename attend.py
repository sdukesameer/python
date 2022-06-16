import datetime
fh=open(input())
fh1=open("db.txt")
wh=open("out.csv",'w')
l=[]; stud={}
for line in fh1:
    (a,b)=line.split(','); b=int(b)
    stud[b]=a
for line in fh:
    if line.startswith('M') or line.startswith('F'):
        continue
    for word in line.split():
        if int(word) not in l:
            l.append(int(word))
        break
(p,a)=0,0
for key in stud:
    if key in l:
        print(str(key).ljust(15,' '),stud[key].ljust(25,' '),2,sep=',',file=wh)
        p=p+1
    else:
        print(str(key).ljust(15,' '),stud[key].ljust(25,' '),0,sep=',',file=wh)
        a=a+1
print("\nTotal present: "+str(p)+", "+"total absent: "+str(a)+".",file=wh)