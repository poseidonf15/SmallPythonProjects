num = int(input("Enter here. : "))
num2 = int(input("Enter here. : "))

for i in range (num,num2+1):
    if (i % 3 == 0 and i % 5 == 0):
        print ("FizzBuzz")
    elif (i % 3 == 0):
        print ("Fizz")
    elif (i % 5 == 0):
        print ("Buzz")
    else:
        print(i)
