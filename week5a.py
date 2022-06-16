def grade(g):
    if g=="A":
        x=10
    elif g=="AB":
        x=9
    elif g=="B":
        x=8
    elif g=="BC":
        x=7
    elif g=="C":
        x=6
    elif g=="CD":
        x=5
    elif g=="D":
        x=4
    return (x)
(f,students,grades)=(0,[],[])
while(1):
    inp=input()
    if inp=="EndOfInput":
        break
    if inp=="Courses":
        f=1
        continue
    if inp=="Students":
        f=2
        continue
    if inp=="Grades":
        f=3
        continue
    if f==2:
        students.append(inp)
    if f==3:
        grades.append(inp)
for i in range(len(students)):
    students[i]=students[i].split("~")
for i in range(len(grades)):
    grades[i]=grades[i].split("~")
students=sorted(students)
print
for i in range(len(students)):
    avg=0.0
    (total,count)=(0,0)
    for j in grades:
        if students[i][0] in j:
            count=count+1
            total=total+grade(j[4])
    if count == 0:
        students[i].append("0")
    else:
        avg=round(total/count,2)
        students[i].append(str(avg))
for i in range(len(students)):
    students[i]="~".join(students[i])
    print(students[i])