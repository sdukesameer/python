while(1):
    try:
        fn=input("Enter file name: ")
        fp=open(fn,"r")
    except FileNotFoundError:
        print("File not Found. Try again.")
    else:
        break;
list=fp.readlines()
for i in list:
    for j in i[:-1]:
        print(j,end="")
    print(end=" ")
fp.close()