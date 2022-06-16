from tkinter import *

def write():
    fd=open("file.txt","a")
    fd.write("--Student Details--\n")
    fd.write("Name: "+name.get()+"\n")
    fd.write("Roll No: "+roll.get()+"\n")
    fd.write("Stream: "+stream.get()+"\n")
    fd.write("Section: "+section.get()+"\n")
    fd.write("E-mail ID: "+email.get()+"\n")
    fd.write("Contact No: "+contact.get()+"\n\n")
    fd.close()
    Label(f4, text="Data Saved Successfully To file.txt!", bg="green", fg="white", font="comicsansms 10 bold",padx=130).pack(anchor="center", fill="x")

root=Tk()
root.geometry("380x290")
root.minsize(width=380, height=290)
root.maxsize(width=380, height=290)
root.title("Student Registration Form - By Sameer")

f1=Frame(root,bg="white",width=380,height=20)
f1.pack(side=TOP,pady=5)
f2=Frame(root,bg="white",width=380,height=210)
f2.pack(side=TOP,pady=5)
f3=Frame(root,bg="white",width=380,height=20)
f3.pack(side=TOP,pady=5)
f4=Frame(root,bg="white",width=380,height=20)
f4.pack(side=TOP,pady=5)

Label(f1,text="Student Registration Form",bg="blue",fg="red",font="comicsansms 10 bold",padx=130).pack(anchor="center",fill="x")

Label(f2,text="Name: ",padx=5,pady=5,font="comicsansms 10 bold").grid(row=0,column=0)
Label(f2, text="Roll No: ", padx=5, pady=5,font="comicsansms 10 bold").grid(row=1, column=0,)
Label(f2, text="Stream: ", padx=5, pady=5,font="comicsansms 10 bold").grid(row=2, column=0,)
Label(f2,text="Section: ",padx=5,pady=5,font="comicsansms 10 bold").grid(row=3,column=0,)
Label(f2, text="E-Mail ID: ", padx=5, pady=5,font="comicsansms 10 bold").grid(row=4, column=0,)
Label(f2, text="Contact No: ", padx=5, pady=5,font="comicsansms 10 bold").grid(row=5, column=0,)

name=StringVar()
roll=StringVar()
stream=StringVar()
section=StringVar()
email=StringVar()
contact=StringVar()

Entry(f2,width=30,font="comicsansms 10 bold",textvariable=name).grid(row=0,column=1)
Entry(f2,width=30,font="comicsansms 10 bold",textvariable=roll).grid(row=1,column=1)
Entry(f2,width=30,font="comicsansms 10 bold",textvariable=stream).grid(row=2,column=1)
Entry(f2,width=30,font="comicsansms 10 bold",textvariable=section).grid(row=3,column=1)
Entry(f2,width=30,font="comicsansms 10 bold",textvariable=email).grid(row=4,column=1)
Entry(f2,width=30,font="comicsansms 10 bold",textvariable=contact).grid(row=5,column=1)

Button(f3,text="Save to file!",bg="orange",fg="black",padx=5,pady=5,font="comicsansms 10 bold",command=write).pack(anchor="center",fill="x")

root.mainloop()
