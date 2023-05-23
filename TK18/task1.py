from tkinter import *
import random

window = Tk()
window.title("tk")
window.geometry("250x375")
window.iconbitmap("alarm.ico")

alarmsnum = 10
newalarm = ""
change_window = ""

def generate_alarms():
    global alarmsnum
    alarmsnum = 10
    alarmbox.delete(0, END)
    alarms = []
    a = 0
    b = 5
    for i in range (10):
        num = random.randint(a,b)
        if (num < 10):
            clock = "07:0" + str(num)
        else:
            clock = "07:" + str(num)
        alarms.append(clock)
        a += 6
        b += 6
    alarmbox.insert(END, *alarms)
    size.config(text = sizex + str(alarmsnum))

def delete_alarms():
    global alarmsnum
    indexes = alarmbox.curselection()
    indexesSort = sorted(indexes, reverse = True)
    for index in (indexesSort):
        alarmsnum -= 1
        alarmbox.delete(index)
    size.config(text = sizex + str(alarmsnum))

def open_change_window():
    global newalarm
    global change_window
    
    change_window = Toplevel()
    change_window.title("Change")
    change_window.geometry("300x125")
    
    label1 = Label(change_window, text = "Enter new time")
    label1.pack(side = TOP, pady = 10)

    newalarm = Entry(change_window, width = 20)
    newalarm.pack(side = TOP)
    newalarm.insert(0, alarmbox.get(ACTIVE))

    savebutton = Button(change_window, text = "Save", width = 25, command = change_alarm)
    savebutton.pack(side = TOP, pady = 10)

def change_alarm():
    global newalarm
    global change_window
    alarmbox.insert(ACTIVE, newalarm.get())
    alarmbox.delete(ACTIVE)
    change_window.destroy()
    

title = Label(text = "Alarmclock")
title.pack(side = TOP, pady = 10)

sizex = "Number of alarmclocks: "
size = Label(text = "Number of alarmclocks: ")
size.pack(side = TOP, pady = 10)

alarmbox = Listbox(width = 30, height = 10, justify = CENTER, selectmode = EXTENDED)
alarmbox.pack(side = TOP, pady = 10)

randombutton = Button(text = "Random alarm", width = 30, command = generate_alarms)
randombutton.pack(side = TOP)

changebutton = Button(text = "Change the alarm", width = 30, command = open_change_window)
changebutton.pack(side = BOTTOM, pady = 10)

deletebutton = Button(text = "Delete an alarm", width = 30, command = delete_alarms)
deletebutton.pack(side = BOTTOM)

window.mainloop()
