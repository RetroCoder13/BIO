startingPos = "EOOOOXXXX"
possibleMoves = []

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

def possibleMoves(position,letter):
    firstLetterPos = position.find(letter)
    emptyPos = position.find("E")
    for i in range(4):
        listOfPos = stringToList(position)
        if(i == 0):
            nextLetterPos = firstLetterPos
        else:
            nextLetterPos = position.find(letter,nextLetterPos+1)

        listOfPos[emptyPos] = letter
        listOfPos[nextLetterPos] = "E"

        print(listToString(listOfPos))
        
        # newPosition = position.replace(position[emptyPos],position[nextLetterPos])
        # print(newPosition)

possibleMoves(startingPos, "X")