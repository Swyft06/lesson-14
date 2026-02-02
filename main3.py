from tkinter import *
import random
root = Tk()
root.title("Dice Roller")
root.geometry("300x300")

def roll():
    number = random.randint(1,6)
    num.config(text = str(number))

title = Label(root,text = "Roll the Dice!",font = ("bold",25))
title.pack(pady=10)

num = Label(root,text = "",font = ("bold",50))
num.place(x=125,y=100)

btn = Button(root,text = "ROLL",bg= "light blue",width = 10,command = roll)
btn.pack(side = BOTTOM,pady = 20)

root.mainloop()
