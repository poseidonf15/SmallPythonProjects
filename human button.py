from tkinter import *

window = Tk()
window.geometry("700x700")

frame1 = LabelFrame(font = FLAT)
frame1.grid(row = 0, rowspan = 6, column = 0, columnspan = 4)

human = Button(frame1, text = "HUMAN", width = 15)
human.grid(row = 2, column = 2)

window.mainloop()
