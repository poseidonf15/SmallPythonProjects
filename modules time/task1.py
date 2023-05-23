import time

mylist = ["Actions speak louder than words.", 
            "You can't judge a book by its cover.", 
            "The early bird catches the worm.", 
            "Beauty is in the eye of the beholder."]

a = mylist[0]
b = mylist[1]
c = mylist[2]
d = mylist[3]
num = 0

print ("Typing speed check! Type the following sentence as fast as you can and I will time it for you...")
print ("")
time.sleep(2)
print ("Ready")
time.sleep(1)
print ("Set")
time.sleep(1)
print ("Go!")
print ("")

print (a)
start_time = time.time()
x = input()
end_time = time.time()
user_time = end_time - start_time

print ("")
print (f"You've typed {len(x)} characters in {user_time} seconds.")
print (f"It means your typing speed is {len(x) / user_time} characters per second.")
print ("")

if (x == a):
    print ("No mistakes!")
else:
    print ("You write it brong!")
    for i in range (0, len(a)):
        if (x[i] != a[i]):
            num += 1
            print (f"""You've made a mistake and wrote "{x[i]}" instead of "{a[i]}".""")
print (f"You have done {num} mistakes")

