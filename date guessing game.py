# Day of the Year guessing game

# list of dates in the year
import random

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
num_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# reformat a list of months and a list of days to become a massive list of every day in the year
def calendar(month_names, num_days_in_month):
    # checks if there is a corresponding amount of dates for every month
    if len(month_names) != len(num_days_in_month):
        return []

    dates = []
    idx = 0

    # loop for individually adding every day the the list "first"
    while idx < len(month_names):
        for date in range(1, num_days_in_month[idx] + 1):
            dates.append(month_names[idx] + " " + str(date))
        idx = idx + 1
    return dates

# runs the calender function to get the list of days
first = calendar(month_names, num_days_in_month)


def guess_game(first = calendar(month_names, num_days_in_month)):
    # finds the center of the list
    mid = len(first) // 2
    if first[mid] == "Jul 2":
        mid = random.randint(0, len(first) - 1)

    # gets the user input
    val = is_earlier(first[mid])

    if val == 1:
        # calls itself but this time with only the dates before the center
        return guess_game(first[:mid + 1])
    elif val == 2:
        # calls itself but this time with only the dates after the center
        return guess_game(first[mid - 1:])
    else:
        # computer guesses correctly
        return first[mid]


# takes the input and returns 1, 2 or 3 for earlier, later or equal and prints the date the computer guesses
def is_earlier(guess=10):
    return int(input("{}: 1 - earlier, 2 - later, 3 - equal?: ".format(guess)))


if __name__ == '__main__':
    print('Think of a specific date in any year')
    print('e.g., Jan 1 or Feb 29 or Jul 4 or Dec 25')
    print('Truthfully answer "Yes" or "No" to the following questions')
    print('I will determine the date in ten questions or less')

    print(guess_game())
