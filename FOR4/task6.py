import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
string = ""
num = (random.randint(1,28))

for i in range (0,num):
    string = string + alphabet[i]
    print (string)

answer = 30
while (answer != num):
    print ("")
    answer = int(input("How many words do you see? : "))
    if (answer != num):
        print ("Brong answer.")
print (f"Good job you right there is {num} word.")
    

