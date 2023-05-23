from tkinter import *
import random

window = Tk()
window.geometry("500x500")
window.title("Canvas")
window.resizable(False, False)

x = 150
y = 150
side = 100

canvas = Canvas(height  = 450, width = 450, relief = SOLID, bd = 1, bg = "white")
canvas.pack(expand = True)

for i in range (2000):
    x = random.randint(0, 450)
    y = random.randint(0, 450)
    side = random.randint(10, 50)
    canvas.create_oval(x, y, x + side, y + side,
                       fill = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}",
                       outline = f"#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}",
                       width = 3)
    window.update()

window.mainloop()
