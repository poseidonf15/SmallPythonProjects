from tkinter import *
from tkinter import filedialog

window = Tk()
window.title("To-do list")
window.geometry("300x700")
window.resizable(False, False)

i = 1

def add():
    global i 
    text = f"{i}."
    text = text + " " + what.get()
    text = text + "\t" + "\t" + when.get() + "\n"
    todolist.insert(END, text)
    i += 1
    what.delete(0, END)
    when.delete(0, END)

def delete():
    todolist.delete(0.0, END)

def save():
    text = todolist.get(0.0, END)
    file = filedialog.asksaveasfile(title = "Save file",
                                    filetypes = (("txt files", "*.txt"),("all files","*.*")))
    if file:
        file.write(text)

def load():
    file = filedialog.askopenfile(title = "Select file",
                                  filetypes = (("txt files", "*.txt"),("all files","*.*")))
    text = file.read()

frame1 = LabelFrame(text = "Write down an important task")
frame1.pack(side = TOP, pady = 10, padx = 15)

label1 = Label(frame1, text = "New task")
label1.grid(row = 0, column = 0, padx = 30, pady = 10)

label2 = Label(frame1, text = "Until when")
label2.grid(row = 0, column = 1, padx = 30, pady = 10)

what = Entry(frame1, width = 20)
what.grid(row = 1, column = 0, padx = 5)

when = Entry(frame1, width = 20)
when.grid(row = 1, column = 1, padx = 5)

button1 = Button(frame1, text = "Create new important task", width = 20, command = add)
button1.grid(row = 2, column = 0, columnspan = 2, pady = 10)

todolist = Text(width = 40)
todolist.pack(side = TOP)

button2 = Button(text = "Delete all tasks", width = 15, command = delete)
button2.pack(side = TOP, pady = 20)

savebutton = Button(text = "Save", width = 10, command = save)
savebutton.pack(side = TOP, pady = 0)

loadbutton = Button(text = "Load", width = 10, command = load)
loadbutton.pack(side = TOP, pady = 20)

window.mainloop()
