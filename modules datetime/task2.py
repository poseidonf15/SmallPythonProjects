import datetime

year = int(input("Enter the year of birth: "))
month = int(input("Enter the month of birth: "))
day = int(input("Enter the day of birth: "))

difference = datetime.datetime.today() - datetime.datetime(year, month, day)
print (f"From birthday to today passed {difference.days} days")

