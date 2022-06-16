c,s=0,0.0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    s+=float(line[line.find(':')+1:])
    c+=1
print("Average spam confidence:",s/c)