num = int(input("Enter a number : "))
if (num%2 == num%3 == num%5 == 0) :
    print ("2,3 and 5")
elif (num%2 == num%3 == 0) :
    print ("2 and 3")
elif (num%2 == 0) :
    print ("2")
elif (num%2 != 0) and (num%3 != 0) and (num%5 != 0) :
    print ("0")




