from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x300")
window.title("Problem solver")

def equate():
    try:
        solution = eval(equation.get())
        messagebox.showinfo("Done!", f"Solution was found: {solution}")
    except SyntaxError:
        messagebox.showwarning("Attention!", "You missed something, revise the example")
    except NameError:
        messagebox.showerror("Error!", "You wrote something completely incorrect.")
    except ZeroDivisionError:
        messagebox.showwarning("Are you serious?", "Are you dividing by zero?")
    

frame = LabelFrame(text = "", relief = FLAT)
frame.pack(side = TOP, pady = 65)

label = Label(frame, text = "Enter math expression using thee following sings: \n\n+ - * / // % **")
label.pack(side = TOP)

equation = Entry(frame, justify = CENTER, width = 35)
equation.pack(side = TOP, pady = 15)

button = Button(frame, text = "Solve", width = 25, command = equate)
button.pack(side = TOP)

window.mainloop()
