from tkinter import *

window = Tk()
window.title("Color picker")
window.geometry("550x300")

def color_generate(value):
    red = red_scale.get()
    green = green_scale.get()
    blue = blue_scale.get()
    color = f"#{red:02x}{green:02x}{blue:02x}"
    color2 = f"#{225 - red:02x}{225 - green:02x}{225 - blue:02x}"
    label_color.config(bg = color, text = str(color), fg = color2)
    copy_color.delete(0, END)
    copy_color.insert(0, str(color))

frame_RGB = LabelFrame(text = "Choose colors", height = 250, width = 250)
frame_RGB.place(x = 15, y = 30)

frame_color = LabelFrame(text = "Result color", height = 250, width = 250)
frame_color.place(x = 285, y = 30)

label_color = Label(frame_color, font = ("Arial", 15, "bold"), height = 8, width = 16)
label_color.place(x = 20, y = 20)

copy_color = Entry(frame_color, font = ("Arial", 15, "bold"), width = 7)
copy_color.place(x = 77, y = 170)

label_red = Label(frame_RGB, text = "Red", fg = "red")
label_red.place(x = 15, y = 3)

red_scale = Scale(frame_RGB, from_ = 0, to = 225, orient = HORIZONTAL, length = 215,
                  activebackground = "red", command = color_generate)
red_scale.place(x = 10, y = 20)

label_green = Label(frame_RGB, text = "Green", fg = "green")
label_green.place(x = 15, y = 63)

green_scale = Scale(frame_RGB, from_ = 0, to = 225, orient = HORIZONTAL, length = 215,
                  activebackground = "green", command = color_generate)
green_scale.place(x = 10, y = 80)

label_blue = Label(frame_RGB, text = "Blue", fg = "blue")
label_blue.place(x = 15, y = 123)

blue_scale = Scale(frame_RGB, from_ = 0, to = 225, orient = HORIZONTAL, length = 215,
                  activebackground = "blue", command = color_generate)
blue_scale.place(x = 10, y = 140)

window.mainloop()
