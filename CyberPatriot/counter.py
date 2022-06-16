file = open("die.txt")
lines = file.readlines()

string = ""
for i in lines:
    string = string + i

totalList = string.split("attempted-recon")
print(len(totalList) - 1)
