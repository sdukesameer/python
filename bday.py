import datetime
#bubble sort function
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j][2].split("/")[0]>arr[j+1][2].split("/")[0]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
#convert 04/05/2000 to 4th May
def db(s):
    sr=""
    spl=s.split("/")
    for i in range(3):
        spl[i]=int(spl[i])
    if spl[0]==1 or spl[0]==21 or spl[0]==31:
        f=str(spl[0])
        if f[0]=='0':
            sr=f[1]+"st "
        else:
            sr=f+"st "
    elif spl[0]==2 or spl[0]==22:
        f=str(spl[0])
        if f[0]=='0':
            sr=f[1]+"nd "
        else:
            sr=f+"nd "
    elif spl[0]==3 or spl[0]==23:
        f=str(spl[0])
        if f[0]=='0':
            sr=f[1]+"rd "
        else:
            sr=f+"rd "
    else:
        f=str(spl[0])
        if f[0]=='0':
            sr=f[1]+"th "
        else:
            sr=f+"th "
    if int(spl[1])==1:
        sr=sr+"January"
    elif int(spl[1])==2:
        sr=sr+"February"
    elif int(spl[1])==3:
        sr=sr+"March"
    elif int(spl[1])==4:
        sr=sr+"April"
    elif int(spl[1])==5:
        sr=sr+"May"
    elif int(spl[1])==6:
        sr=sr+"June"
    elif int(spl[1])==7:
        sr=sr+"July"
    elif int(spl[1])==8:
        sr=sr+"August"
    elif int(spl[1])==9:
        sr=sr+"September"
    elif int(spl[1])==10:
        sr=sr+"October"
    elif int(spl[1])==11:
        sr=sr+"November"
    else:
        sr=sr+"December"
    return sr
#initialisation
students={}
months = {
    "January" : [],
    "February" : [],
    "March" : [],
    "April" : [],
    "May" : [],
    "June" : [],
    "July" : [],
    "August" : [],
    "September" : [],
    "October" : [],
    "November" : [],
    "December" : []
}
#input and put all necessary data in students dictionary
#fname=input("Enter .txt file name you want to open: ")
fh=open("dob.txt")
for line in fh:
    l=[]
    c=0
    for word in line.split(","):
        if c==2 or c==4 or c==6 or c==9:
            l.append(word)
        c+=1
    students[l[1]]=l
#insert all data's according to their month
#'13000119001': ['SHUBRAJIT ROY', '13000119001', '29/03/2000', '8131838608']
for roll in students:
    m=int(students[roll][2].split('/')[1])
    if m==1:
        months["January"].append(students[roll])
    elif m==2:
        months["February"].append(students[roll])
    elif m==3:
        months["March"].append(students[roll])
    elif m==4:
        months["April"].append(students[roll])
    elif m==5:
        months["May"].append(students[roll])
    elif m==6:
        months["June"].append(students[roll])
    elif m==7:
        months["July"].append(students[roll])
    elif m==8:
        months["August"].append(students[roll])
    elif m==9:
        months["September"].append(students[roll])
    elif m==10:
        months["October"].append(students[roll])
    elif m==11:
        months["November"].append(students[roll])
    else:
        months["December"].append(students[roll])
#sort all months according to date
for month in months:
    bubbleSort(months[month])
#user choice manupulation
inp=0
while(inp!=5):
    print("\n1. Display all b'days month wise -")
    print("2. Display b'days of a selective month -")
    print("3. Search a person's date of birth -")
    print("5. Exit program -")
    inp=int(input("Enter your choice: "))
    cur_time=datetime.datetime.now()
    if inp==1:
        for month in months:
            print("\nB'day Month:-",month,end="\n\n")
            for stud in months[month]:
                print("Name: ",stud[0].ljust(25,' ')," B'day: ",db(stud[2]).ljust(15,' '),"Roll: ",stud[1],"  "," Contact: ",stud[3],end="\n", sep="")
    elif inp==2:
        print("\nMonths = January, February, March, April, May, June, July, August, September, October, November, December")
        mn=input("Enter the month you want to view: ")
        for month in months:
            if month==mn:
                print("\nB'day Month:-",month,end="\n\n")
                for stud in months[month]:
                    print("Name: ",stud[0].ljust(25,' ')," B'day: ",db(stud[2]).ljust(15,' '),"Roll: ",stud[1],"  "," Contact: ",stud[3],end="\n", sep="")
    elif inp==3:
        ch=0
        while(ch!=3):
            print("\n1. Search by Name: ")
            print("2. Search by Roll: ")
            print("3. Don't Search")
            ch=int(input("Enter your choice: "))
            if ch==1:
                c=0
                while(c!=1):
                    name=input("\nEnter full name: ").strip().upper()
                    for roll in students:
                        if students[roll][0]==name:
                            print("\nName : ",students[roll][0],"\n","B'day : ",db(students[roll][2]),"\n","Roll : ",students[roll][1],"\n","Contact : ",students[roll][3],end="\n", sep="")
                            c=1; break;
                    if c == 0:
                        print("Invalid Name, name not found.")
                        x=input("Wanna try again? (Yes/No): ").upper();
                        if x=="NO" or x=='N':
                            break;
                    if c==1:
                        print("\nDo you wish to know ",students[roll][0],"'s ","age: ",end="",sep="")
                        yn=input(" [Yes/No]: ").upper()
                        if yn=="YES" or yn=="Y":
                            code=0
                            while code!=1210:
                                code=int(input("Enter the secret code: "))
                                if code==int("01210"):
                                    spl=students[roll][2].split("/")
                                    if int(spl[1]) > cur_time.month:
                                        print("\n",end="")
                                        print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])-1," years",sep="")
                                    elif int(spl[1]) < cur_time.month:
                                        print("\n",end="")
                                        print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])," years",sep="")
                                    else:
                                        if int(spl[0]) > cur_time.day:
                                            print("\n",end="")
                                            print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])-1," years",sep="")
                                        elif int(spl[0]) < cur_time.day:
                                            print("\n",end="")
                                            print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])," years",sep="")
                                        else:
                                            print("Its your b'day, Happy Birthday!")
                                else:
                                    print("You don't have correct code!")
                                    x=input("Wanna try again? (Yes/No): ").upper();
                                    if x=="NO" or x=='N':
                                        break;
            elif ch==2:
                c=0
                while c!=1:
                    roll=input("\nEnter last 3 digits or full Roll no [In case of Stream Change enter full Roll only!]: ")
                    if len(roll)==3:
                        roll="13000119"+roll
                    try:
                        print("\nName : ",students[roll][0],"\n","B'day : ",db(students[roll][2]),"\n","Roll : ",students[roll][1],"\n","Contact : ",students[roll][3],end="\n", sep="")
                        c=1
                        print("\nDo you wish to know ",students[roll][0],"'s ","age: ",end="",sep="")
                        yn=input(" [Yes/No]: ").upper()
                        if yn=="YES" or yn=='Y':
                            code=0
                            while code!=1210:
                                code=int(input("Enter the secret code: "))
                                if code==int("01210"):
                                    spl=students[roll][2].split("/")
                                    if int(spl[1]) > cur_time.month:
                                        print("\n",end="")
                                        print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])-1," years",sep="")
                                    elif int(spl[1]) < cur_time.month:
                                        print("\n",end="")
                                        print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])," years",sep="")
                                    else:
                                        if int(spl[0]) > cur_time.day:
                                            print("\n",end="")
                                            print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])-1," years",sep="")
                                        elif int(spl[0]) < cur_time.day:
                                            print("\n",end="")
                                            print(students[roll][0],"'s ","Age is: ",cur_time.year-int(spl[2])," years",sep="")
                                        else:
                                            print("*** Its your b'day, Happy Birthday! ***")
                                else:
                                    print("You don't have correct code!")
                                    x=input("Wanna try again? (Yes/No): ").upper();
                                    if x=="NO" or x=='N':
                                        break;
                        else:
                            c=1;
                    except:
                        print("Invalid Roll, roll not found.")
                        x=input("Wanna try again? (Yes/No): ").upper();
                        if x=="NO" or x=='N':
                            c=1;
            elif ch==3:
                print("Exiting Search. Thank You.")
            else:
                print("Oops, Invalid, criteria. Try again!")
    elif inp==5:
        print("Thank you, exitting the program!")
    else:
        print("Oops, Invalid choice! Try again.")