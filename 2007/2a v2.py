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
        # if letter == "X":
        #     if "XEX" in move[1:] and move[0] == letter:
        #         if move[0] == letter:
        #             return move
        # if letter == "O":
        #     if "OEO" in move[1:] and move[0] == letter:
        #         if move[0] == letter:
        #             return move
        if letter == "X":
            if ("XEX" in move[1:] and move[0] == "X") or ("XE" in move[7:9] and move[1] == "X" and move[0] == "X") or ("EX" in move[1:3] and move[8] == "X" and move[0] == "X"):
                return move
        if letter == "O":
            if ("OEO" in move[1:] and move[0] == "O") or ("OE" in move[7:9] and move[1] == "O" and move[0] == "O") or ("EO" in move[1:3] and move[8] == "O" and move[0] == "O"):
                return move
    # return moves[0]

def stratTwo(moves,opponentLetter):
    for move in moves:
        possibleOpponentMoves = possibleMoves(move, opponentLetter)
        if not stratOne(possibleOpponentMoves, opponentLetter):
            return move
    return moves[0]

def checkWin(position):
    if ("XEX" in position[1:] and position[0] == "X") or ("XE" in position[7:9] and position[1] == "X" and position[0] == "X") or ("EX" in position[1:3] and position[8] == "X" and position[0] == "X"):
        print(position + "\nPlayer 2 Wins!")
        return position
    if ("OEO" in position[1:] and position[0] == "O") or ("OE" in position[7:9] and position[1] == "O" and position[0] == "O") or ("EO" in position[1:3] and position[8] == "O" and position[0] == "O"):
        print(position + "\nPlayer 1 Wins!")
        return position

test = None
count = 0

while True:
    count += 1
    if(test!="r"):
        test = input()
    
    if(checkWin(currentPos)):
        break
    
    playerOMoves = possibleMoves(currentPos, "O")
    if stratOne(playerOMoves, "O") == None:
        currentPos = stratTwo(playerOMoves, "X")
    else:
        currentPos = stratOne(playerOMoves, "O")
    
    if(checkWin(currentPos)):
        break
    elif(test=="n"):
        print(currentPos)

    if(test!="r"):
        test = input()

    playerXMoves = possibleMoves(currentPos, "X")
    if stratOne(playerXMoves, "X") == None:
        currentPos = stratTwo(playerXMoves, "O")
    else:
        currentPos = stratOne(playerXMoves, "X")
        
    if(checkWin(currentPos)):
        break
    elif(test=="n"):
        print(currentPos)

    if(count == 100):
        print("Draw")
        break

# print(possibleMoves(currentPos, "O"))