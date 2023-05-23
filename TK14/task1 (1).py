from tkinter import *

window = Tk()
window.geometry("400x300")
window.resizable(False,False)
window.title("Data input-output")

def show():
    outputbox.delete(0, END)
    password = inputbox.get()
    outputbox.insert(END, password)

passwordbox = LabelFrame(text = "Password", width = 40, relief = RIDGE)
passwordbox.pack(expand = True)

label1 = Label(passwordbox, text = "Enter your password:")
label1.pack(side = TOP, pady = 5, padx = 20)

inputbox = Entry(passwordbox, bg = "black", fg = "white", font = "Helvetica",
               justify = CENTER, relief = RAISED, width = 13, state = NORMAL, show = "*")
inputbox.pack(side = TOP, padx = 20)

label2 = Label(passwordbox, text = "Your password")
label2.pack(side = TOP, pady = 5, padx = 20)

outputbox = Entry(passwordbox, width = 20, justify = CENTER)
outputbox.pack(side = TOP, padx = 20)

showbutton = Button(passwordbox, text = "Show", width = 15, command = show)
showbutton.pack(side = TOP, pady = 10, padx = 20)

window.mainloop()
