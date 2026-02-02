from tkinter import *

root = Tk()
root.title("Discount App")
root.geometry("300x300")

def calculate():
    original = int(en1.get())
    discount = int(en2.get())
    amount_saved = original*(discount/100)
    saved.configure(text = f"${amount_saved}")
    price = original - amount_saved
    final.configure(text =f"${price}")


op = Label(root,text = "Original Price($):")
op.place(x=10,y=10)

dis = Label(root,text = "Discount(%):")
dis.place(x=10,y=40)

en1 = Entry(root,width = 20)
en1.place(x=100,y=10)

en2 = Entry(root,width=20)
en2.place(x=100,y=40)

btn = Button(root,text= "Caluclate",bg = 'yellow',command = calculate)
btn.place(x=50,y=100)

ams = Label(root,text  = "Amount Saved:")
ams.place(x=10,y=150)

fp = Label(root,text ="Final Price:")
fp.place(x=10,y=180)

saved = Label(root,text = "",width = 10)
saved.place(x=90,y=150)

final = Label(root,text="",width = 10)
final.place(x=90,y=180)


root.mainloop()