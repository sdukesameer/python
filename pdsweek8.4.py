fname = input("Enter file name: ")
fname="romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    for letter in line.split():
        if letter not in lst:
            lst.append(letter)
print(sorted(lst))
