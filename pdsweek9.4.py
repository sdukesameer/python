name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d={}
for line in handle:
    if line.startswith("From "):
        l=line.split()
        d[l[1]] = d.get(l[1],0)+1
hc,hn=-1,""
for w,c in d.items():
    if c > hc:
        hc=c
        hn=w
print(hn,hc)