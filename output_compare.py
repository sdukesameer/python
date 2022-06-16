#fname=input("Enter 1st file name: ")
fh=open("hr_output.txt")
#sname=input("Enter 2nd file name: ")
sh=open("code_output.txt")
c=1
for i,j in zip(fh,sh):
    if i!=j:
        print("Different at line: "+str(c),end="")
        if i=="YES":
            print(" | YES:NO")
        else:
            print(" | NO:YES")
    c+=1
fh.close()
sh.close()