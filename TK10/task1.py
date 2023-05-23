from tkinter import *

window = Tk()
window.geometry("600x400")
window.title("My program")

close = Button(text="Click me", width = 20, command=quit)
close.pack(expand=True)

window.mainloop()
