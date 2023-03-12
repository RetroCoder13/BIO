string = input().upper()
numbers = input()
steps,position = int(numbers.split(" ")[0]),int(numbers.split(" ")[1])

def stringToList(string):
    list = []
    for i in range(len(string)):
        list += [string[i]]
    return list

def listToString(list):
    string = ""
    for i in range(len(list)):
        string += list[i]
    return string

def replaceLetter(letter):
    if letter == "A":
        return "B"
    if letter == "B":
        return "AB"
    if letter == "C":
        return "CD"
    if letter == "D":
        return "DC"
    if letter == "E":
        return "EE"

for i in range(steps):
    # if(string == "EEE"):
    #     print("0 0 0 0 " + str(position))
    #     exit()
    list = stringToList(string)
    for i in range(len(list)):
        list[i] = replaceLetter(list[i])
    string = listToString(list)
    if(len(string)>position):
        string = string[0:position]

print(string.count("A",0,position),string.count("B",0,position),string.count("C",0,position),string.count("D",0,position),string.count("E",0,position))