import random
print ("Hello dear player.\nThis is a game where you need to guess the number what the computer choose for you.\nin the start you get 50 coins.\nevery your fail atempt you get minus 10 coins.\nevery time you guees the number you get 50 coins.\nwhen you get 200 coins you win.\n\nthere are three difficultys easy (from 1 to 10) normal (from 1 to 20) and hard (from 1 to 50)")
choose = input("""choose the difficulty "easy" "normal" or "hard". : """)

coins = 50
x = 0

while (coins > 0):
    if (choose == "easy"):
        random_num = (random.randint(1,10))
    elif (choose == "normal"):
        random_num = (random.randint(1,20))
    elif (choose == "hard"):
        random_num = (random.randint(1,50))
    
    while (x != random_num):
        try:
            x = int(input("Enter the number: "))
        except ValueError:
            x =  int(input("Enter an Integer number: "))
        if (x < random_num):
            print ("The number is bigger")
        elif (x > random_num):
            print ("The number is smaller")
        else:
            print ("good job that was the number")
            coins += 50
            print (f"your balance is {coins} coins\n")
            break
        coins -= 10
        print (f"your balance is {coins} coins\n")

print ("You win :D")
