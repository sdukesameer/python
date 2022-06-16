import datetime; import calendar
print("\n # Welcome to MS-Teams Attendance Calculator Program # \n")
dh,fh=open(input("Please input name-list filename (.csv): "),"r",encoding='utf-8'),open(input("Please input attendance filename (.csv): "),"r",encoding='utf-8')
stud={};c=0;s="";e="";m="";d=0;pt=0;u=0;z=[]
for line in dh:
    if u==0:
        for z in line.split(','): 
            if z.upper().strip()=='MS TEAMS ID' or z.upper().strip()=='TEAMS ID' or z.upper().strip()=='MS ID': z=line.split(','); break; 
            u+=1
    elif len(line)<1:   continue
    else:   x=line.split(',');    x.append("");x.append("");x.append(0);stud[int(x[u].strip()[:x[u].index('@')])]=x
for line in fh:
    c+=1
    if c==2:
        word=line.split(",");print("\nFaculty Name: \"",word[0],"\", the day was \"",calendar.day_name[datetime.datetime.strptime(word[2].split(',')[0][1:],'%m/%d/%Y').weekday()],"\" and the class started at \"",word[2].split(',')[1],"\".",sep='')
        m=str(word[2].split(',')[0][1:].split('/')[1]) + "-" + ("Jan" if int(word[2].split(',')[0][1:].split('/')[0])==1 else "Feb" if int(word[2].split(',')[0][1:].split('/')[0])==2 else "Mar" if int(word[2].split(',')[0][1:].split('/')[0])==3 else "Apr" if int(word[2].split(',')[0][1:].split('/')[0])==4 else "May" if int(word[2].split(',')[0][1:].split('/')[0])==5 else "Jun" if int(word[2].split(',')[0][1:].split('/')[0])==6 else "Jul" if int(word[2].split(',')[0][1:].split('/')[0])==7 else "Aug" if int(word[2].split(',')[0][1:].split('/')[0])==8 else "Sep" if int(word[2].split(',')[0][1:].split('/')[0])==9 else "Oct" if int(word[2].split(',')[0][1:].split('/')[0])==10 else "Nov" if int(word[2].split(',')[0][1:].split('/')[0])==11 else "Dec")
        s=word[2].split(',')[1].split()[0]; e=input("Please enter the class ending time (HH:MM:SS): ")
        t=str(datetime.datetime.strptime(e,'%H:%M:%S') - datetime.datetime.strptime(s,'%H:%M:%S')).split(':')
        d=int(t[0])*60 + int(t[1]) + (1 if int(t[2])>29 else 0); pt=round(d/50)
        print("The class was: ",str(pt)," periods long,"," as the total duration was: ",t[0]," hour ",t[1]," minutes and ",t[2]," seconds.\n",sep="");
    elif c>2 and not line.startswith('Mr.'):
        word=line.split(',')
        if word[1].startswith("Joined"):   stud[int(word[0])][-3]=word[-1].split()[0]; stud[int(word[0])][-1]=1
        elif word[1]=="Left":
            if stud[int(word[0])][-2]!="": 
                d1=datetime.datetime.strptime(str(stud[int(word[0])][-2]),'%H:%M:%S') 
                d2=datetime.datetime.strptime(str(datetime.datetime.strptime(word[-1].split()[0],'%H:%M:%S') - datetime.datetime.strptime(stud[int(word[0])][-3],'%H:%M:%S')),'%H:%M:%S')
                stud[int(word[0])][-2] =str(datetime.timedelta(hours=d1.hour,minutes=d1.minute,seconds=d1.second) + datetime.timedelta(hours=d2.hour,minutes=d2.minute,seconds=d2.second));  stud[int(word[0])][-1]=0
            elif stud[int(word[0])][-2]=="":
                stud[int(word[0])][-2] = str(datetime.datetime.strptime(word[-1].split()[0],'%H:%M:%S') - datetime.datetime.strptime(stud[int(word[0])][-3],'%H:%M:%S')); stud[int(word[0])][-1]=0
fh.close(); (p,a)=0,0
for i in z[:-1]: print(str(i).center(30,' '),sep='',end='')
print(z[-1][:-1].center(30,' '),"Duration".center(10,' '),m.center(15,' '),sep='',end='\n\n')
for key in stud:
    if stud[key][-3]=="" and stud[key][-2]=="":
        for i in stud[key][:-4]: print(str(i).center(30,' '),sep='',end='')
        print(stud[key][-4][:-1].center(30,' '),"ABSENT".center(10,' '),"0".center(15,' '),sep=''); a+=1
    elif stud[key][-3]!="" and stud[key][-2]=="":
        t=str(datetime.datetime.strptime(e,'%H:%M:%S') - datetime.datetime.strptime(stud[key][-3],'%H:%M:%S')).split(':')
        for i in stud[key][:-4]: print(str(i).center(30,' '),sep='',end='')
        print(stud[key][-4][:-1].center(30,' '),str(datetime.datetime.strptime(e,'%H:%M:%S') - datetime.datetime.strptime(stud[key][-3],'%H:%M:%S')).center(10,' '),str(round(((int(t[0])*60 + int(t[1]) + (1 if int(t[2])>29 else 0) + 1)/d)*pt)).center(15,' '),sep=''); p+=1
    elif stud[key][-2]!="" and stud[key][-1]==0:
        for i in stud[key][:-4]: print(str(i).center(30,' '),sep='',end='')
        print(stud[key][-4][:-1].center(30,' '),str(stud[key][-2]).center(10,' '),str(round(((int(str(stud[key][-2]).split(':')[0])*60 + int(str(stud[key][-2]).split(':')[1]) + (1 if int(str(stud[key][-2]).split(':')[2])>29 else 0) + 1)/d)*pt)).center(15,' '),sep=''); p+=1
    elif stud[key][-2]!="" and stud[key][-1]==1:
        d1=datetime.datetime.strptime(str(stud[key][-2]),'%H:%M:%S')
        d2=datetime.datetime.strptime(str(datetime.datetime.strptime(e,'%H:%M:%S') - datetime.datetime.strptime(stud[key][-3],'%H:%M:%S')),'%H:%M:%S')
        t=str(datetime.timedelta(hours=d1.hour,minutes=d1.minute,seconds=d1.second) + datetime.timedelta(hours=d2.hour,minutes=d2.minute,seconds=d2.second)).split(":")
        for i in stud[key][:-4]: print(str(i).center(30,' '),sep='',end='')
        print(stud[key][-4][:-1].center(30,' '),str(datetime.timedelta(hours=d1.hour,minutes=d1.minute,seconds=d1.second) + datetime.timedelta(hours=d2.hour,minutes=d2.minute,seconds=d2.second)).center(10,' '),str(round(((int(t[0])*60 + int(t[1]) + (1 if int(t[2])>29 else 0) + 1)/d)*pt)).center(15,' '),sep=''); p+=1
print("\nTotal present: "+str(p)+", "+"total absent: "+str(a)+".");p,a,i=0,0,input("\nDo you want to save all these data's to a csv or txt file? (Y/N): ").upper()
if i=="Y" or i=="YES":
    f=input("Enter the output filename: "); wh=open(f,'w');
    print(*z[:-1],z[-1][:-1],"Duration",m,sep=',',end='\n',file=wh)
    for key in stud:
        if stud[key][-3]=="" and stud[key][-2]=="":
            print(*stud[key][:-4],stud[key][-4][:-1],"ABSENT","0",sep=',',file=wh); a+=1
        elif stud[key][-3]!="" and stud[key][-2]=="":
            t=str(datetime.datetime.strptime(e,'%H:%M:%S') - datetime.datetime.strptime(stud[key][-3],'%H:%M:%S')).split(':')
            print(*stud[key][:-4],stud[key][-4][:-1],str(datetime.datetime.strptime(e,'%H:%M:%S') - datetime.datetime.strptime(stud[key][-3],'%H:%M:%S')),str(round(((int(t[0])*60 + int(t[1]) + (1 if int(t[2])>29 else 0) + 1)/d)*pt)),sep=',',file=wh); p+=1
        elif stud[key][-2]!="" and stud[key][-1]==0:
            print(*stud[key][:-4],stud[key][-4][:-1],str(stud[key][-2]),str(round(((int(str(stud[key][-2]).split(':')[0])*60 + int(str(stud[key][-2]).split(':')[1]) + (1 if int(str(stud[key][-2]).split(':')[2])>29 else 0) + 1)/d)*pt)),sep=',',file=wh); p+=1
        elif stud[key][-2]!="" and stud[key][-1]==1:
            d1=datetime.datetime.strptime(str(stud[key][-2]),'%H:%M:%S')
            d2=datetime.datetime.strptime(str(datetime.datetime.strptime(e,'%H:%M:%S') - datetime.datetime.strptime(stud[key][-3],'%H:%M:%S')),'%H:%M:%S')
            t=str(datetime.timedelta(hours=d1.hour,minutes=d1.minute,seconds=d1.second) + datetime.timedelta(hours=d2.hour,minutes=d2.minute,seconds=d2.second)).split(":")
            print(*stud[key][:-4],stud[key][-4][:-1],str(datetime.timedelta(hours=d1.hour,minutes=d1.minute,seconds=d1.second) + datetime.timedelta(hours=d2.hour,minutes=d2.minute,seconds=d2.second)),str(round(((int(t[0])*60 + int(t[1]) + (1 if int(t[2])>29 else 0) + 1)/d)*pt)),sep=',',file=wh); p+=1
    print("\nTotal present: ",str(p),"total absent: ",str(a),sep=',',file=wh)
    print("\nAll above data saved to "+f,end='\n\n'); wh.close()
else:   print("No problem, Thank you! Have a nice day.\n")