from tkinter import *

window = Tk()
window.geometry("400x450")
window.title("password generator")

label = LabelFrame(text = "symbols")
label.pack(expand = True)
##Dont forget the brackets at the end of BooleanVar
lowercase = BooleanVar()
check_lowercase = Checkbutton(label, text = "abcdefghijklmnopqrstuvwxyz", variable = lowercase, offvalue = False, onvalue = True)
check_lowercase.grid(row = 1, column = 1, sticky = NW, pady = 10, padx = 20)

entry1 = Entry(label, justify = "center", width = 3)
entry1.grid(row = 1, column = 2, sticky = NE, pady = 10, padx = 20)
entry1.insert(0, "4")

numbers = BooleanVar()
check_numbers = Checkbutton(label, text = "0123456789", variable = numbers, offvalue = False, onvalue = True)
check_numbers.grid(row = 2, column = 1, sticky = NW, pady = 10, padx = 20)

entry2 = Entry(label, justify = "center", width = 3)
entry2.grid(row = 2, column = 2, sticky = NE, pady = 10, padx = 20)
entry2.insert(0, "4")

uppercase = BooleanVar()
check_uppercase = Checkbutton(label, text = "ABCDEFGHIJKLMNOPQRSTUVWYZ", variable = uppercase, offvalue = False, onvalue = True)
check_uppercase.grid(row = 3, column = 1, sticky = NW, pady = 10, padx = 20)

entry3 = Entry(label, justify = "center", width = 3)
entry3.grid(row = 3, column = 2, sticky = NE, pady = 10, padx = 20)
entry3.insert(0, "4")

symbols = BooleanVar()
check_symbols = Checkbutton(label, text = "!@#$%^&*()?<>`~-_", variable = symbols, offvalue = False, onvalue = True)
check_symbols.grid(row = 4, column = 1, sticky = NW, pady = 10, padx = 20)

entry4 = Entry(label, justify = "center", width = 3)
entry4.grid(row = 4, column = 2, sticky = NE, pady = 10, padx = 20)
entry4.insert(0, "4")

password_box = Listbox(label, justify = "center", height = 5, width = 30)
password_box.grid(row = 5, column = 1, columnspan = 2, padx = 30)

generate_password = Button(label, text = "Generate password")
generate_password.grid(row = 6, column = 1, columnspan = 2, pady = 5, padx = 25)

if __name__ == "__main__":
    window.mainloop()