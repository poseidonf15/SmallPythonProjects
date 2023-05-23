from tkinter import *

window = Tk()
window.geometry("400x300")
window.resizable(False,False)
window.title("Data input-output")

def check():
    texts = "Password is OK!"
    digitchecking = False
    upperchecking = False
    lowerchecking = False
    
    password = inputbox.get()
    for symbol in password:
        if (symbol.isdigit()):
            digitchecking = True
    for symbol in password:
        if (symbol.islower()):
            upperchecking = True
    for stmbol in password:
        if(stmbol.isupper()):
            lowerchecking = True

    if (digitchecking and upperchecking and lowerchecking):
        label2.config(fg = "green")
    else:
        label2.config(fg = "red")
        texts = ""
    if (digitchecking):
        stupid = 0
    else:
        texts = "There are not enough numbers "
    if (lowerchecking):
        stupid = 0
    else:
        texts = texts + "\nThere are not enough lowercase letters "
    if (upperchecking):
        stupid = 0
    else:
        texts = texts + "\nThere are not enough uppercase letters"
    if (digitchecking or upperchecking or lowerchecking):
        stupid = 0
    else:
        texts = "Several conditions for the password are not met"
    label2.config(text = texts)


def theme():
    window["bg"] = ("#353535")
    passwordbox.config(bg = "#353535", fg = "white")
    label1.config(bg = "#353535", fg = "white")
    checkbutton.config(bg = "#535353", fg = "white")
    themebutton.config(bg = "#535353", fg = "white", state = DISABLED)
    label2.config(bg = "#353535", fg = "white")
    
passwordbox = LabelFrame(text = "Password", width = 40, relief = RIDGE)
passwordbox.pack(expand = True)

label1 = Label(passwordbox, text = "Enter your password:")
label1.pack(side = TOP, pady = 5, padx = 20)

inputbox = Entry(passwordbox, bg = "black", fg = "white", font = "Helvetica",
                 justify = CENTER, relief = RAISED, width = 13, state = NORMAL, show = "*")
inputbox.pack(side = TOP, padx = 20)

label2 = Label(passwordbox, text = "")
label2.pack(side = TOP, pady = 5, padx = 20)

checkbutton = Button(passwordbox, text = "Check the password", width = 15, command = check)
checkbutton.pack(side = TOP, pady = 10, padx = 20)

themebutton = Button(passwordbox, text = "Change theme", command = theme)
themebutton.pack(side = TOP, pady = 10, padx = 20)

window.mainloop()
