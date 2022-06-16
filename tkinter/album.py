from tkinter import *
root = Tk()

root.geometry("1500x700")
root.title("My Album by Sameer!")
Label(text="Baloon", bg="yellow", fg="black", font="comicsansms 10 bold",padx=130,pady=5).grid(row=0,column=0,padx=5,pady=5)
Label(text="Dice", bg="red", fg="yellow", font="comicsansms 10 bold",padx=130, pady=5).grid(row=0, column=1, padx=5, pady=5)
Label(text="Heart", bg="orange", fg="green", font="comicsansms 10 bold",padx=130, pady=5).grid(row=0, column=2, padx=5, pady=5)
Label(text="Spiderman", bg="black", fg="red", font="comicsansms 10 bold",padx=120, pady=5).grid(row=0, column=3, padx=5, pady=5)

Label(text="Earth", bg="blue", fg="white", font="comicsansms 10 bold",padx=130, pady=5).grid(row=2, column=0, padx=5, pady=5)
Label(text="Meme", bg="green", fg="pink", font="comicsansms 10 bold",padx=130, pady=5).grid(row=2, column=1, padx=5, pady=5)
Label(text="Puzzle", bg="white", fg="indigo", font="comicsansms 10 bold",padx=130, pady=5).grid(row=2, column=2, padx=5, pady=5)
Label(text="Apple", bg="indigo", fg="orange", font="comicsansms 10 bold",padx=130, pady=5).grid(row=2, column=3, padx=5, pady=5)

p1 = PhotoImage(file="baloon.png", height=300, width=300)
p2 = PhotoImage(file="dice.png", height=300, width=300)
p3 = PhotoImage(file="heart.png", height=300, width=300)
p4 = PhotoImage(file="spider.png", height=300, width=300)

p5 = PhotoImage(file="earth.png", height=300, width=300)
p6 = PhotoImage(file="meme.png", height=300, width=300)
p7 = PhotoImage(file="puzzle.png", height=300, width=300)
p8 = PhotoImage(file="apple.png", height=300, width=300)

Label(image=p1).grid(row=1, column=0, padx=5, pady=5)
Label(image=p2).grid(row=1, column=1, padx=5, pady=5)
Label(image=p3).grid(row=1, column=2, padx=5, pady=5)
Label(image=p4).grid(row=1, column=3, padx=5, pady=5)

Label(image=p5).grid(row=3, column=0, padx=5, pady=5)
Label(image=p6).grid(row=3, column=1, padx=5, pady=5)
Label(image=p7).grid(row=3, column=2, padx=5, pady=5)
Label(image=p8).grid(row=3, column=3, padx=5, pady=5)

root.mainloop()
