from tkinter import *

root = Tk()
root.title("Area Calculator")
root.geometry("200x150")

def calculate():
    l = int(l_e.get())
    w = int(w_e.get())
    final = l*w
    output.config(text=f"Area: {final} sq units")

length = Label(root,text = "Length:")
length.place(x=10,y=10)

width = Label(root,text= "Width:")
width.place(x=10,y=40)

l_e = Entry(root,width = 20)
l_e.place(x=55,y=10)

w_e = Entry(root,width = 20)
w_e.place(x=55,y=40)

btn = Button(root,text = "Calculate Area",bg = "orange",command = calculate)
btn.place(x=40,y=80)

output = Label(root,text = "",font = ("bold",10))
output.place(x=20,y=120)



root.mainloop()