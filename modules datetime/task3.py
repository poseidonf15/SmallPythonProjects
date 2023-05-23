import datetime

year = int(input("Enter a year: "))
a = datetime.date(year, 1, 1)
num = 0

for month in range (1, 13):
    if datetime.date(year, month, 13).weekday() == 4:
        print (f"Fridey the 13th is found: {year}-{month}-13")
        num += 1

print (f"In 2020 discovered {num} Fridays the 13th")
    
    
