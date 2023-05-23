from tkinter import *

window = Tk()
window.geometry("400x250")
window.title("Widgets and their argument")
window.resizable(False,False)

frame1 = LabelFrame(relief = FLAT, bg = "#7a249c", width = 40)
frame1.grid(pady = 20, padx = 40)

frame2 = LabelFrame(relief = FLAT, bg = "#7a249c", width = 60)
frame2.grid(pady = 10, padx = 40)

label1 = Label(frame1,text = " Lorem ipsum dolor sit amet, consectetur\n"
               "adipiscing elit. Sed sit amet ipsum\n"
               "sit amet eros auctor\n"
               "interdum.", justify = CENTER, relief = FLAT,
               bg = "#7a249c", fg = "white", width = 40, height = 5)
label1.grid(column = 0, columnspan = 2, padx = 10, pady = 5)

Button1 = Button(frame2, text = "Button 1", bg = "red", fg = "white", width = 15,)
Button1.grid(row = 1, column = 0, padx = 20, pady = 5)

Button2 = Button(frame2, text = "Button 2", bg = "green", fg = "white", width = 15,
                 activebackground = "blue", activeforeground = "yellow")
Button2.grid(row = 1, column = 1, padx = 20, pady = 5)

window.mainloop()
