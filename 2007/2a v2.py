# Example win for X: XXOOOOXXE
#                     ^^^^^^

# currentPos = "EOOOOXXXX"
# currentPos = "OEOXOXXOX"
currentPos = input().upper()

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
    # firstLetterPos = position.find(letter)
    firstLetterPos = position.find(letter)
    emptyPos = position.find("E")
    moves = []
    # for i in range(4):
    #     listOfPos = stringToList(position)
    #     if(i == 0):
    #         nextLetterPos = firstLetterPos
    #     else:
    #         nextLetterPos = position.find(letter,nextLetterPos+1)

    #     listOfPos[emptyPos] = letter
    #     listOfPos[nextLetterPos] = "E"

    #     moves += [listToString(listOfPos)]

    for i in range(4):
        if(i == 0):
                nextLetterPos = firstLetterPos
        else:
            nextLetterPos = position.find(letter,nextLetterPos+1)
        listOfPos = stringToList(position)
        try:
            if(emptyPos==8):
                if(nextLetterPos==1 or nextLetterPos==emptyPos-1 or nextLetterPos==0):
                    listOfPos[emptyPos] = letter
                    listOfPos[nextLetterPos] = "E"
                    moves += [listToString(listOfPos)]
            elif(emptyPos==1):
                    if(nextLetterPos==emptyPos+1 or nextLetterPos==8 or nextLetterPos==0):
                        listOfPos[emptyPos] = letter
                        listOfPos[nextLetterPos] = "E"
                        moves += [listToString(listOfPos)]
                    elif(emptyPos==0):
                        if(listOfPos[nextLetterPos-1] == letter and listOfPos[nextLetterPos+1] == letter):
                            continue
                        else:
                            listOfPos[emptyPos] = letter
                            listOfPos[nextLetterPos] = "E"
                            moves += [listToString(listOfPos)]
            else:
                if(nextLetterPos==emptyPos+1 or nextLetterPos==emptyPos-1 or nextLetterPos==0):
                    listOfPos[emptyPos] = letter
                    listOfPos[nextLetterPos] = "E"
                    moves += [listToString(listOfPos)]
                elif(emptyPos==0):
                    if(listOfPos[nextLetterPos-1] == letter and listOfPos[nextLetterPos+1] == letter):
                        continue
                    else:
                        listOfPos[emptyPos] = letter
                        listOfPos[nextLetterPos] = "E"
                        moves += [listToString(listOfPos)]
        except:
            continue
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
            print(position + "\nPlayer 2 Wins!")
            return position
        if "OEO" in position[1:] and position[0] == "O":
            print(position + "\nPlayer 1 Wins!")
            return position

test = None
while True:
    if(test!="r"):
        test = input()

    if(checkWin(currentPos)):
        break
    
    if(test=="n" or test=="r"):
        playerOMoves = possibleMoves(currentPos, "O")
        if stratOne(playerOMoves, "O") == None:
            currentPos = stratTwo(playerOMoves, "O")
        else:
            currentPos = stratOne(playerOMoves, "O")
        
        if(test=="n"):
            print(currentPos)

    if(test!="r"):
        test = input()
    
    if(checkWin(currentPos)):
        break

    if(test=="n" or test=="r"):
        playerXMoves = possibleMoves(currentPos, "X")
        if stratOne(playerXMoves, "X") == None:
            currentPos = stratTwo(playerXMoves, "X")
        else:
            currentPos = stratOne(playerXMoves, "X")
        
        if(test=="n"):
            print(currentPos)

# print(possibleMoves(currentPos, "O"))