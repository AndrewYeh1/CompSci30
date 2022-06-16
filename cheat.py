dataList = []

dataType = input("Select data type: ")
raw = input("Please input shit: ")
if dataType == "f":
    raw = raw.split(",")

    for i in range(int(len(raw)/2)):
        for j in range(int(raw[i * 2])):
            dataList.append(int(raw[i * 2 + 1]))
elif dataType == "fs":
    dataList = raw.split(", ")
    dataList = list(map(int, dataList))
elif dataType == "fn":
    dataList = raw.split(",")
    dataList = list(map(int, dataList))

devList = []
avg = sum(dataList)/len(dataList)
print("The average is:", avg)

for i in dataList:
    devList.append((i - avg)**2)

print("The standard deviation is:", (sum(devList)/len(devList))**0.5)
