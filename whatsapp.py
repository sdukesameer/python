import io
s=[]
fname=input("Enter file name you want to comprehend: ")
fh=open(fname,encoding="utf8")
date=input("Enter the date as (dd/mm/yyyy): ")
for line in fh:
    if line.startswith(date):
        s.append(line[line.find('-'):])

ename=input("Enter the file name in which you want to save the manupulated data: ")
with io.open(ename, "w", encoding="utf-8") as f:
    for items in s:
        f.write('%s\n' %items)
    print("%s named file has been successfully created.\n" %ename)