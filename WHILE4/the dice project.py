import random

num = input("Play? ")


while (num != "0"):
    if (num == "1"):
            print ("First dice: ",(random.randint(1,6)))
            print ("Second dice: ",(random.randint(1,6)))   

    elif (num == "2"):
        print ("First dice: ",(random.randint(1,20)))
        print ("Second dice: ",(random.randint(1,20)))
        print ("Third dice: ",(random.randint(1,20)))

    elif (num == "3"):
        num2 = 1
        while (num2 < 101):
            print (f"Dice number {num2}: ",(random.randint(1,6)))
            num2 += 1

    else:
        print ("Wrong input, try again.")

    num = input("Play? ")
        
        
    
