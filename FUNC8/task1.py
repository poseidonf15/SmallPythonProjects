import random
import time

def display_Intro():
    print ("")
    print ("""You are in a land full of dragons. In front of you, you see two caves.
In one cave, the dragon is friendly and will share his treasure with you.
The other dragon is greedy and hungry and wants to eat you.""")
    print ("")

answer = 3
def choose_Cave():
    global answer
    while (answer != 1 and answer != 2):
        answer = int(input("Choose 1 or 2: "))
        print ("")
    return answer
    
def check_Cave(choose_Cave):
    global answer
    answer = 3
    print ("You are approaching a cave…")
    time.sleep(2)
    print ("It's dark and creepy.…")
    time.sleep(2)
    print ("A large dragon jumps out in front of you! \nHe opens his jaws and…")
    print ("")
    time.sleep(2)
    chance = random.randint(1,2)

    if (choose_Cave == chance):
        print ("Dragon gives you his treasure")
    else:
        print ("the Dragon eats you in one bite")

a = "yes"
while (a == "yes"):
    display_Intro()
    check_Cave(choose_Cave())
    print ("")
    a = input("Do you want to play more? \n")
    
