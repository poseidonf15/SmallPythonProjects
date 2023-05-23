import random

from_num = int(input("From what number should I guess? "))
to_num = int(input("Until what number should I guess? "))
secret = (random.randint(from_num,to_num))

x = secret - 1
try_num = 0
a = "yes"

while (a == "yes"):
    x = int(input("Enter number: "))
    while (x != secret):
        try_num += 1
        if (secret > x):
            print("The secret number is bigger")
        elif (secret < x):
            print("The secret number is less")
        x = int(input("Enter number: "))
    try_num += 1
    print(f"Hurrah! You guessed! It took {try_num} tries")
    a = input("Play again? ")
    
