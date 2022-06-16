from tkinter import *

def f1():
    print("Button 1 pressed")
def f2():
    print("Button 2 pressed")
def f3():
    print("Button 3 pressed")
def f4():
    print("Button 4 pressed")
def f5():
    print("Button 5 pressed")

root=Tk()
root.geometry("500x500")

f=Frame(root,bg='grey',width=500,height=500)
f.pack(side=LEFT,anchor="nw",fill='x')

b1 = Button(f, text="Button 1", bg='white', fg='red', padx=5,pady=5, font="comicsansms 10 bold", borderwidth=5,command=f1)
b2 = Button(f, text="Button 2", bg='white', fg='blue', padx=5,pady=5, font="comicsansms 10 bold", borderwidth=5,command=f2)
b3 = Button(f, text="Button 3", bg='white', fg='green', padx=5,pady=5, font="comicsansms 10 bold", borderwidth=5,command=f3)
b4 = Button(f, text="Button 4", bg='white', fg='orange' ,padx=5,pady=5, font="comicsansms 10 bold", borderwidth=5,command=f4)
b5 = Button(f, text="Button 5", bg='white',fg='black', padx=5,pady=5, font="comicsansms 10 bold", borderwidth=5,command=f5)

b1.pack(side=LEFT,padx=10)
b2.pack(side=LEFT,padx=10)
b3.pack(side=LEFT,padx=10)
b4.pack(side=LEFT,padx=10)
b5.pack(side=LEFT,padx=10)

root.mainloop()
