import random
n = int(input("Enter a number : "))
mylist = list()
for i in range (n):
    mylist.append(str(random.randint(1,100)))
print (mylist)
