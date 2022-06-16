import re
sum=0;count=0
fname=input("Enter the file name: ")
file=open(fname)
for line in file:
    l=re.findall('[0-9]+',line)
    if len(l)<1:    continue
    for i in l:
        sum=sum+int(i)
print("Sum: "+str(sum),sep='')