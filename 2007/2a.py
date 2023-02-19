# startingPos = "EOOOOXXXX"
startingPos = "XOOOOXXOE"

def strat1(position,letter):
    endPosition = None
    for i in range(len(position)-1):
        if i == 0:
            middle = position[i]
        if(letter == "X" and middle == letter):
            if i == 1:
                    if((position[8] == "E" and position[i+1] == letter and position[i] == "O") or (position[8] == letter and position[i+1] == "E" and position[i] == "O")):
                        endPosition = "E" + position[1:].replace("E",letter)
            elif i == 8:
                    if((position[i-1] == "E" and position[1] == letter and position[i] == "O") or (position[i-1] == letter and position[1] == "E" and position[i] == "O")):
                        endPosition = "E" + position[1:].replace("E",letter)
            else:
                    if((position[i-1] == "E" and position[i+1] == letter and position[i] == "O") or (position[i-1] == letter and position[i+1] == "E" and position[i] == "O")):
                        endPosition = "E" + position[1:].replace("E",letter)

        if(letter == "O" and middle == letter):
            if i == 1:
                    if((position[8] == "E" and position[i+1] == letter and position[i] == "O") or (position[8] == letter and position[i+1] == "E" and position[i] == "O")):
                        endPosition = "E" + position[1:].replace("E",letter)
            elif i == 8:
                    if((position[i-1] == "E" and position[1] == letter and position[i] == "O") or (position[i-1] == letter and position[1] == "E" and position[i] == "O")):
                        endPosition = "E" + position[1:].replace("E",letter)
            else:
                    if((position[i-1] == "E" and position[i+1] == letter and position[i] == "O") or (position[i-1] == letter and position[i+1] == "E" and position[i] == "O")):
                        endPosition = "E" + position[1:].replace("E",letter)
        
        if(endPosition):
            return endPosition
        else:
            return position

print(strat1(startingPos,"X"))