num = int(input("Enter here. : "))
x = 0
for i in range (1,num + 1):
    if (num % i == 0):
        print (i,end=" ")
        x += 1
print ("")
if (x > 2):
    print ("NO")
else:
    print ("PRIME")
    
