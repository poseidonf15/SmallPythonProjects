from tkinter import *

window = Tk()
window.geometry("500x600")
window.title("Widget positioning")

frame3 = LabelFrame(text = "Place", width = 300, height = 100)
frame3.pack(side = TOP)

Button30 = Button(frame3, text = "Button30", bg = "black", fg = "white", width = 10)
Button30.place(x = 60, y = 0)

Button31 = Button(frame3, text = "Button31", bg = "black", fg = "white", width = 10)
Button31.place(x = 175, y = 50)

frame2 = LabelFrame(text = "Grid")
frame2.pack(side = TOP)
frame2.pack(padx=50)

Button20 = Button(frame2, text = "Button20", bg = "black", fg = "white", width = 30)
Button20.grid(column = 0, columnspan = 2, row = 0, padx = 10, pady = 10)

Button21 = Button(frame2, text = "Button21", bg = "black", fg = "white", width = 10)
Button21.grid(column = 0, row = 1, padx = 10, pady = 10)

Button22 = Button(frame2, text = "Button22", bg = "black", fg = "white", width = 10, height = 8)
Button22.grid(column = 1, row = 1, rowspan = 3, padx = 10, pady = 10)

Button23 = Button(frame2, text = "Button23", bg = "black", fg = "white", width = 10)
Button23.grid(column = 0, row = 2, padx = 10, pady = 10)

Button24 = Button(frame2, text = "Button24", bg = "black", fg = "white", width = 10)

Button25 = Button(frame2, text = "Button25", bg = "black", fg = "white", width = 10)
Button25.grid(column = 0, row = 3, padx = 10, pady = 10)

frame1 = LabelFrame(text = "Pack", width = 300, height = 100)
frame1.pack(side = TOP)
frame1.pack(padx=50)

Button10 = Button(frame1, text = "Button10", bg = "black", fg = "white", width = 10)
Button10.pack(pady = 10, padx = 10, side = LEFT)

Button11 = Button(frame1, text = "Button11", bg = "black", fg = "white", width = 10)
Button11.pack(pady = 10, padx = 10, side = LEFT)

Button12 = Button(frame1, text = "Button12", bg = "black", fg = "white", width = 10)
Button12.pack(pady = 10, padx = 10, side = LEFT)

Quit = Button(text = "Quit Button", bg = "black", fg = "white", width = 30, command = quit)
Quit.pack(side = BOTTOM)

window.mainloop()

