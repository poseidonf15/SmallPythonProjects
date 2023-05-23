from tkinter import *

window = Tk()
window.geometry("300x400")
window.title("Encrypting")

main = LabelFrame(relief = FLAT)
main.pack(fill = X)

choose = LabelFrame(main, text = "Choose an encryption method")
choose.pack(side = TOP, pady = 10)

choice = IntVar()

radiocaesar = Radiobutton(choose, text = "Caeser", variable = choice, value = 0)
radiocaesar.pack(side = TOP, pady = 5, padx = 110)

radioatbash = Radiobutton(choose, text = "Atbash", variable = choice, value = 1)
radioatbash.pack(side = TOP, pady = 5, padx = 25)

radiocaesar_affine = Radiobutton(choose, text = "Caesar's affine",
                                 variable = choice, value = 2)
radiocaesar_affine.pack(side = TOP, pady = 5, padx = 70)

Data = LabelFrame(main, text = "Data", relief = GROOVE)
Data.pack(side = TOP, pady = 10)

label1 = Label(Data, text = "Enter text:")
label1.grid(row = 0, column = 0, padx = 10, pady = 5)

label2 = Label(Data, text = "Enter key:")
label2.grid(row = 0, column = 1)

label3 = Label(Data, text = "Enter key2:")
label3.grid(row = 0, column = 2, padx = 10, pady = 5)

plaintextbox = Entry(Data, width = 20, justify = "center")
plaintextbox.grid(row = 1, column = 0, padx = 10, pady = 5)

keybox = Entry(Data, width = 5, justify = "center") 
keybox.grid(row = 1, column = 1)

key2box = Entry(Data, width = 5, justify = "center") 
key2box.grid(row = 1, column = 2, padx = 10, pady = 5)

message = LabelFrame(main, text = "Encrypted messages", relief = GROOVE)
message.pack(side = TOP)

ciphername = Label(message, text = "Caesar's cipher:")
ciphername.pack(side = TOP, padx = 75 , pady = 10)

ciphermessage = Label(message, text = "")
ciphermessage.pack(side = TOP, pady = 10)

encryptB = Button(main, text = "Encrypt", width = 20)
encryptB.pack(side = TOP, pady = 5)

if __name__ == "__main__":
    window.mainloop()
