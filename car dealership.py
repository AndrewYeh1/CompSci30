# Andrew Yeh
# Car Dealership
# CompSci 30
# Dec 7th
# This program is my own work - A.Y.

class Car:
    def __init__(self, make, model, year, odometer, color, price):
        self.dataSet = []
        self.dataSet.append(make)
        self.dataSet.append(model)
        self.dataSet.append(year)
        self.dataSet.append(odometer)
        self.dataSet.append(color)
        self.dataSet.append(price)

    def get_data(self, num):
        return self.dataSet[num]

    def set_data(self, num, data):
        self.dataSet[num] = data


def create_list():
    list = []
    list.append(Car("Lexus", "LFA", 2005, 10000, "Yellow", 1000000))
    list.append(Car("Lancia", "Stratos", 1975, 15000, "Black", 1200000))
    list.append(Car("Pagani", "Zonda R", 2007, 1234, "Black", 9000000))
    list.append(Car("Nissan", "GTR", 1999, 12030, "Blue", 312000))
    list.append(Car("Koenigsegg", "Jesko Absolut", 2021, 0, "Orange", 4000000))
    list.append(Car("Lotus", "Carlton", 1991, 123456, "Green", 50000))
    return list


def search_list(list):
    searchType = int(input("How would you like to search? (1, for specific car) (2, for largest value) (3, for smallest value) (4, all) "))
    if searchType == 1:
        searchItem = int(input("Which car would you like to search for? (1-6) "))
        for j in range(6):
            print(list[searchItem - 1].get_data(j), end=" ")
        print()
    if searchType == 2 or searchType == 3:
        searchItem = int(input("Which value would you like to search for? (3, year) (4, odometer) (6, price) "))
        searchItemTable = {3: "year", 4: "odometer", 6: "price"}
        if searchItem == 3 or searchItem == 4 or searchItem == 6:
            searchList = [x.get_data(searchItem - 1) for x in list]
            if searchType == 2:
                value = max(searchList)
                ind = searchList.index(value)
                print(f"The {list[ind].get_data(0)} {list[ind].get_data(1)} has the highest {searchItemTable[searchItem]} at the value of {value}.")
            else:
                value = min([x.get_data(searchItem - 1) for x in list])
                ind = searchList.index(value)
                print(f"The {list[ind].get_data(0)} {list[ind].get_data(1)} has the lowest {searchItemTable[searchItem]} at the value of {value}.")
    elif searchType == 4:
        for i in range(6):
            for j in range(6):
                print(list[i].get_data(j), end=" ")
            print()


carList = create_list()
search_list(carList)



