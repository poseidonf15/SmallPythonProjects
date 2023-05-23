time = input("Enter here. : ")
if "p.m." in time:
    if (time[0:2] == "12"):
        print ("00:00")
    else:
        num = int(time[0:2]) + 12
        print (str(num) + ":00")

else:
    print (time[0:2] + ":00")
