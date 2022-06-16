fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)
l=[];count = 0
for line in fh:
    if line.startswith("From "):
        l=line.split()
        print(l[1])
        count+=1
print("There were", count, "lines in the file with From as the first word")