from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Stock Checker")
root.geometry("300x200")

def check_stock():
    color = color_var.get()
    gender = gender_var.get()
    
    if color == "Red" and gender == "Men":
        status_label.config(text="Status: Out of Stock", foreground="red")
    else:
        status_label.config(text="Status: Available", foreground="green")


color_var = StringVar()
gender_var = StringVar()

l =Label(root, text="Color:")
l.pack()

color_combo = Combobox(root, textvariable=color_var, state="readonly")
color_combo['values'] = ("Red", "Black", "White")
color_combo.current(0)
color_combo.pack()

gender = Label(root, text="Gender:")
gender.pack()

men = Radiobutton(root, text="Men", variable=gender_var, value="Men")
men.pack()
women = Radiobutton(root, text="Women", variable=gender_var, value="Women")
women.pack()

gender_var.set("Men")
status_label = Label(root, text="Status: ", font=("Arial", 12))
status_label.pack(pady=10)

b = Button(root, text="Check Stock", command=check_stock)
b.pack()

root.mainloop()
