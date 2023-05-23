from tkinter import *
from math import sqrt
from tkinter import messagebox

window = Tk()
window.geometry("300x300")
window.title("Equations solver")

def equate(event):
    output.delete(0.0, END)
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())
        c = int(entry_c.get())
        answer = messagebox.askyesno("Checkup", f"Are you sure you want to solve the equation \nwith the values {a}, {b} and {c}?")
        if (answer):
            D = b**2 - 4 * a * c
            if (D >= 0):
                x1 = (-b + sqrt(D)) / (2 * a)
                x2 = (-b - sqrt(D)) / (2 * a)
                output.insert(END, f"""Discriminant is {D}
x1 = {x1}
x2 = {x2}""")
            else:
                output.insert(END, f"""Discriminant is {D}
The equation has no solution.""")
    except(ValueError):
        output.insert(END, "Make sure you entered \n3 numbers!")

def cleaning(event):
     event.widget.delete(0, END)
    

Enter = LabelFrame(text = "Enter intial data", relief = SUNKEN)
Enter.pack(side = TOP, padx = 20, pady = 10)

entry_a = Entry(Enter , width = 3)
entry_a.pack(side = LEFT, padx = 25, pady = 10)

label1 = Label(Enter, text = "x**2 +")
label1.pack(side = LEFT, pady = 10)

entry_b = Entry(Enter , width = 3)
entry_b.pack(side = LEFT, padx = 10, pady = 10)

label2 = Label(Enter, text = "x +")
label2.pack(side = LEFT, pady = 10)

entry_c = Entry(Enter , width = 3)
entry_c.pack(side = LEFT, padx = 10, pady = 10)

label3 = Label(Enter, text = "= 0")
label3.pack(side = LEFT, padx = 10, pady = 10)

solution = LabelFrame(text = "Solution", relief = SUNKEN)
solution.pack(side = TOP, padx = 20)

output = Text(solution, width = 220, height = 5)
output.pack(side = TOP, padx = 10, pady = 10)

window.bind("<Return>", equate)
entry_a.bind("<FocusIn>", cleaning)
entry_b.bind("<FocusIn>", cleaning)
entry_c.bind("<FocusIn>", cleaning)
window.bind("<Control-Key-1>", lambda event: entry_a.focus())
window.bind("<Control-Key-2>", lambda event: entry_b.focus())
window.bind("<Control-Key-3>", lambda event: entry_c.focus())

window.mainloop()
