# Andrew Yeh
# CIA Fact Finder
# CompSci 30
# Nov 15th
# This program is my own work - A.Y.

def search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def top25():
    file = open("countries")
    countriesRaw = file.readlines()
    for i in range(len(countriesRaw)):
        countriesRaw[i] = countriesRaw[i].strip('\n')

    file.close()
    return countriesRaw


def readFiles():
    # read files
    file = open("birth_rate", 'r')
    birthRateRaw = file.readlines()[1:]
    birthRate = []
    for line in birthRateRaw:
        birthRate.append([line.split("\t")[0], line.split("\t")[1], line.split("\t")[2].strip('\n')])

    file = open("gdp", 'r')
    gdpRaw = file.readlines()[1:]
    gdp = []
    for line in gdpRaw:
        gdp.append([line.split("\t")[0], line.split("\t")[1].strip('"'), line.split("\t")[2].strip('\n')])

    file = open("population", 'r')
    populationRaw = file.readlines()[1:]
    population = []
    for line in populationRaw:
        population.append([line.split("\t")[0], line.split("\t")[1].strip('"'), line.split("\t")[2].strip('\n')])

    file = open("unemployment", 'r')
    unemploymentRaw = file.readlines()[1:]
    unemployment = []
    for line in unemploymentRaw:
        unemployment.append([line.split("\t")[0], line.split("\t")[1], line.split("\t")[2].strip('\n')])

    countriesRaw = top25()

    file.close()

    # extract data for top 25 countries
    countryList = []
    for country in range(len(countriesRaw)):
        if (search([item[0] for item in birthRate], countriesRaw[country])) != -1:
            countryList.append([countriesRaw[country], birthRate[search([item[0] for item in birthRate], countriesRaw[country])][1]])
        else:
            countryList.append([countriesRaw[country], "unknown"])
        if (search([item[0] for item in gdp], countriesRaw[country])) != -1:
            countryList[country].append(gdp[search([item[0] for item in gdp], countriesRaw[country])][1])
        else:
            countryList[country].append("unknown")
        if (search([item[0] for item in population], countriesRaw[country])) != -1:
            countryList[country].append(population[search([item[0] for item in population], countriesRaw[country])][1])
        else:
            countryList[country].append("unknown")
        if (search([item[0] for item in unemployment], countriesRaw[country])) != -1:
            countryList[country].append(unemployment[search([item[0] for item in unemployment], countriesRaw[country])][1])
        else:
            countryList[country].append("unknown")

    return countryList


def findData(countryList):
    target = input("Which country would you like to search for? ")
    top25Countries = top25()
    while search(top25Countries, target) == -1:
        target = input("Invalid, try again. ")
    index = search([item[0] for item in countryList], target)
    print("What data would you like to search for?")
    print("(1, Birth Rate)(2, GDP)(3, Population)(4, Unemployment)")
    print("You can search for multiple values at the same time.")
    request = input('Example: "2" "13" "134" ')
    while (not request.isnumeric()) or (len(request) > 4 or len(request) < 1):
        request = input("Invalid, try again. ")
    try:
        for i in request:
            if int(i) == 1:
                print("Birth Rate:")
            elif int(i) == 2:
                print("GDP:")
            elif int(i) == 3:
                print("Population:")
            else:
                print("Unemployment:")
            print(countryList[index][int(i)])
    except:
        print("Failed, invalid input. ")


if __name__ == "__main__":
    dataList = readFiles()
    go = 'y'
    while go == 'y':
        findData(dataList)
        go = input('Use again? ("y" or "n") ')
        while go != "y" and go != "n":
            go = input('Invalid ("y" or "n") ')
