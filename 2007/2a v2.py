# Example win for X: XXOOOOXXE
#                     ^^^^^^

# currentPos = "EOOOOXXXX"
currentPos = "OXOEOXXOX"

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
    moves = []
    for i in range(4):
        listOfPos = stringToList(position)
        if(i == 0):
            nextLetterPos = firstLetterPos
        else:
            nextLetterPos = position.find(letter,nextLetterPos+1)

        listOfPos[emptyPos] = letter
        listOfPos[nextLetterPos] = "E"

        moves += [listToString(listOfPos)]

    return moves
        
        # newPosition = position.replace(position[emptyPos],position[nextLetterPos])
        # print(newPosition)

def stratOne(moves,letter):
    for move in moves:
        if letter == "X":
            if "XEX" in move[1:] and move[0] == letter:
                return move
        if letter == "O":
            if "OEO" in move[1:] and move[0] == letter:
                return move

def stratTwo(moves,opponentLetter):
    for move in moves:
        possibleOpponentMoves = possibleMoves(move, opponentLetter)
        if not stratOne(possibleOpponentMoves, opponentLetter):
            return move
    return moves[0]

def checkWin(position):
        if "XEX" in position[1:] and position[0] == "X":
            return position
        if "OEO" in position[1:] and position[0] == "O":
            return position

playerXMoves = possibleMoves(currentPos, "X")
if stratOne(playerXMoves, "X") == None:
    currentPos = stratTwo(playerXMoves, "O")
else:
    print("YOU WIN")

print(currentPos)

playerOMoves = possibleMoves(currentPos, "O")
if stratOne(playerOMoves, "O") == None:
    currentPos = stratTwo(playerOMoves, "O")
else:
    print("OPPONENT WIN")

print(currentPos)