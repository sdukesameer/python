name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d={}
for line in handle:
    if line.startswith("From "):
        l=line.split()
        h=l[-2].split(':')
        d[h[0]] = d.get(h[0],0)+1
for key,v in sorted(d.items()):
    print(key,v)