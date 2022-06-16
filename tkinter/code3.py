from tkinter import *
from tkinter.font import ITALIC
from PIL import *
root = Tk()

root.geometry("500x400")
root.minsize(width=500, height=400)
root.maxsize(width=1920, height=1080)
root.title("Software Status!")
Label(text="READY", bg="green", fg="black", padx=5, pady=5, font="comicsansms 15 bold", borderwidth=5, relief=SUNKEN).pack(side=BOTTOM, fill=X, padx=5, pady=5)

root.mainloop()
