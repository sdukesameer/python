from tkinter import *
#from PIL import Image, ImageTk
root=Tk()

root.geometry("500x500")
root.minsize(width=500, height=500)
root.maxsize(width=1920, height=1080)

Label(text="This is my Album").pack()

'''photo=Image.open("pic1.jpg")
image=ImageTk.PhotoImage(photo)
Label(image=image).pack()'''

pic=PhotoImage(file="baloon.png")
Label(image=pic).pack()

root.mainloop()
