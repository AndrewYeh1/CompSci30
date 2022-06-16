# Andrew Yeh
# Days of the Week
# CompSci 30
# Sept 14th
# This program is my own work - A.Y.

def count_days(current, future):
    current += future
    if current % 7 == 0:
        return "Sunday"
    elif current % 7 == 1:
        return "Monday"
    elif current % 7 == 2:
        return "Tuesday"
    elif current % 7 == 3:
        return "Wednesday"
    elif current % 7 == 4:
        return "Thursday"
    elif current % 7 == 5:
        return "Friday"
    elif current % 7 == 6:
        return "Saturday"

currentDay = int(input("What is the current day of the week? (0-6 0=Sunday) "))
while 0 >= currentDay or currentDay >= 7:
    currentDay = int(input("Invalid input. (0-6 0=Sunday) "))
amtOfDays = int(input("Input the amount of days after today you would like to find the day of the week for: "))
finalDay = count_days(currentDay, amtOfDays)
print(f"It is going to be {finalDay} after {amtOfDays} day(s).")
