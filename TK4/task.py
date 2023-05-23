from tkinter import *

window = Tk()
drawing = Canvas(window, height = 100, width = 300, bg = "grey")
drawing.pack()

def oval_change(event):
    drawing.delete(oval)
    drawing.create_text(65, 55, text = "Oval was here")

def rectangle_change(event):
    drawing.delete(rectangle)
    drawing.create_text(165, 55, text = "Rectangle was here")

def polygon_change(event):
    drawing.create_polygon(260, 30, 230, 80, 285, 80, outline = "black" , fill = "yellow")

oval = drawing.create_oval(25, 20, 105, 90, outline = "black" , fill = "orange", tag = "rect")

rectangle = drawing.create_rectangle(130, 20, 200, 90, outline = "black" , fill = "green")

polygon = drawing.create_polygon(260, 20, 220, 90, 295, 90, outline = "black" , fill = "white")

drawing.tag_bind(oval, "<Button>", oval_change)

drawing.tag_bind(rectangle, "<Button>", rectangle_change)

drawing.tag_bind(polygon, "<Button>", polygon_change)

window.mainloop()
