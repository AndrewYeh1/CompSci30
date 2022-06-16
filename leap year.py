# Andrew Yeh
# Leap Year
# CompSci 30
# Sept 10th
# This program is my own work - A.Y.

year = int(input("Type in a year to find out if it is a leap year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year, "is a leap year.")
        else:
            print(year, "is not a leap year.")
    else:
        print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
