from tkinter import *

window = Tk()
window.geometry("200x450")
window.title("Rainbow")
window.configure(bg = "white")

codes = ['#FF0000', '#FFA500', '#FFFF00', '#008000','#0000FF', '#000080', '#4B0082']
colors = ["red", "orange", "yellow", "green","light blue", "blue", "violet"] 

def change_text(x):
    global codes
    global colors
    color_name.config(text = colors[x])
    color_code.config(text = codes[x])

color_name = Label(font = "Arial,14", bg = ("#ffffff"), width = 20, height = 2)
color_name.pack(side = TOP)

color_code = Label(font = "Arial,14", bg = ("#ffffff"), width = 20, height = 2)
color_code.pack(side = TOP, pady = 5)

for i in range (0, 7):
    button = Button(width = 25, height = 2, bg = codes[i], command = lambda index = i: change_text(index))
    button.pack(side = TOP)

window.mainloop()
